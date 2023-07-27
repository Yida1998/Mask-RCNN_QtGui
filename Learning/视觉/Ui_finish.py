# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\视觉练习\finish.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow 
import cv2
import numpy as np

class Ui_MainWindow(object):

    image = cv2.imread('lena.jpg')
    image1 = cv2.imread('boat.bmp')
    image2 = cv2.imread('test1.jpg')
    image3 = cv2.imread('lesson2.jpg')
    image4 = cv2.imread('shop.jpg')
    image5 = cv2.imread('computer.jpg')
    image6 = cv2.imread('lenaNoise.jpg')
    image7 =cv2.imread('dolphins.jpg')
    image8 = cv2.imread('paojie.jpg')
    image9 = cv2.imread('inpaint2.jpg')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 30, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 60, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 60, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(730, 20, 131, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 60, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(730, 140, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(90, 30, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 512, 512))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 230, 512, 512))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 180, 1151, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(370, 60, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(370, 90, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(90, 120, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(180, 120, 75, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(270, 120, 75, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(730, 50, 111, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(370, 120, 75, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(540, 20, 75, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(540, 50, 75, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(540, 80, 75, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(540, 110, 75, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(540, 140, 75, 23))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(180, 150, 75, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(730, 80, 75, 23))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(730, 110, 75, 23))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(270, 150, 75, 23))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(180, 90, 75, 23))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(270, 90, 75, 23))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(950, 80, 75, 23))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(950, 110, 75, 23))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(820, 80, 75, 23))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(820, 110, 75, 23))
        self.pushButton_33.setObjectName("pushButton_33")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 20, 20, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(630, 20, 20, 151))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 40, 51, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 50, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 180, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(630, 180, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1213, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2019030002103 = QtWidgets.QMenu(self.menubar)
        self.menu_2019030002103.setObjectName("menu_2019030002103")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2019030002103.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_1.clicked.connect(self.btn1_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)
        self.pushButton_3.clicked.connect(self.btn3_clicked)
        self.pushButton_4.clicked.connect(self.btn4_clicked)
        self.pushButton_5.clicked.connect(self.btn5_clicked)
        self.pushButton_6.clicked.connect(self.btn6_clicked)
        self.pushButton_7.clicked.connect(self.btn7_clicked)
        self.pushButton_8.clicked.connect(self.btn8_clicked)
        self.pushButton_9.clicked.connect(self.btn9_clicked)
        self.pushButton_10.clicked.connect(self.btn10_clicked)
        self.pushButton_11.clicked.connect(self.btn11_clicked)
        self.pushButton_12.clicked.connect(self.btn12_clicked)
        self.pushButton_13.clicked.connect(self.btn13_clicked)
        self.pushButton_14.clicked.connect(self.btn14_clicked)
        self.pushButton_15.clicked.connect(self.btn15_clicked)
        self.pushButton_16.clicked.connect(self.btn16_clicked)
        self.pushButton_17.clicked.connect(self.btn17_clicked)
        self.pushButton_18.clicked.connect(self.btn18_clicked)
        self.pushButton_19.clicked.connect(self.btn19_clicked)
        self.pushButton_20.clicked.connect(self.btn20_clicked)
        self.pushButton_21.clicked.connect(self.btn21_clicked)
        self.pushButton_22.clicked.connect(self.btn22_clicked)
        self.pushButton_23.clicked.connect(self.btn23_clicked)
        self.pushButton_24.clicked.connect(self.btn24_clicked)
        self.pushButton_25.clicked.connect(self.btn25_clicked)
        self.pushButton_26.clicked.connect(self.btn26_clicked)
        self.pushButton_27.clicked.connect(self.btn27_clicked)
        self.pushButton_28.clicked.connect(self.btn28_clicked)
        self.pushButton_29.clicked.connect(self.btn29_clicked)
        self.pushButton_30.clicked.connect(self.btn30_clicked)
        self.pushButton_31.clicked.connect(self.btn31_clicked)
        self.pushButton_32.clicked.connect(self.btn32_clicked)
        self.pushButton_33.clicked.connect(self.btn33_clicked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "a+b"))
        self.pushButton_4.setText(_translate("MainWindow", "add(a,b)"))
        self.pushButton_5.setText(_translate("MainWindow", "rgb"))
        self.pushButton_6.setText(_translate("MainWindow", "bgr"))
        self.pushButton_7.setText(_translate("MainWindow", "按位逻辑运算(取反)"))
        self.pushButton_8.setText(_translate("MainWindow", "掩模"))
        self.pushButton_9.setText(_translate("MainWindow", "伪彩色"))
        self.pushButton_1.setText(_translate("MainWindow", "原图"))
        self.pushButton_2.setText(_translate("MainWindow", "自我介绍"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_10.setText(_translate("MainWindow", "二值化"))
        self.pushButton_11.setText(_translate("MainWindow", "水平翻转"))
        self.pushButton_12.setText(_translate("MainWindow", "旋转"))
        self.pushButton_13.setText(_translate("MainWindow", "缩放"))
        self.pushButton_14.setText(_translate("MainWindow", "透视"))
        self.pushButton_15.setText(_translate("MainWindow", "卷积运算"))
        self.pushButton_16.setText(_translate("MainWindow", "彩色椒盐噪声"))
        self.pushButton_17.setText(_translate("MainWindow", "sift检测"))
        self.pushButton_18.setText(_translate("MainWindow", "均值滤波"))
        self.pushButton_19.setText(_translate("MainWindow", "方框滤波"))
        self.pushButton_20.setText(_translate("MainWindow", "高斯滤波"))
        self.pushButton_21.setText(_translate("MainWindow", "中值滤波"))
        self.pushButton_22.setText(_translate("MainWindow", "双边滤波"))
        self.pushButton_23.setText(_translate("MainWindow", "图像锐化"))
        self.pushButton_24.setText(_translate("MainWindow", "浮雕效果"))
        self.pushButton_25.setText(_translate("MainWindow", "平均值池化"))
        self.pushButton_26.setText(_translate("MainWindow", "图像修复"))
        self.pushButton_27.setText(_translate("MainWindow", "轮廓检测"))
        self.pushButton_28.setText(_translate("MainWindow", "垂直翻转"))
        self.pushButton_29.setText(_translate("MainWindow", "沿XY轴翻转"))
        self.pushButton_30.setText(_translate("MainWindow", "图像金字塔"))
        self.pushButton_31.setText(_translate("MainWindow", "连通域计算"))
        self.pushButton_32.setText(_translate("MainWindow", "腐蚀"))
        self.pushButton_33.setText(_translate("MainWindow", "膨胀"))
        self.label_3.setText(_translate("MainWindow", "滤波"))
        self.label_4.setText(_translate("MainWindow", "lena区"))
        self.label_5.setText(_translate("MainWindow", "其他"))
        self.label_6.setText(_translate("MainWindow", "原图"))
        self.label_7.setText(_translate("MainWindow", "处理后"))
        self.menu.setTitle(_translate("MainWindow", "art1"))
        self.menu_2019030002103.setTitle(_translate("MainWindow", "art2"))

    def btn1_clicked(self):
        self.image_1 = self.image
        self.image_1 = QtGui.QImage(self.image_1.data, self.image_1.shape[1], self.image_1.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_1))


    def btn2_clicked(self):
        # 自我介绍
        imageDst = np.zeros(self.image.shape,np.uint8)
        cv2.copyTo(self.image,None,imageDst)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(imageDst,"I am Lena.",(50,50) ,font,2,(20,200,20),2)
        self.image_intro = imageDst
        self.image_intro = QtGui.QImage(self.image_intro.data, self.image_intro.shape[1], self.image_intro.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.image_intro))
  

    def btn3_clicked(self):
        # a+b
        a=self.image
        b=a
        self.result=a+b
        self.result = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result))

    def btn4_clicked(self):
        # add(a,b)
        a=self.image
        b=a
        self.result=cv2.add(a,b)
        self.result = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result))
    
    def btn5_clicked(self):
        # rgb
        b,g,r = cv2.split(self.image)
        self.image_bgr =cv2.merge([r,g,b])
        self.image_bgr = QtGui.QImage(self.image_bgr.data, self.image_bgr.shape[1], self.image_bgr.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.image_bgr))

    def btn6_clicked(self):
        #bgr
        b,g,r = cv2.split(self.image)
        self.image_bgr =cv2.merge([b,g,r])
        self.image_bgr = QtGui.QImage(self.image_bgr.data, self.image_bgr.shape[1], self.image_bgr.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.image_bgr))


    def btn7_clicked(self):
        # 按位逻辑运算(取反)
        self.shop_not = cv2.bitwise_not(self.image4)
        self.shop_not = QtGui.QImage(self.shop_not.data, self.shop_not.shape[1], self.shop_not.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.shop_not))

        self.image_shop1 = self.image4
        self.image_shop1 = QtGui.QImage(self.image_shop1.data, self.image_shop1.shape[1], self.image_shop1.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_shop1))

        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.shop_not))

    def btn8_clicked(self):
        # 掩模
        a=cv2.imread("Lena.jpg",1)
        w,h,c=a.shape
        m=np.zeros((w,h),dtype=np.uint8)
        m[100:400,200:400]=255
        m[100:500,100:200]=255
        c=cv2.bitwise_and(a,a,mask=m)
        self.result=cv2.bitwise_and(a,a,mask=m)
        self.result = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()   
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result))

    def btn9_clicked(self):
        # 伪彩色
        self.result=cv2.applyColorMap(self.image2,cv2.COLORMAP_COOL)
        self.result = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result))

        self.image_shop1 = self.image2
        self.image_shop1 = QtGui.QImage(self.image_shop1.data, self.image_shop1.shape[1], self.image_shop1.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_shop1))


    #图像二值化
    def btn10_clicked(self):
        lena1 = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.t,self.rst = cv2.threshold(lena1,127,255,cv2.THRESH_BINARY)
        self.rst = QtGui.QImage(self.rst.data, self.rst.shape[1], self.rst.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.rst))

    #图像水平翻转
    def btn11_clicked(self):
        self.x = cv2.flip(self.image,0)
        self.x = QtGui.QImage(self.x.data, self.x.shape[1], self.x.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.x))

    
    
        

    #仿射映射-旋转
    def btn12_clicked(self):
        height,width = self.image.shape[:2]
        M = cv2.getRotationMatrix2D((width/2,height/2),50,0.3)
        self.rotate = cv2.warpAffine(self.image,M,(width,height))
        self.rotate = QtGui.QImage(self.rotate.data, self.rotate.shape[1], self.rotate.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.rotate))

    
    # 图像缩放
    def btn13_clicked(self):
        self.imageDst = cv2.resize(self.image,None,fx = 0.5,fy=0.5)
        self.imageDst = QtGui.QImage(self.imageDst.data, self.imageDst.shape[1], self.imageDst.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.imageDst))


    #透视
    def btn14_clicked(self):
        rows,cols = self.image.shape[:2]
        pts1 = np.float32([[150,50],[400,50],[60,450],[310,450]])
        pts2 = np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        self.dst = cv2.warpPerspective(self.image,M,(cols,rows))
        self.dst = QtGui.QImage(self.dst.data, self.dst.shape[1], self.dst.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.dst))
    
    # A05
    # 图像卷积运算
    def btn15_clicked(self):
        kernel2 = np.ones((7, 7), np.float32) / 49
        self.result2 = cv2.filter2D(self.image, -1, kernel=kernel2)
        self.result2 = QtGui.QImage(self.result2.data, self.result2.shape[1], self.result2.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result2))

    # # 彩色图像添加椒盐噪声
    def btn16_clicked(self):
        def add_noisy(image, n=10000):
            result = image.copy()
            w, h = image.shape[:2]
            for i in range(n):
                # 宽和高的范围内生成一个随机值，模拟表x,y坐标
                x = np.random.randint(1, w)
                y = np.random.randint(1, h)
                if np.random.randint(0, 2) == 0:
                    # 生成白色噪声（盐噪声）
                    result[x, y] = 0
                else:
                    # 生成黑色噪声（椒噪声）
                    result[x, y] = 255
            return result
        
        self.image_shop1 = self.image7
        self.image_shop1 = QtGui.QImage(self.image_shop1.data, self.image_shop1.shape[1], self.image_shop1.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_shop1))

        self.color_image_noisy = add_noisy(self.image7, 10000)
        self.color_image_noisy = QtGui.QImage(self.color_image_noisy.data, self.color_image_noisy.shape[1], self.color_image_noisy.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.color_image_noisy))


    # 灰度图像添加椒盐噪声
    
    # # 彩色图像添加高斯噪声
    # def btn17_clicked(self):
    #     def add_noise(image,mean=0,val=0.01):
    #         size = image.shape
    #         # 像素值进行归一化
    #         image = image / 255
    #         # size 指定了尺寸
    #         gauss = np.random.normal(mean,val**0.5,size)
    #         noise = image + gauss
    #         return gauss,noise

    #     self.color_noisy_image = add_noise(self.image)
    #     self.color_noisy_image = QtGui.QImage(self.color_noisy_image.data, self.color_noisy_image.shape[1], self.color_noisy_image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
    #     self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.color_noisy_image))
    def btn17_clicked(self):
        sift = cv2.SIFT_create()
        kps = sift.detect(self.image)
        self.image_sift = cv2.drawKeypoints(self.image, kps, None, -1, cv2.DrawMatchesFlags_DEFAULT)
        self.image_sift = QtGui.QImage(self.image_sift.data, self.image_sift.shape[1], self.image_sift.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.image_sift))
    #灰色图像添加高斯噪声
    
    #均值滤波
    def btn18_clicked(self):
        self.image_Noise = self.image6
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise))

        self.blur_result=cv2.blur(self.image6,(5,5))
        self.blur_result = QtGui.QImage(self.blur_result.data, self.blur_result.shape[1], self.blur_result.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.blur_result))

    #方波滤波
    def btn19_clicked(self):
        self.image_Noise = self.image6
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise))

        self.r=cv2.boxFilter(self.image6,-1,(2,2),normalize=0)
        self.r = QtGui.QImage(self.r.data, self.r.shape[1], self.r.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.r))

    #高斯滤波
    def btn20_clicked(self):
        self.image_Noise = self.image6
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise))

        self.r=cv2.GaussianBlur(self.image6,(5,5),0,0)
        self.r = QtGui.QImage(self.r.data, self.r.shape[1], self.r.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.r))

    #中值滤波
    def btn21_clicked(self):
        self.image_Noise = self.image6
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise))

        self.r=cv2.medianBlur(self.image6,3)
        self.r = QtGui.QImage(self.r.data, self.r.shape[1], self.r.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.r))

    #双边滤波
    def btn22_clicked(self):
        self.image_Noise = self.image6
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise))

        self.r=cv2.bilateralFilter(self.image6,25,100,100)
        self.r = QtGui.QImage(self.r.data, self.r.shape[1], self.r.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.r))

    #图像锐化
    def btn23_clicked(self):
        lap_9 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
        # 拉普拉斯9的锐化
        self.dst = cv2.filter2D(self.image,cv2.CV_8U,lap_9)
        self.dst = QtGui.QImage(self.dst.data, self.dst.shape[1], self.dst.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.dst))

    #图像浮雕效果
    def btn24_clicked(self):
        ker = np.array([[-2,-1,0],
                        [-1,1,1],
                        [0,1,2]])
        self.img = cv2.filter2D(self.image,-1,kernel=ker)
        self.img = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.img))

    #平均值池化
    def btn25_clicked(self):
        def average_pooling(img,G=4):
            out=img.copy()
            H,W,C = img.shape
            Nh = int(H/G)
            Nw = int(W/G)
            for y in range(Nh):
                for x in range(Nw):
                    for c in range(C):
                        out[G*y:G*(y+1),G*x:G*(x+1),c] = np.mean(out[G*y:G*(y+1),G*x:G*(x+1),c]).astype(np.int)
            return out

        self.out = average_pooling(self.image8)
        self.out = QtGui.QImage(self.out.data, self.out.shape[1], self.out.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.out))

        self.image_Noise = self.image8
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise))

    #A09

    # 图像修复
    def btn26_clicked(self):
        
         
        _,mask1 = cv2.threshold(self.image9,245,255,cv2.THRESH_BINARY)
        k = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        mask1 = cv2.dilate(mask1,k)
        self.result1 = cv2.inpaint(self.image9,mask1[:,:,-1],5,cv2.INPAINT_NS)
        self.result1 = QtGui.QImage(self.result1.data, self.result1.shape[1], self.result1.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result1))

        self.image_Noise = self.image9
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise))

       

    

    def btn27_clicked(self):
        kernel = np.ones((3,3),dtype = np.uint8)
        open = cv2.morphologyEx(self.image,cv2.MORPH_OPEN,kernel)
        close = cv2.morphologyEx(self.image,cv2.MORPH_CLOSE,kernel)
        self.image_gradient = cv2.morphologyEx(self.image,cv2.MORPH_GRADIENT,kernel)
        
        self.image_gradient = QtGui.QImage(self.image_gradient.data, self.image_gradient.shape[1], self.image_gradient.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.image_gradient))

    def btn28_clicked(self):
        # 图像垂直翻转
        self.x = cv2.flip(self.image,1)
        self.x = QtGui.QImage(self.x.data, self.x.shape[1], self.x.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.x))

    def btn29_clicked(self):
        # 沿xy轴翻转
        self.x = cv2.flip(self.image,-1)
        self.x = QtGui.QImage(self.x.data, self.x.shape[1], self.x.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.x))
    
    def btn30_clicked(self):
        #图像金字塔
        import cv2 as cv
        def gauss_image(image):
            level = 3
            img = image.copy()
            gauss_images = []
            gauss_images.append(G0)
            cv.imshow("Gauss_0",G0)
            for i in range(level):
                dst = cv.pyrDown(img)
                gauss_images.append(dst)
                windName = 'Guass_{}'.format(i+1)
                cv.namedWindow(windName,1)
                cv.imshow(windName,dst)
                img = dst.copy()
            return gauss_images

        def laplian_image(image):
            gauss_images = gauss_image(image)
            level = len(gauss_images)
            for i in range(level-1,0,-1):
                expand = cv.pyrUp(gauss_images[i],dstsize=gauss_images[i-1].shape[:2])
                lpls = cv.subtract(gauss_images[i-1],expand)
                cv.imshow('Laplacian_{}'.format(level-i),lpls)
            expand = cv.pyrUp(cv.pyrDown(gauss_images[3]),dstsize=gauss_images[3].shape[:2])
            lpls = cv.subtract(gauss_images[3],expand)
            cv.imshow('Laplacian_{}'.format(0),lpls) 

        if __name__ == '__main__':
            G0 = cv.imread("Lena.jpg")
            if G0 is None:
                print('Failed to read lena.jpg.') 
                sys.exit()

            laplian_image(G0) 
            cv.waitKey(0)
            cv.destroyAllWindows() 
            
    def btn31_clicked(self):

        import cv2 as cv
        from numpy.random.mtrand import random

        def generate_random_color():
            return np.random.randint(0,256,3)
        def fill_color(img1,n,img2):
            h,w=img1.shape
            res = np.zeros((h,w,3),img1.dtype)
            #生成随机颜色
            random_color = {}
            for c in range(1,n):
                random_color[c] = generate_random_color()
            #为不同的连通域填色
            for i in range(h):
                for j in range(w):
                    item = img2[i][j]
                    if item == 0:
                        pass
                    else:
                        res[i,j,:]=random_color[item]
            return res
        if __name__== '__main__':
            #对图像进行读取，并转换为灰度图像
            rice = cv.imread('rice.png',cv.IMREAD_GRAYSCALE)
            if rice is None:
                print('..........')
                sys.exit()
            #将图像转成二值图像
            rice_BW = cv.threshold(rice,50,255,cv.THRESH_BINARY)
            #统计连通域
            count, dst = cv.connectedComponents(rice_BW[1],ltype=cv.CV_16U)

            #以不同颜色标记出不同的连通域
            self.result1 = fill_color(rice,count,dst)

            self.image_Noise = rice
            self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise))

            self.result1 = QtGui.QImage(self.result1.data, self.result1.shape[1], self.result1.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result1))

    def btn32_clicked(self):
        # 腐蚀
        o=cv2.imread("erode.bmp",cv2.IMREAD_UNCHANGED)
        kernel = np.ones((5,5),np.uint8)
        self.result1 = cv2.erode(o,kernel)
      
        self.result1 = QtGui.QImage(self.result1.data, self.result1.shape[1], self.result1.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result1))

        self.image_Noise = o
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise)) 
    
    def btn33_clicked(self):
        #膨胀
        o=cv2.imread("dilation.bmp",cv2.IMREAD_UNCHANGED)
        kernel = np.ones((9,9),np.uint8)
        self.result1 = cv2.dilate(o,kernel)
      
        self.result1 = QtGui.QImage(self.result1.data, self.result1.shape[1], self.result1.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.result1))

        self.image_Noise = o
        self.image_Noise = QtGui.QImage(self.image_Noise.data, self.image_Noise.shape[1], self.image_Noise.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image_Noise)) 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())