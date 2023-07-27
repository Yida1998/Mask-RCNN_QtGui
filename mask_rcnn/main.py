"""
Author: yida
Time is: 2022/6/27 10:36 
this Code: 调用mask_rcnn实现土壤分割系统
"""

import json
import os
import sys
import time

import PySide2
import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication  # 加载窗口
from PySide2.QtWidgets import QFileDialog  # 加载文件
from torchvision import transforms

from backbone import resnet50_fpn_backbone
from draw_box_utils import draw_objs
from network_files import MaskRCNN

# os.environ['QT_MAC_WANTS_LAYER'] = '1'

# 解决无法启动的问题
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class Mask_RCNN:
    def __init__(self, ui, img_path, weights_path='./best.pt'):
        self.ui = ui
        self.num_classes = 1  # 不包含背景
        self.box_thresh = 0.9
        self.weights_path = weights_path  # 模型权重
        self.img_path = img_path  # 图像路径
        self.label_json_path = 'coco91_indices.json'

    def master(self):
        num_classes = self.num_classes  # 不包含背景
        box_thresh = self.box_thresh
        weights_path = self.weights_path
        img_path = self.img_path
        label_json_path = self.label_json_path
        # get devices
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        print("using {} device.".format(device))
        self.ui.textEdit.append("using {} device.".format(device))

        # create model
        model = self.create_model(num_classes=num_classes + 1, box_thresh=box_thresh)

        # load train weights
        assert os.path.exists(weights_path), "{} file dose not exist.".format(weights_path)
        model.load_state_dict(torch.load(weights_path, map_location='cpu')["model"])
        model.to(device)
        # read class_indict
        assert os.path.exists(label_json_path), "json file {} dose not exist.".format(label_json_path)
        with open(label_json_path, 'r') as json_file:
            category_index = json.load(json_file)

        # load image
        assert os.path.exists(img_path), f"{img_path} does not exits."
        original_img = Image.open(img_path).convert('RGB')

        # from pil image to tensor, do not normalize image
        data_transform = transforms.Compose([transforms.ToTensor()])
        img = data_transform(original_img)
        # expand batch dimension
        img = torch.unsqueeze(img, dim=0)

        model.eval()  # 进入验证模式
        with torch.no_grad():
            # init
            img_height, img_width = img.shape[-2:]
            init_img = torch.zeros((1, 3, img_height, img_width), device=device)
            model(init_img)

            t_start = self.time_synchronized()
            predictions = model(img.to(device))[0]
            t_end = self.time_synchronized()
            print("inference+NMS time: {}".format(t_end - t_start))
            self.ui.textEdit.append("inference+NMS time: {}".format(t_end - t_start))

            predict_boxes = predictions["boxes"].to("cpu").numpy()
            predict_classes = predictions["labels"].to("cpu").numpy()
            predict_scores = predictions["scores"].to("cpu").numpy()
            predict_mask = predictions["masks"].to("cpu").numpy()
            predict_mask = np.squeeze(predict_mask, axis=1)  # [batch, 1, h, w] -> [batch, h, w]
            if len(predict_boxes) == 0:
                print("没有检测到任何目标!")
                self.ui.textEdit.append("没有检测到任何目标!")

                return
            print("类别: {}  置信度: {} ".format(category_index, predict_scores))
            self.ui.textEdit.append("类别: {}  置信度: {} ".format(category_index, predict_scores))

            # plt.figure(figsize=(40, 30))
            plot_img = draw_objs(original_img,
                                 boxes=predict_boxes,
                                 classes=predict_classes,
                                 scores=predict_scores,
                                 masks=predict_mask,
                                 category_index=category_index,
                                 line_thickness=10,  # 3
                                 font='font.sans-serif.ttf',
                                 font_size=100)  # 20
            # plt.imshow(plot_img)
            # plt.show()
            # 保存预测的图片结果
            # plot_img.save("./test_result.jpg")
            # 保存mask图像

            img = np.array(original_img)
            # img = cv2.imread(img_path)
            predict_mask = np.array(np.squeeze(predict_mask, axis=0))
            predict_mask = np.where(predict_mask > 0.5, 1, 0)  # 这个mask是对每个类别都有一个,输出的值是0-1之间的概率, 所以要加一个判断

            img[:, :, 0] = img[:, :, 0] * predict_mask
            img[:, :, 1] = img[:, :, 1] * predict_mask
            img[:, :, 2] = img[:, :, 2] * predict_mask
            # img[img == 0] = 255
            b, g, r = cv2.split(img)
            factor = np.where((b == r) & (r == g) & (b == 0))
            b[factor] = 255
            g[factor] = 255
            r[factor] = 255
            img = cv2.merge([b, g, r])
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            # 左上 右下 四个点
            point_l, point_t, point_r, point_b = int(predict_boxes[0][0]), int(predict_boxes[0][1]), int(predict_boxes[0][2]), int(predict_boxes[0][3])
            # 仅获取外接矩形区域
            test_cut = img[point_t:point_b, point_l:point_r]
            # cv2.imwrite("./test_cut.jpg", test_cut)
            # mask结果 + 最小外接矩形
            cv2.rectangle(img, (point_l, point_t), (point_r, point_b), (0, 0, 255), 10)
            # cv2.imwrite("./test_maskResult.jpg", img)
            # 保存mask二值图
            predict_mask = np.where(predict_mask == 1, 255, 0)
            # cv2.imwrite("./test_mask.jpg", predict_mask)
            return plot_img, img, test_cut

    @staticmethod
    def create_model(num_classes, box_thresh=0.5):
        backbone = resnet50_fpn_backbone()
        model = MaskRCNN(backbone,
                         num_classes=num_classes,
                         rpn_score_thresh=box_thresh,
                         box_score_thresh=box_thresh)

        return model

    @staticmethod
    def time_synchronized():
        torch.cuda.synchronize() if torch.cuda.is_available() else None
        return time.time()

    def save_maskResult(self, mask, path_save):
        """
        保存最终分割结
        :param mask:
        :param path_save:
        :return:
        """
        cv2.imwrite(path_save, mask)


