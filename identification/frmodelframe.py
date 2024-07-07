import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from identification.frmodel import Ui_Dialog
from identification.fruitIdentify import ImageUploader  # 导入下一个页面的类
from identification.fruitview import NutritionDialog

class frmodelWindow(QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置界面布局和组件
        # 连接按钮的点击事件到对应的槽函数
        self.pushButton.clicked.connect(self.function1)
        self.pushButton_2.clicked.connect(self.function2)
        self.pushButton_3.clicked.connect(self.function3)
        self.view = {}

    # 跳转到果蔬识别页面
    def function1(self):
        self.nextframe = ImageUploader()
        self.nextframe.show()
        self.close()


    # 查看果蔬识别记录
    def function2(self):
        from identification.fruitview import NutritionDialog
        self.nextwindow = NutritionDialog()
        self.nextwindow.show()
        self.close()

    # 返回
    def function3(self):
        from identification.mainframe import MainWindow
        self.nextpage = MainWindow()
        self.nextpage.show()
        self.close()

