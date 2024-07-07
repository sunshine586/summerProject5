from PyQt5.QtWidgets import QApplication
from identification.firstframe import FirstWindow
import sys

class IdentifyApp(QApplication):
    def __init__(self):
        super(IdentifyApp, self).__init__(sys.argv)
        self.dialog = FirstWindow()
        self.dialog.show()
