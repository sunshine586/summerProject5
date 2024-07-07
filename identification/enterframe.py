import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from identification.enter import Ui_Dialog  # 导入通过 pyuic 生成的界面类
from identification.mainframe import MainWindow  # 导入下一个页面的类

class EnterFrame(QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置界面布局和组件
        # 将按钮点击事件与处理函数连接
        self.pushButton.clicked.connect(self.goin)

    def goin(self):
        self.nextframe = MainWindow()
        self.nextframe.show()
        self.close()

