import sys
import copy
from os import getcwd
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PIL import ImageQt

from interface import TitleWindow
from ImageToGcode import zagr_img, pixelisation_image, save_g_to_file
from functions import calculate_gcode
from settings import Settings

def_set = Settings()

# Create aplication
app = QApplication(sys.argv)

# Create form and init UI
ui = TitleWindow()

# Body
# Define name Kartinka for downloaded image
global Kartinka
global koords
global Gcode
global opening_directory
global saving_directory
Kartinka = None
koords = None
Gcode = "# Epty file"
opening_directory = ""
saving_directory = ""


def zagruzka_kartinki():

    global Kartinka
    global opening_directory

    if opening_directory:
        loc = opening_directory
    else:
        loc = getcwd()
    file_name = ui.show_open_Dialog(loc)

    try:
        Kartinka = zagr_img(file_name)
        # Фіксація положення останнього відкритого файлу
        opening_directory = file_name[:file_name.rfind("/") + 1]
    except:
        print('Не удалось открыть файл!')

    if Kartinka:
        print(Kartinka)
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
    global koords

    local_img = copy.deepcopy(Kartinka)

    text = ui.scale_input.text()

    if local_img:
        print("Shtukis")

        if text and text != '0':

            scale = int(float(ui.scale_input.text()))

            edited_img, size_pixel, koords = pixelisation_image(local_img,
                                                                scale)

            ui.size_pixel_out.setText(str(size_pixel))
            edited_data = ImageQt.ImageQt(edited_img)
            edited_pixmap = QPixmap.fromImage(edited_data)
            edited_pixmap = edited_pixmap.scaled(QtCore.QSize(500, 500), 1, 1)

            ui.edited_image.setPixmap(edited_pixmap)

        else:

            size_start = str(int(min(local_img.size[0],
                                     local_img.size[1]) / 10)
                             )
            ui.scale_input.setText(size_start)


def calculate_path_gcode():
    # Генерация файла с Gcode
    global koords
    global Gcode

    print("Гынырацыя Гы кода")
    # Очистка даних
    Gcode = ""
    # Задание настроек по умолчанию
    z_safe = def_set.z_safe
    feed_z = def_set.feed_z
    max_Z = def_set.max_Z
    filtr_z = def_set.filtr_z

    try:
        Gcode = calculate_gcode(koords, z_safe, feed_z, max_Z, filtr_z)
    except:
        print('Не удалось рассчитать траеторию')



def save_g_code():

    global Gcode
    global saving_directory
    if saving_directory:
        loc = saving_directory
    else:
        loc = getcwd()

    file_name = ui.show_save_Dialog(loc)
    print(file_name)

    try:
        save_g_to_file(file_name, Gcode)
        # Фіксація положення останнього збереженого файлу
        saving_directory = file_name[:file_name.rfind("/") + 1]

    except:
        print('Не удалось сохранить файл!')


# Events


ui.openFile.triggered.connect(zagruzka_kartinki)
ui.zagruzka.clicked.connect(zagruzka_kartinki)
ui.prosmotr.clicked.connect(prosmotr_kartinki)
ui.calculate_path.clicked.connect(calculate_path_gcode)
ui.save_doc.clicked.connect(save_g_code)


# Run main loop
sys.exit(app.exec_())
