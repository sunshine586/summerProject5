import sys
from identification.identifyapp import IdentifyApp
if __name__ == '__main__':
    app = IdentifyApp()
    sys.exit(app.exec())
