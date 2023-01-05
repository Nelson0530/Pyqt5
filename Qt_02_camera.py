from PyQt5 import QtWidgets, QtCore, QtMultimedia
from PyQt5.QtGui import QImage, QPixmap
import sys, cv2, threading

app = QtWidgets.QApplication(sys.argv)
window_w, window_h = 1240, 640
path = './mp3/105_song.mp3'                # 音乐文件路径
url = QtCore.QUrl.fromLocalFile(path)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(window_w, window_h)

# def windowResize(self):
#     global window_w, window_h
#     window_w = Form.width()
#     window_h = Form.height()
#     label.setGeometry(0,0,window_w,window_h)
# Form.resizeEvent = windowResize

ocv = True                     # 一開始設定為 True
def closeOpenCV(self):
    global ocv
    ocv = False                # 關閉視窗時設定為 False
Form.closeEvent = closeOpenCV  # 關閉視窗事件發生時，執行 closeOpenCV 函式

label = QtWidgets.QLabel(Form)
label.setGeometry(0, 0, 640, window_h)

label2 = QtWidgets.QLabel(Form)
label2.setGeometry(640, 0, 600, window_h)

def opencv():
    global window_w, window_h, ocv
    cap = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture("./mp4/105_song.mp4")
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    else:
        content = QtMultimedia.QMediaContent(url)          # 加载音乐
        player = QtMultimedia.QMediaPlayer()               # 创建 QMediaPlayer控件
        player.setMedia(content)                        # 关联 QMediaPlayer控件与音乐地址
        player.play()
    # while 迴圈改為 ocv
    while ocv:
        ret, frame = cap.read()
        ret2, video = cap2.read()
        if not ret and ret2:
            print("Cannot receive frame")
            break
        frame = cv2.resize(frame, (640, window_h))
        video = cv2.resize(video, (600, window_h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        cv2.putText(frame, "hello", (500, 60), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0, 255), 4)
        # height, width, channel = frame.shape
        # h2, w2, c2 = video.shape
        # bytesPerline = channel * width
        img = QImage(frame, 640, window_h, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(img))
        img2 = QImage(video, 600, window_h, QImage.Format_RGB888)
        label2.setPixmap(QPixmap.fromImage(img2))


if __name__ == '__main__':
    video = threading.Thread(target=opencv)
    video.start()

    Form.show()
    sys.exit(app.exec_())
