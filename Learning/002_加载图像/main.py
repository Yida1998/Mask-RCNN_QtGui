"""
Author: yida
Time is: 2022/6/26 22:04 
this Code: 
"""
"""
Author: yida
Time is: 2022/6/26 18:46 
this Code: 
"""
import os

import cv2
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog  # 加载图像

os.environ['QT_MAC_WANTS_LAYER'] = '1'


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.path = "/Users/yida/Downloads/图片/萌图/1.jpg"
        self.img = cv2.imread(self.path)
        self.ui = QUiLoader().load('../ui/ui001.ui')

        # 按钮1
        self.ui.pushButton1.clicked.connect(self.handleCalc1)
        self.ui.pushButton1.setText("输出路径")

        # 按钮2
        self.ui.pushButton2.clicked.connect(self.handleCalc2)
        self.ui.pushButton2.setText("加载图像1")

        # 按钮3
        self.ui.pushButton3.clicked.connect(self.handleCalc3)
        self.ui.pushButton3.setText("加载图像2")

    def handleCalc1(self):
        # self.ui.textEdit.clear()  # 清楚文本内容
        self.ui.textEdit.append(self.path)
        info = self.ui.textEdit.toPlainText()  # 获取文本内容
        print(info)

    def handleCalc2(self):
        # self.ui.textEdit.clear()   # 清楚文本内容
        img_name = QFileDialog.getOpenFileName(
            self.ui,
            "加载图像",
            r"./",  # 起始目录
        )
        self.path = img_name[0]
        self.ui.textEdit.append(self.path)
        # 更换label图像2
        self.ui.label1.setPixmap(self.path)
        self.ui.label1.setFixedSize(500, 500)

    def handleCalc3(self):
        # self.ui.textEdit.clear()   # 清楚文本内容
        img_name = QFileDialog.getOpenFileName(
            self.ui,
            "加载图像",
            r"./",  # 起始目录
        )
        self.path = img_name[0]
        self.ui.textEdit.append(self.path)
        print(self.path)
        # 更换label图像2
        self.ui.label2.setPixmap(self.path)
        self.ui.label2.setFixedSize(500, 500)


if __name__ == '__main__':
    # 解决mac下的问题提示
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    # 初始化
    app = QApplication([])
    # 实例化类
    stats = Stats()
    stats.ui.show()
    app.exec_()
