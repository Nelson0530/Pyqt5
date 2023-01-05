from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


class Center(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setWindowTitle('center')
        self.resize(250, 150)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    qb = Center()
    qb.show()
    sys.exit(app.exec_())
