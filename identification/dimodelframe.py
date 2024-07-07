import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from identification.dimodel import Ui_Dialog
from identification.dishesIdentify import ImageUploader

class dimodelWindow(QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置界面布局和组件

        # 连接按钮的点击事件到对应的槽函数
        self.pushButton.clicked.connect(self.function1)
        self.pushButton_2.clicked.connect(self.function2)
        self.pushButton_3.clicked.connect(self.function3)

    # 菜品识别
    def function1(self):
        print("Button 1 clicked. Function 1 executed.")
        self.nextframe = ImageUploader()
        self.nextframe.show()
        self.close()

    # 查看识别菜品记录
    def function2(self):
        # Add your code for function 2 here
        from identification.dishesview import NutritionDialog
        self.nextwindow = NutritionDialog()
        self.nextwindow.show()
        self.close()

    # 返回
    def function3(self):
        from identification.mainframe import MainWindow
        self.nextpage = MainWindow()
        self.nextpage.show()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWindow = dimodelWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())
