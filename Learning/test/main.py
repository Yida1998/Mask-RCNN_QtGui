"""
Author: yida
Time is: 2022/6/25 18:00 
this Code: 
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi  # 需要导入的模块


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        loadUi("/Users/yida/PycharmProjects/Test/QTGui/test/untitled.ui", self)  # 加载UI文件
        self.pushButton.clicked.connect(self.AA)  # 调用UI文件中的控件




    def AA(self):
        s = self.lineEdit.text()
        print(s)
        s = self.lineEdit_2.text()
        print(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec_())
