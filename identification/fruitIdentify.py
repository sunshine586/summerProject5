import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from identification.fruit import Ui_Dialog
import requests
import base64
import json
global_variable = {}
class ImageUploader(QMainWindow,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置界面布局和组件

        # Connect button clicks to methods
        self.pushButton_2.clicked.connect(self.upload_image)
        self.pushButton_3.clicked.connect(self.detect_fruit_vegetable)
        self.pushButton_4.clicked.connect(self.go_back)
        # Connect otherButton if needed
        self.uploaded_image_path = None

        # 字典用于存储水果及对应的营养价值信息
        self.fruit_vegetable = {
            # 蔬菜
            "苹果": "苹果有助于减肥，对皮肤好，还能预防便秘。",
            "香蕉": "香蕉能快速补充能量，对心脏好，还能帮助缓解压力。",
            "橙子": "橙子维C多，能增强免疫力，对预防感冒有帮助。",
            "草莓": "草莓含有很多抗衰老的东西，对眼睛和皮肤都好。",
            "葡萄": "葡萄含有丰富的抗氧化物质，对健康有益，但要注意糖分。",
            "樱桃": "樱桃含有丰富的抗炎成分，对缓解疼痛有一定的帮助。",
            "大樱桃": "樱桃含有丰富的抗炎成分，对缓解疼痛有一定的帮助。",
            "菠萝": "菠萝含有丰富的维生素C，对消化好，还能增强免疫力。",
            "芒果": "芒果维A和维C含量高，对皮肤和免疫系统都有好处。",
            "梨": "梨水分多，能帮助清热润肺，对嗓子好。",
            "蓝莓": "蓝莓对保护视力和提高记忆力有好处，是一种超级食品。",
            "红提":"红提富含抗氧化物质、维生素和矿物质，具有抗衰老、预防贫血、增强免疫力等多种健康功效。",

            # 蔬菜
            "胡萝卜": "胡萝卜富含维A，对视力和皮肤都好，还能增强免疫力。",
            "西红柿": "西红柿含有丰富的番茄红素，对心脏健康和防癌有好处。",
            "菠菜": "菠菜含铁质和钙质，对骨骼和血液健康非常重要。",
            "西兰花": "西兰花是抗癌明星，含有丰富的维生素C和纤维。",
            "黄瓜": "黄瓜水分高，有助于清热解毒，对皮肤好。",
            "土豆": "土豆是良好的碳水化合物来源，对能量代谢和消化有好处。",
            "洋葱": "洋葱含有抗氧化物质，能增强免疫力，对心血管健康有益。",
            "南瓜": "南瓜含有丰富的β-胡萝卜素，对视力和皮肤健康有好处。",
            "甜椒": "甜椒维C含量高，有助于提高免疫力，对皮肤好。",
            "蘑菇": "蘑菇含有丰富的矿物质和抗氧化物质，对健康有益。"
        }

        self.rf_detal = {}

    def upload_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image files (*.jpg)")
        if filename:
            self.uploaded_image_path = filename
            pixmap = QPixmap(filename)
            self.label_2.setPixmap(
                pixmap.scaled(self.label_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.label_2.setText("")
            self.label_2.setStyleSheet("")

    def detect_fruit_vegetable(self, **fr_new):
        if self.uploaded_image_path:
            request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient"

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
                        max_score_item = max(results, key=lambda x: x['score'])
                        name = max_score_item['name']
                        # 在字典中查询营养价值信息
                        nutritional_value = self.fruit_vegetable.get(name, "未提供营养价值信息。")
                        # 添加到add_price字典中
                        self.rf_detal[name] = nutritional_value
                        global_variable[name] = nutritional_value
                        # 弹出提示框显示得分最高的对象的名称和营养价值信息
                        QMessageBox.information(self, "检测结果显示",
                                                f"检测到的果蔬是: {name}\n营养价值信息: {nutritional_value}")
                    else:
                        QMessageBox.information(self, "检测结果显示", "未检测到任何果蔬。")
                except json.JSONDecodeError:
                    QMessageBox.critical(self, "错误", "解析响应JSON失败。")
            else:
                QMessageBox.critical(self, "错误", f"对象检测失败。状态码: {response.status_code}")


    def go_back(self):
        from identification.frmodelframe import frmodelWindow
        self.nextpage = frmodelWindow()
        self.nextpage.show()
        self.close()


#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ImageUploader()
#     window.show()
#     sys.exit(app.exec_())
