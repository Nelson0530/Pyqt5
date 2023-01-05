from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont, QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit,
                             QLabel, QPushButton)
import sys, cv2, threading, mysql.connector, face_recognition
from datetime import datetime
import os
# from T_NewUserAndencode import User

class Dance3(QtWidgets.QWidget):  # 我們開發的視窗
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DancePage3')  # 視窗名
        self.resize(1920, 1000)  # 視窗大小
        self.DancePage3()
        self.EditName()
        # self.run()
        # self.SeeHere()

        self.VideoPlayer()


    def DancePage3(self):
        grview = QtWidgets.QGraphicsView(self)  # 加入 QGraphicsView
        grview.setGeometry(0, 0, 1920, 1000)    # 設定 QGraphicsView 位置與大小
        scene = QtWidgets.QGraphicsScene()      # 加入 QGraphicsScene
        scene.setSceneRect(810, 340, 300, 400)  # 設定 QGraphicsScene 位置與大小
        img = QtGui.QPixmap('Your Name.jpg')    # 加入圖片
        scene.addPixmap(img)                    # 將圖片加入 scene
        grview.setScene(scene)                  # 設定 QGraphicsView 的場景為 scene


    def VideoPlayer(self):
        grview = QtWidgets.QGraphicsView(self)  # 加入 QGraphicsView
        grview.setGeometry(507, 60, 500, 500)    # 設定 QGraphicsView 位置與大小
        scene = QtWidgets.QGraphicsScene()      # 加入 QGraphicsScene
        scene.setSceneRect(140, 10, 400, 480)  # 設定 QGraphicsScene 位置與大小
        # img = QtGui.QPixmap('./images/yaki.jpg')    # 加入圖片
        Temptimg = QtGui.QPixmap('./images/tempt.jpg')
        IsTemptimg = Temptimg.scaled(640, 500)
        scene.addPixmap(IsTemptimg)                    # 將圖片加入 scene
        grview.setScene(scene)                  # 設定 QGraphicsView 的場景為 scene


    def EditName(self):
        font = QFont()
        self.inputname = QtWidgets.QLineEdit(self)  # 建立單行輸入框
        self.inputname.setGeometry(1085, 139, 575, 109)  # 設定位置和尺寸
        font.setPointSize(40)  # 字型大小
        self.setFont(font)  # 将font应用到lineEdit
        self.setStyleSheet("background-color:rgba(255,255,255,0);border-width:0;border-style:outset;")  # 邊框無色與邊框、欄位透明

        self.enterbutton = QPushButton('', self)
        self.enterbutton.setGeometry(1659, 139, 205, 109)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)  # 按鈕透明度(透明0-1不透明)
        self.enterbutton.setGraphicsEffect(op)
        self.enterbutton.setAutoFillBackground(True)
        self.enterbutton.clicked.connect(self.SavetheName)

    def SavetheName(self):
        if self.inputname.text() != '':
            yourname = self.inputname.text()
            print(yourname)
            curImg = cv2.imread('./images/tempt.jpg')
            print(curImg)
            img = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)  # type which is ready to encoding
            EncodeofFace = list(face_recognition.face_encodings(img)[0])  # 單人encoding並放在list中
            print(EncodeofFace)
            cv2.imwrite(f'./images/{yourname}.jpg', curImg)
            curImg = []
            print(curImg)

            connection = mysql.connector.connect(host='localhost',
                                                 database='lets_dance',
                                                 user='dba',
                                                 password='dbaMySQL80')
            my_cursor = connection.cursor(prepared=True)
            try:
                insert_face = "INSERT INTO player(p_name,p_face,p_date) VALUES (%s,%s,%s)"
                data_list = (yourname, str(EncodeofFace), str(datetime.today()))
                my_cursor.executemany(insert_face, (data_list,))
                connection.commit()
            except Exception as err:
                print(err)
                connection.rollback()
            os.remove('./images/tempt.jpg')


    def SeeHere(self):
        self.label = QtWidgets.QLabel(self)  # 建立 QLabel
        self.label.setGeometry(507, 57, 500, 502)  # 設定 QLabel 大小和視窗相同

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera1")
            exit()
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Cannot receive frame")
                break
            frame = cv2.resize(frame, (500, 502))  # 改變尺寸和視窗相同
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 轉換成 RGB
            frame = cv2.flip(frame, 1)
            height, width, channel = frame.shape  # 讀取尺寸和 channel數量
            bytesPerline = channel * width  # 設定 bytesPerline ( 轉換使用 )
            # 轉換影像為 QImage，讓 PyQt5 可以讀取
            img = QImage(frame, width, height, bytesPerline, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(img))  # QLabel 顯示影像
        cap.release()
        cv2.destroyAllWindows()


    def run(self):
        self.vedio = threading.Thread(target=self.SeeHere)
        self.vedio.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 「系統」的視窗程式
    Form = Dance3()
    Form.show()

    sys.exit(app.exec_())