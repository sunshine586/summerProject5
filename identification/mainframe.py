from PyQt5 import QtWidgets, QtGui, QtCore
from identification.first import Ui_Dialog
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from identification.formal import Ui_Dialog  # 导入通过 pyuic 生成的界面类
from identification.frmodelframe import frmodelWindow  # 导入页面1的类
from identification.dimodelframe import dimodelWindow  # 导入页面2的类
# from identification.firstframe import FirstWindow  # 导入页面3的类

class MainWindow(QtWidgets.QMainWindow,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置界面布局和组件
        # 连接按钮的点击事件到对应的槽函数
        self.pushButton.clicked.connect(self.show_page1)
        self.pushButton_2.clicked.connect(self.show_page2)
        self.pushButton_3.clicked.connect(self.show_page3)

    def show_page1(self):
        self.page1 = frmodelWindow()  # 创建页面1的实例
        self.page1.show()  # 显示页面1
        self.close()

    def show_page2(self):
        self.page2 = dimodelWindow()  # 创建页面2的实例
        self.page2.show()  # 显示页面2
        self.close()

    def show_page3(self):
        from identification.firstframe import FirstWindow
        self.nextpage = FirstWindow()
        self.nextpage.show()
        self.close()

