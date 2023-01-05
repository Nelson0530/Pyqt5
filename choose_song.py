import sys, cv2, mysql.connector
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel)
from PyQt5.QtGui import QImage, QPixmap, QFont

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello')
        self.resize(1920, 980)
        self.ui()
        self.photo()

    def ui(self):
        self.view = QtWidgets.QGraphicsView(self)
        self.view.setGeometry(0, 0, 1920, 980)
        scene = QtWidgets.QGraphicsScene()
        image = QPixmap("./UIimages/UI_5.jpg")
        image = image.scaled(1915, 970)
        scene.setSceneRect(0, 0, 1915, 970)
        scene.addPixmap(image)
        self.view.setScene(scene)

    def photo(self):
        connection = mysql.connector.connect(host='localhost',
                                             database='lets_dance',
                                             user='root',
                                             password='ab0930769971')
        my_cursor = connection.cursor(prepared=True)
        try:
            select_score = "SELECT POINT FROM history order by POINT desc limit 3"
            my_cursor.execute(select_score)
            result = my_cursor.fetchall()
            print(result)
            a = str(result[0][0])
            b = str(result[1][0])
            c = str(result[2][0])
            print(a)
        except Exception as err:
            print(err)
            connection.rollback()

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(1470, 360, 180, 70)
        self.label.setAlignment(QtCore.Qt.AlignRight)  # 對齊方式(向右)
        self.label.setStyleSheet("color:white")
        self.label.setFont(QFont("Verdana", 30))
        self.label.setText(a)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(1530, 440, 180, 70)
        self.label2.setAlignment(QtCore.Qt.AlignRight)  # 對齊方式(向右)
        self.label2.setStyleSheet("color:white")
        self.label2.setFont(QFont("Verdana", 30))
        self.label2.setText(b)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(1610, 520, 180, 70)
        self.label3.setAlignment(QtCore.Qt.AlignRight)  # 對齊方式(向右)
        self.label3.setStyleSheet("color:white")
        self.label3.setFont(QFont("Verdana", 30))
        self.label3.setText(c)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setGeometry(150, 540, 700, 80)
        self.label5.setStyleSheet("color:white")
        self.label5.setFont(QFont("Verdana", 30))
        self.label5.setText("Chiki-chiki Bam-bam")

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setGeometry(720, 10, 550, 550)
        photo = QImage("./UIimages/ciki.jpg")  # , 950, 970, (950 * 3), QImage.Format_RGB888)
        self.label4.setPixmap(QPixmap.fromImage(photo))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.showMaximized()
    sys.exit(app.exec_())
