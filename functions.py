from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PIL import ImageQt
from PIL import ImageDraw


def ris_pixel(weigth_point, height_point,
              size_pixel, S, image, first_lap):
    """Функція для заповнення квадратної області круглими пікселями"""
    # коло, в залежності (від величини S (від 0,0 до 1))

    # Очистка заднього фону
    draw = ImageDraw.Draw(image)
    if first_lap:
        width = image.size[0]  # Визначаємо ширину картинки.
        height = image.size[1]  # Визначаємо висоту картинки.
        draw.rectangle((0, 0, width, height), (255, 255, 255))

    # Малювання кола в позиціі пікселя чорним кольором (0, 0, 0)
    # і розміром S(величина от 0 до 1) від розміру пікселя
    # Діаметр кола
    size_circ = size_pixel * S

    offset_pos = int((size_pixel - size_circ) / 2)
    pos_h_circ_0 = height_point + offset_pos
    pos_w_circ_0 = weigth_point + offset_pos
    pos_h_circ_1 = height_point + offset_pos + size_circ
    pos_w_circ_1 = weigth_point + offset_pos + size_circ

    if size_circ != 0:
        draw.ellipse((pos_w_circ_0, pos_h_circ_0,
                      pos_w_circ_1, pos_h_circ_1,
                      ), (0, 0, 0))

    return image


def pos_glub(wigth_p, height_p, size_pixel, S_depth):
    """Функція для визначення позиції і глибини точки на заготовці"""

    # Визначення позиції точки на площині XY в пікселях
    half_pixel = size_pixel / 2
    X = wigth_p + half_pixel
    Y = height_p + half_pixel
    # Визначення глибини опускання фрези від 0 до 1
    Z = S_depth

    return X, Y, Z


def head_end():
    """Функція повертає початок і закінчення файлу з G-кодом
    для програми NC Studio."""

    GcodeHead = '''M3
G0Z50.000
G0X0.000Y0.000S18000 \n'''
    GcodeEnd = '''G0Z50.000
G0X0.000Y0.000
G0Z50.000
G0X0Y0
M30'''

    return GcodeHead, GcodeEnd


def calculate_gcode(Width_size, Height_size, koords, feed_z, z_safe,
                    depth_Z, filtr_z):
    """Функція створює управляючу програму для станка
        на основі списку координат"""
    # if V_size and H_size:

    #     print("Rozmir zagotovki zadano")
    # else:
    #     print("Vidsutnya zagotovka")
    head_gcode, end_gcode = head_end()
    body_gcode = ""
    for tochka in koords:
        # 0 = білий колір, мінімальна глибина;
        # 1 = чорний колір, максимальна глибина
        tochka_Z = round(- depth_Z * tochka[2], 2)
        # Додавання координати з глибиною більшою за filtr_z
        if abs(tochka_Z) >= filtr_z:
            body_gcode += ("G0" + "X" + str(tochka[0]) +
                           "Y" + str(tochka[1]) +
                           "Z" + str(z_safe) + "\n"
                           )
            body_gcode += ("G1" + "Z" + str(tochka_Z) + "F" +
                           str(feed_z) + "\n" +
                           "G0" + "Z" + str(z_safe) + "\n"
                           )

    Gcode = head_gcode + body_gcode + end_gcode

    return Gcode


def convert_pil_image_to_QtPixmap(image):
    """ """
    image_data = ImageQt.ImageQt(image)
    image_pixmap = QPixmap.fromImage(image_data)
    image_pixmap = image_pixmap.scaled(QtCore.QSize(500, 500), 1, 1)

    return image_pixmap


def check(par_def, par_inp):
    try:
        if par_inp.text():
            return par_inp.text()
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

    return work_parameters