import sys
from os import getcwd
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from interface import TitleWindow
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

    loc = getcwd()
    file_name = ui.showDialog(loc)

    global Kartinka
    try:
        Kartinka = zagr_img(file_name)
    except:
        print('Не удалось открыть файл!')


    width = Kartinka.size[0]  # Определяем ширину.
    height = Kartinka.size[1]  # Определяем висоту.

    origin_data = ImageQt.ImageQt(Kartinka)
    origin_pixmap = QPixmap.fromImage(origin_data)
    origin_pixmap = origin_pixmap.scaled(QtCore.QSize(500, 500), 1, 1)

    ui.origin_image.setPixmap(origin_pixmap)

    shablon = "Розмір зображення: "
    ui.info_picture.setText(shablon + str(width) +
                            " на " + str(height) + " пікселів.")


def prosmotr_kartinki():

    global Kartinka

    text = ui.scale_input.text()
    if Kartinka:
        print("Shtukis")
        ui.size_pixel_out.setText(str(34))
        # if text and text != '0':

        #     print(Kartinka)

        #     scale = int(float(ui.scale_input.text()))
        #     edited_img, size_pixel, koord = pixelisation_image(Kartinka, scale)

        #     ui.size_pixel_out = str(size_pixel)
        #     print(edited_img)
        #     # Тут має бути код, який змінює картинку
        #     ui.size_pixel_out.setText(str(size_pixel)
        #     # edited_data = ImageQt.ImageQt(edited_img)
        #     # edited_pixmap = QPixmap.fromImage(edited_data)

        #     # ui.edited_image.setPixmap(edited_pixmap)

        # else:

        #     size_start = str(min(Kartinka.size[0], Kartinka.size[1]))
        #     ui.scale_input.setText(size_start)



# Events


ui.zagruzka.clicked.connect(zagruzka_kartinki)
ui.prosmotr.clicked.connect(prosmotr_kartinki)

# Run main loop
sys.exit(app.exec_())
