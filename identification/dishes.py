# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dishes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(855, 687)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 881, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, -10, 891, 721))
        self.label.setStyleSheet("background-image: url(:/bg1.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(150, 50, 641, 101))
        self.label_4.setStyleSheet("color: rgb(56, 99, 7);\n"
"color: rgb(0, 0, 0);\n"
"font: 24pt \"楷体\";")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 180, 411, 311))
        self.label_2.setStyleSheet("border: 2px dashed gray; /* 2像素宽的灰色虚线边框 */  \n"
"border-radius: 5px;      /* 可选：添加圆角 */  ")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 550, 171, 41))
        self.pushButton_2.setStyleSheet("background-image: url(:/bg1.jpg);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"楷体\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 550, 171, 41))
        self.pushButton_3.setStyleSheet("background-image: url(:/bg1.jpg);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"楷体\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 550, 171, 41))
        self.pushButton_4.setStyleSheet("background-image: url(:/bg1.jpg);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"楷体\";")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "农家乐——果蔬识别与菜品识别系统"))
        self.pushButton_2.setText(_translate("Dialog", "上传图片"))
        self.pushButton_3.setText(_translate("Dialog", "开始识别"))
        self.pushButton_4.setText(_translate("Dialog", "返回"))
import data.a_rc