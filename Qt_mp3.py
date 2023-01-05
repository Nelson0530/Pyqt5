from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtMultimedia
import sys

# 播放mp3------------------------------------------------------------------
app = QtWidgets.QApplication(sys.argv)
path = './mp3/105_song.mp3'                # 音乐文件路径
url = QtCore.QUrl.fromLocalFile(path)
# 👆支持音乐url或本地地址
# 注：url 路径无法使用双引号的url地址，单引号可以（不要问我为什么，我也想知道）
# 如果你有双引号的url地址，建议这么写 path = path[1:-1]

content = QtMultimedia.QMediaContent(url)  # 加载音乐
player = QtMultimedia.QMediaPlayer()       # 创建 QMediaPlayer控件
player.setMedia(content)                   # 关联 QMediaPlayer控件与音乐地址
# player.setVolume(80)                       # 设置播放音量 0~100
player.play()                              # 播放

sys.exit(app.exec())
