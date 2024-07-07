# 导入生成的Python文件
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from identification.enterframe import EnterFrame
from identification.first import Ui_Dialog  # Replace with your actual UI file import
from PyQt5.QtWidgets import QDialog

# 创建主窗口类
class FirstWindow(QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 连接按钮点击事件
        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.login)

        # 字典用于存储用户名和密码
        self.users = {}

    # 注册
    def register(self):
        username = self.textEdit.toPlainText().strip()  # 获取用户名
        password = self.textEdit_2.toPlainText().strip()  # 获取密码

        if username and password:
            if username not in self.users:
                self.users[username] = password
                QMessageBox.information(self, '注册', f"已注册用户：{username},请返回登录！")
                # 清除用户名和密码
                self.textEdit.setText("")
                self.textEdit_2.setText("")

            else:
                QMessageBox.warning(self, '注册', f"用户名 '{username}' 已存在，请返回重新注册！")
        else:
            QMessageBox.warning(self, '注册', "请输入用户名和密码！")

    # 登录
    def login(self):
        username = self.textEdit.toPlainText().strip()  # 获取用户名
        password = self.textEdit_2.toPlainText().strip()  # 获取密码

        if username and password:
            # 登录成功
            if username in self.users and self.users[username] == password:
                QMessageBox.information(self, '登录', f"已登录用户 '{username}'.")

                # 跳转到下一个页面
                self.nextframe = EnterFrame()
                self.nextframe.show()
                self.close()

            else:
                QMessageBox.warning(self, '登录', "用户名或密码无效.")
        else:
            QMessageBox.warning(self, '登录', "请输入用户名和密码.")

    # def goin(self):
    #     self.nextframe = EnterFrame()  # 跳转到下一页
    #     self.nextframe.show()
    #     self.close()

#
# if __name__ == "__main__":
#     import sys
#
#     app = QApplication(sys.argv)
#     nextPage = EnterFrame()
#     nextPage.show()
#     sys.exit(app.exec_())
