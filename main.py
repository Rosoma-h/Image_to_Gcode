import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from QFileDialog import TitleWindow
from PyQt5.QtGui import QPixmap
from PIL import ImageQt

from ImageToGcode import zagr_img, pixelisation_image



# import sys
# from PyQt5 import QtWidgets
# from PyQt5 import QtCore
# from PyQt5.QtGui import QPixmap
# from PIL import ImageQt

# from interface import Ui_MainWindow
# from ImageToGcode import zagr_img, pixelisation_image


# Create aplication
app = QApplication(sys.argv)

# Create form and init UI
ui = TitleWindow()

# Body
# Define name Kartinka for downloaded image
global Kartinka
Kartinka = None


def zagruzka_kartinki():

    file_name = ui.showDialog()
    print(file_name)

    global Kartinka
    try:
        Kartinka = zagr_img(file_name)
    except:
        print('Hrin')


    width = Kartinka.size[0]  # Определяем ширину.
    height = Kartinka.size[1]  # Определяем висоту.
    print(width, height)
    origin_data = ImageQt.ImageQt(Kartinka)
    origin_pixmap = QPixmap.fromImage(origin_data)
    origin_pixmap = origin_pixmap.scaled(QtCore.QSize(500, 500), 1, 1)

    ui.origin_image.setPixmap(origin_pixmap)

    shablon = "Розмір зображення: "
    ui.info_picture.setText(shablon + str(width) +
                            " на " + str(height) + " пікселів.")


def prosmotr_kartinki():
    pass
    # text = ui.lineEdit_1.text()
    # if text and text != '0':
    #     pass
    # else:
    #     ui.lineEdit_1.setText('1')

    # if Kartinka:
    #     print(Kartinka)

    #     scale = int(float(ui.lineEdit_1.text()))
    #     edited_img = pixelisation_image(Kartinka, "acvalang.jpg", scale)[0]
    #     print(edited_img)
    #     # Тут має бути код, який змінює картинку

    #     edited_data = ImageQt.ImageQt(Kartinka)
    #     edited_pixmap = QPixmap.fromImage(edited_data)
    #     edited_pixmap = edited_pixmap.scaled(QtCore.QSize(500, 500), 1, 1)

    #     ui.edited_image.setPixmap(edited_pixmap)

# Events


ui.zagruzka.clicked.connect(zagruzka_kartinki)
ui.prosmotr.clicked.connect(prosmotr_kartinki)

# Run main loop
sys.exit(app.exec_())
