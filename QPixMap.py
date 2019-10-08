import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        paint = QPixmap()
        pixmap = QPixmap("Capture.PNG")
        paint = drawPixmap(3, 3, pix)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(100, 100)
        self.setWindowTitle("Dom")
        self.show()


if __name__ == "__main__":


    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())