import sys
import copy
from os import getcwd
from PyQt5.QtWidgets import QApplication
# from PyQt5 import QtCore
# from PyQt5.QtGui import QPixmap
# from PIL import ImageQt

from settings import Settings
from interface import TitleWindow
from ImageToGcode import zagr_img, pixelisation_image, save_g_to_file
from functions import (calculate_gcode, convert_pil_image_to_QtPixmap,
                       check_input_values, path_info_text, path_lenght)


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
Gcode = '# Epty file'
opening_directory = ''
saving_directory = ''

mess = 'Завантажте зображення.'
ui.statusBar().showMessage(mess)


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
        opening_directory = file_name[:file_name.rfind('/') + 1]
        mess = ('Зображення завантажене. ' +
                'Напишіть величину кратності та "пікселізуйте" зображення.'
                )
        ui.statusBar().showMessage(mess)
    except:
        print('Не удалось открыть файл!')
        mess = 'Не вдалося відкрити файл!'
        ui.statusBar().showMessage(mess)

    if Kartinka:

        origin_pixmap = convert_pil_image_to_QtPixmap(Kartinka)
        ui.origin_image.setPixmap(origin_pixmap)

        width = Kartinka.size[0]  # Определяем ширину.
        height = Kartinka.size[1]  # Определяем висоту.
        shablon = 'Розмір зображення: '
        ui.info_picture.setText(shablon + str(width) +
                                ' на ' + str(height) + ' пікселів.')


def pikselizacia_kartinki():

    global Kartinka
    global koords

    local_img = copy.deepcopy(Kartinka)
    text = ui.scale_input.text()

    if local_img:

        if not(text and text != '0'):

            size_start = str(int(min(local_img.size[0],
                                     local_img.size[1]) / 10))
            ui.scale_input.setText(size_start)

        scale = int(float(ui.scale_input.text()))
        edited_img, size_pixel, koords = pixelisation_image(local_img,
                                                            scale)
        ui.size_pixel_out.setText(str(size_pixel))
        edited_pixmap = convert_pil_image_to_QtPixmap(edited_img)
        ui.edited_image.setPixmap(edited_pixmap)

        mess = ('Зображення "пікселізоване".')
        ui.statusBar().showMessage(mess)

        # активація кнопки розрахунку траєкторії
        ui.calculate_path.setDisabled(False)


def calculate_path_gcode():
    """Генерація файлу з Gcode."""
    global koords
    global Gcode

    # Очистка даних
    Gcode = ''

    work_parameters = check_input_values(ui, def_set, Kartinka)
    work_parameters.append(koords)
    work_parameters.append(Kartinka.size)
    # print('Гынырацыя Гы кода')
    ui.statusBar().showMessage('Генерація G-коду....')
    try:
        Gcode = calculate_gcode(*work_parameters)
        ui.path_info.setText(path_info_text(*path_lenght(Gcode)))
        ui.statusBar().showMessage('G-код згенерований успішно!')
        # print('Код згынырырован')
    except:
        mess = ('Не вдалося згенерувати G-код. ' +
                'Перевірте чи завантажене зображення "пікселізоване"')
        ui.statusBar().showMessage(mess)

    # активація кнопки збереження траєкторії
    ui.save_doc.setDisabled(False)


def save_g_code():
    """Збереження G коду у файл."""
    global Gcode
    global saving_directory
    if saving_directory:
        loc = saving_directory
    else:
        loc = getcwd()

    file_name = ui.show_save_Dialog(loc)

    try:
        save_g_to_file(file_name, Gcode)
        # Фіксація положення останнього збереженого файлу
        saving_directory = file_name[:file_name.rfind('/') + 1]
        mess = 'Файл ' + file_name + ' збережено.'
        ui.statusBar().showMessage(mess)

    except:
        print('Не удалось сохранить файл!')


# Events


ui.openFile.triggered.connect(zagruzka_kartinki)
ui.zagruzka.clicked.connect(zagruzka_kartinki)
ui.pixelization.clicked.connect(pikselizacia_kartinki)
ui.calculate_path.clicked.connect(calculate_path_gcode)
ui.save_doc.clicked.connect(save_g_code)


# Run main loop
sys.exit(app.exec_())