class QtSegmentation:
    def __init__(self):
        # --------------------------ui------------------------------

        # 从文件中加载UI定义
        self.ui = QUiLoader().load('./mask_rcnn.ui')

        # 按钮1: 加载模型
        self.ui.pushButton_1.clicked.connect(self.button1_loadModel)

        # 按钮2: 加载图像
        self.ui.pushButton_2.clicked.connect(self.button2_loadImage)
        self.ui.pushButton_2.setEnabled(False)

        # 按钮3: 图像分割
        self.ui.pushButton_3.clicked.connect(self.button3_segImage)
        self.ui.pushButton_3.setEnabled(False)

        # 按钮4: 保存图像
        self.ui.pushButton_4.clicked.connect(self.button4_saveImage)
        self.ui.pushButton_4.setEnabled(False)


        # 进度条
        # self.ui.progressBar.setRange(0, 5)        # 这玩意不起作用

        # ---------------------------model-------------------------------
        # 初始化模型参数
        self.model_path = './best.pth'  # 默认模型, 可加载
        self.img_path = None  # 图像路径
        # 分割结果保存
        self.seg_img = './seg_img.png'
        self.img_load = './load_img.png'    # 解决qt不显示24位图像 重新保存图像在加载
        # mask图像
        self.mask = None
        # model
        self.model = None
        # 最小外接矩形
        self.cut = None

    def button1_loadModel(self):
        """
        按钮事件1
        :return:
        """
        # 加载模型
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "加载训练模型",  # 标题
            r"",  # 起始目录
            # "模型 (*.pth, *.pt)"  # 选择类型过滤项，过滤内容在括号中
            "(*.pth *.pt)"  # 选择类型过滤项，过滤内容在括号中
        )
        if filePath is None:
            self.ui.textEdit.append("请正确输入模型路径...", filePath)
        else:
            self.ui.textEdit.append("加载模型: {}".format(filePath))
            self.model_path = filePath
        # 情况label1和label2的幕布
        self.ui.label1.clear()
        self.ui.label2.clear()

        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)



    def button2_loadImage(self):
        """
        按钮事件2
        :return:
        """
        # 选择图像
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择土壤图像",  # 标题
            r"",  # 起始目录
            "*.jpg *.png *.jpeg"  # 选择类型过滤项，过滤内容在括号中
        )
        if filePath is None:
            self.ui.textEdit.append("请正确加载图像路径...", filePath)

        else:
            self.ui.textEdit.append("加载图像路径: {}".format(filePath))
            # 显示图像
            print(filePath)
            # 重新保存图像
            img_load = cv2.imread(filePath)
            cv2.imwrite(self.img_load, img_load)
            self.ui.label1.setPixmap(self.img_load)
            self.ui.label1.setFixedSize(500, 375)
            # 先清空label2
            self.ui.label2.clear()
            # 获取图像路径
            self.img_path = filePath
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_2.setEnabled(False)

    def button3_segImage(self):
        """
        按钮事件3
        :return:
        """
        img_path = self.img_path
        if img_path is None:
            self.ui.textEdit.append("请加载正确的图像...")
        else:
            model_path = self.model_path
            # 打开图像
            model = Mask_RCNN(ui=self.ui, img_path=img_path, weights_path=model_path)
            self.model = model
            plt_img, self.mask, self.cut = model.master()
            plt_img = np.array(plt_img)
            plt_img = cv2.cvtColor(plt_img, cv2.COLOR_RGB2BGR)
            # 保存图像
            cv2.imwrite(self.seg_img, plt_img)
            self.ui.textEdit.append("图像分割已完成...")

            # 显示图像
            self.ui.label2.setPixmap(self.seg_img)
            self.ui.label2.setFixedSize(500, 375)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(True)

    def button4_saveImage(self):
        """
        按钮事件4: 保存图像
        :return:
        """
        model = self.model
        filePath, _ = QFileDialog.getSaveFileName(
            self.ui,  # 父窗口对象
            "保存土壤图像",  # 标题
            r"",  # 起始目录
            "图片类型 (*.png *.jpg *.jpeg)"  # 选择类型过滤项，过滤内容在括号中
        )
        if filePath is None:
            self.ui.textEdit.append("请输入正确路径...")
        else:
            model.save_maskResult(self.mask, filePath)
            # 获取新路径
            filePath_cut = filePath.split('.')[0] + '_cut' + '.png'
            model.save_maskResult(self.cut, filePath_cut)
            self.ui.textEdit.append("成功保存图像路径为: {}".format(filePath))
            self.ui.textEdit.append("成功保存图像外接矩形路径为: {}".format(filePath_cut))
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)


if __name__ == '__main__':
    # 解决mac下的问题提示
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

    # 初始化
    app = QApplication(sys.argv)
    # 实例化类
    seg = QtSegmentation()
    # 显示
    seg.ui.show()
    # 关闭
    app.exec_()
