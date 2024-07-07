from PyQt5 import QtWidgets, QtCore, QtGui
from identification.frview import Ui_Dialog  # 假设这是你的Ui_Dialog类所在的模块
from identification.fruitIdentify import global_variable
class NutritionDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.view = global_variable  # 假设 global_variable 已经被正确设置

        # 创建一个模型
        self.model = QtGui.QStandardItemModel(len(self.view), 2)  # 假设有两列
        self.tableView.setModel(self.model)

        # 设置表头
        self.model.setHorizontalHeaderLabels(['Fruit/Vegetable', 'Nutrition'])

        # 设置第二列的宽度
        self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # 填充数据
        row = 0
        for fruit, description in self.view.items():
            self.model.setItem(row, 0, QtGui.QStandardItem(fruit))
            self.model.setItem(row, 1, QtGui.QStandardItem(description))
            row += 1

        self.pushButton.clicked.connect(self.go_back)

    def go_back(self):
        from identification.fruitIdentify import ImageUploader
        self.nextpage = ImageUploader()
        self.nextpage.show()
        self.close()


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     dialog = NutritionDialog()
#     dialog.show()
#     sys.exit(app.exec_())