# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(592, 456)
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 140, 113, 54))
        self.splitter.setOrientation(Qt.Vertical)

        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")

        self.splitter.addWidget(self.pushButton)
        self.toolButton = QToolButton(self.splitter)
        self.toolButton.setObjectName(u"toolButton")
        self.splitter.addWidget(self.toolButton)

        self.retranslateUi(Form)


        self.textEdit = QPlainTextEdit(self.splitter)
        self.textEdit.setPlaceholderText("111111")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"\u52a0\u6cb9", None))
    # retranslateUi

if __name__ == '__main__':
    ui = Ui_Form()
    ui.setupUi(QWidget)

