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

    # Очистка даних
    Gcode = ""
    # Задание настроек по умолчанию
    V_size = def_set.V_size
    H_size = def_set.V_size
    feed_z = def_set.feed_z
    z_safe = def_set.z_safe
    depth_Z = def_set.depth_Z
    filtr_z = def_set.filtr_z

    default_parameters = [V_size, H_size, koords, feed_z,
                          z_safe, depth_Z, filtr_z]
    work_parameters = check_input_values(default_parameters)
    print("Гынырацыя Гы кода")
    try:
        Gcode = calculate_gcode(*work_parameters)
        print("Код згынырырован")
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

    try:
        save_g_to_file(file_name, Gcode)
        # Фіксація положення останнього збереженого файлу
        saving_directory = file_name[:file_name.rfind("/") + 1]

    except:
        print('Не удалось сохранить файл!')


def check_input_values(default_parameters):
    """ Проверка наличия парраметров в полях ввода, при наличии
        конвертация строкового формата в числовой."""

    global Kartinka
    global koords
    input_fields = (ui.Vertic_size_input,
                    ui.Horiz_size_input,
                    koords,
                    ui.feed_z_input,
                    ui.z_safe_input,
                    ui.depth_Z_input,
                    ui.filtr_z_input
                    )

    V_size = ui.Vertic_size_input.text()
    H_size = ui.Horiz_size_input.text()

    if (
        Kartinka
            and (not(V_size) or V_size == "0")
            and (not(H_size) or H_size == "0")
        ):

        ui.Vertic_size_input.setText(str(Kartinka.size[0]))
        ui.Horiz_size_input.setText(str(Kartinka.size[1]))

    def check(par_def, par_inp):
        try:
            if par_inp.text():
                return par_inp
            else:
                par_inp.setText(str(par_def))
                return par_def
        except:
            return par_def

    def convert_to_digit(d):

        if isinstance(d, str):
            try:
                return int(d)
            except:
                try:
                    return float(d)
                except:
                    pass
        else:
            return d


    params = map(check, default_parameters, input_fields)
    work_parameters = [convert_to_digit(x) for x in params]

    return work_parameters


# Events


ui.openFile.triggered.connect(zagruzka_kartinki)
ui.zagruzka.clicked.connect(zagruzka_kartinki)
ui.prosmotr.clicked.connect(prosmotr_kartinki)
ui.calculate_path.clicked.connect(calculate_path_gcode)
ui.save_doc.clicked.connect(save_g_code)


# Run main loop
sys.exit(app.exec_())
