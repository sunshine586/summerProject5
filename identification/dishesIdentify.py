import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from identification.dishes import Ui_Dialog
import requests
import base64
import json
global_variable = {}
class ImageUploader(QMainWindow,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置界面布局和组件

        self.pushButton_2.clicked.connect(self.upload_image)
        self.pushButton_3.clicked.connect(self.detect_dish)
        self.pushButton_4.clicked.connect(self.go_back1)

        self.uploaded_image_path = None

        # 字典用于存储菜品名称及对应的价格信息
        self.dishes_price = {
            "宫保鸡丁": 32,
            "鱼香肉丝": 28,
            "麻婆豆腐": 22,
            "红烧肉": 38,
            "清蒸鱼": 48,
            "糖醋里脊": 30,
            "水煮牛肉": 42,
            "回锅肉": 36,
            "辣子鸡": 28,
            "京酱肉丝": 26,
            "土豆丝": 16,
            "地三鲜": 24,
            "蚝油生菜": 18,
            "手撕包菜": 20,
            "干煸豆角": 22,
            "蒜蓉西兰花": 20,
            "清炒时蔬": 18,
            "扬州炒饭": 25,
            "蛋炒饭": 20,
            "牛肉拉面": 30,
            "酸辣粉": 15,
            "猪蹄": 58
        }
        # 字典用于存储菜品名称及对应的价格信息
        self.add_price = {

        }

    def upload_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image files (*.jpg)")
        if filename:
            self.uploaded_image_path = filename
            pixmap = QPixmap(filename)
            self.label_2.setPixmap(
                pixmap.scaled(self.label_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.label_2.setText("")
            self.label_2.setStyleSheet("")

    def detect_dish(self):
        if self.uploaded_image_path:
            request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"

            # 二进制方式打开图片文件
            with open(self.uploaded_image_path, 'rb') as f:
                img = base64.b64encode(f.read())

            params = {"image": img}
            access_token = '24.55b6297c488e82c38223d1fbb2f627b7.2592000.1722479161.282335-89935683'
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}

            response = requests.post(request_url, data=params, headers=headers)

            if response.status_code == 200:
                try:
                    data = response.json()
                    results = data.get('result', [])

                    if results:
                        # 获取得分最高的对象
                        max_score_item = max(results, key=lambda x: x['probability'])
                        name = max_score_item['name']
                        # 在字典中查询价格信息
                        price = self.dishes_price.get(name, "未提供价格信息。")
                        # 添加到add_price字典中
                        self.add_price[name] = price
                        global_variable[name] = price
                        # 弹出提示框显示得分最高的对象的名称和价格信息
                        QMessageBox.information(self, "检测结果显示", f"检测到的菜品是: {name}\n价格信息: {price}元")
                    else:
                        QMessageBox.information(self, "检测结果显示", "未检测到任何菜品。")

                except json.JSONDecodeError:
                    QMessageBox.critical(self, "错误", "解析响应JSON失败。")

            else:
                QMessageBox.critical(self, "错误", f"对象检测失败。状态码: {response.status_code}")

    def go_back1(self):
        print("Button 4 clicked. Function 4 executed.")
        from identification.dimodelframe import dimodelWindow
        self.nextpage1 = dimodelWindow()
        self.nextpage1.show()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ImageUploader()
#     window.show()
#     sys.exit(app.exec_())
