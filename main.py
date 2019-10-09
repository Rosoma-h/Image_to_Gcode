import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PIL import ImageQt

from interface import Ui_MainWindow
from ImageToGcode import zagr_img
# Create aplication

app = QtWidgets.QApplication(sys.argv)


# Create form and init UI

Form = QtWidgets.QWidget()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()

# Logi

# ui.lineEdit_1.setText("333")
# ui.lineEdit_1.clear()

# Define name Kartinka for downloaded image
global Kartinka
Kartinka = None


def zagruzka_kartinki():
    text = ui.lineEdit_1.text()
    if text:
        shablon = "Розмір зображення: "
        global Kartinka

        Kartinka = zagr_img("acvalang.jpg")

        width = Kartinka.size[0]  # Определяем ширину.
        height = Kartinka.size[1]  # Определяем висоту.

        origin_data = ImageQt.ImageQt(Kartinka)
        origin_pixmap = QPixmap.fromImage(origin_data)
        origin_pixmap = origin_pixmap.scaled(QtCore.QSize(500, 500), 1, 1)

        ui.origin_image.setPixmap(origin_pixmap)

        ui.label.setText(shablon + str(width) +
                         " на " + str(height) + " пікселів.")
    else:
        ui.lineEdit_1.setText('1')


def prosmotr_kartinki():

    if Kartinka:
        print(Kartinka)


ui.zagruzka.clicked.connect(zagruzka_kartinki)
ui.prosmotr.clicked.connect(prosmotr_kartinki)
# Run main loop

sys.exit(app.exec_())
