"""
Author: yida
Time is: 2022/6/26 18:46 
this Code: 
"""
import os

from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication  # 加载图像

os.environ['QT_MAC_WANTS_LAYER'] = '1'


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('../ui/ui001.ui')

        self.ui.pushButton1.clicked.connect(self.handleCalc1)
        self.ui.pushButton2.clicked.connect(self.handleCalc2)
        self.ui.pushButton3.clicked.connect(self.handleCalc3)

    def handleCalc1(self):
        self.ui.textEdit.clear()  # 清楚文本内容
        self.ui.textEdit.setText("姓名:陈怡达\n")
        info = self.ui.textEdit.toPlainText()  # 获取文本内容
        print(info)

    def handleCalc2(self):
        # self.ui.textEdit.clear()   # 清楚文本内容
        self.ui.textEdit.append("性别:男\n")
        info = self.ui.textEdit.toPlainText()  # 获取文本内容
        print(info)

    def handleCalc3(self):
        # self.ui.textEdit.clear()   # 清楚文本内容
        self.ui.textEdit.append("爱好:二次元\n")
        info = self.ui.textEdit.toPlainText()  # 获取文本内容
        print(info)


if __name__ == '__main__':
    # 解决mac下的问题提示
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    # 初始化
    app = QApplication([])
    # 实例化类
    stats = Stats()
    stats.ui.show()
    app.exec_()
