from PyQt5 import QtWidgets, QtCore, QtGui
from identification.diview import Ui_Dialog  # 假设这是你的Ui_Dialog类所在的模块
from identification.dishesIdentify import global_variable

class NutritionDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.view = global_variable

        # 创建一个模型
        self.model = QtGui.QStandardItemModel(len(self.view), 2)  # 假设有两列
        self.tableView.setModel(self.model)

        # 设置表头
        self.model.setHorizontalHeaderLabels(['Dishes', 'price'])

        # 设置第一列和第二列的宽度
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # 填充数据
        row = 0
        for dish, price in self.view.items():
            self.model.setItem(row, 0, QtGui.QStandardItem(dish))
            self.model.setItem(row, 1, QtGui.QStandardItem(str(price)))
            row += 1

        # 计算第二列所有值的总和
        total_price = 0
        for row in range(self.model.rowCount()):
            price_item = self.model.item(row, 1)
            if price_item.text().isdigit():
                total_price += int(price_item.text())
            else:
                # 如果不希望跳过非整数类型的值，可以在这里处理
                pass

        # 添加一个新的列来显示总和
        self.model.setColumnCount(3)
        self.model.setHorizontalHeaderLabels(['Dishes', 'price', 'Total Price'])
        self.model.setItem(self.model.rowCount() - 1, 2, QtGui.QStandardItem(str(total_price)))

        self.pushButton.clicked.connect(self.go_back)

    def go_back(self):
        from identification.dishesIdentify import ImageUploader
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
