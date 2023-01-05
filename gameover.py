import threading
import time
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel)
from PyQt5.QtGui import QImage, QPixmap, QFont


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello')
        self.resize(1920, 980)
        self.setStyleSheet('background:black;')
        self.ui()
        self.run()

    def text(self):
        a = "     GAME OVER !  See you again !     "
        count = 0
        while count < 40:
            # os.system("cls")
            self.label.setText(a)
            time.sleep(0.25)
            self.label.clear()
            a = a[1:] + a[0]
            count += 1

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(550, 420, 750, 80)
        # self.label.setAlignment(QtCore.Qt.AlignRight)  # 對齊方式(向右)
        self.label.setStyleSheet("color:red")
        self.label.setFont(QFont("Verdana", 40))
        # self.label.setText(self.text())

    def run(self):
        thread = threading.Thread(target=self.text)
        thread.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.showMaximized()
    sys.exit(app.exec_())
