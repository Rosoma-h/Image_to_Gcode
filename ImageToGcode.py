import copy
from PIL import Image
from math import ceil
import functions as f


def zagr_img(name_file):
    """Завантаження зображення."""
    return Image.open(name_file)


def pixelisation_image(image, scale):
    """Візуалізація розбивки картинки на більші фрагменти."""
    edited_image = copy.deepcopy(image)
    width = image.size[0]  # Визначаємо ширину картинки.
    height = image.size[1]  # Визначаємо висоту картинки.
    pix = image.load()
    # Перший прохід по циклу
    first_lap = True
    koords = []
    # обчислення розму "пікселя" пікселізації
    size_pixel = int(ceil(min(width, height) / scale))
    range_size = range(size_pixel)
    # print("Розмір пікселя: ", size_pixel)
    range_w = int(width / size_pixel)
    range_h = int(height / size_pixel)
    box_w = range_w * size_pixel
    box_h = range_h * size_pixel
    # поправки для розміщення рамки в середині картинки
    de_w = int((width - box_w) / 2)
    de_h = int((height - box_h) / 2)
    for h in range(range_h):
        for w in range(range_w):
            # координати позиції для обчислення середнього кольору пікселя
            w_p = w * size_pixel + de_w
            h_p = h * size_pixel + de_h
            # Обчислення середнього кольору пікеля
            for i in range_size:
                for j in range_size:
                    # print(pix[i, j])
                    R = pix[i + w_p, j + h_p][0]
                    G = pix[i + w_p, j + h_p][1]
                    B = pix[i + w_p, j + h_p][2]
                    S_depth = R + G + B
            # Реверс кольору: темніше - глибше, світліше - менша глибина.
            S_depth = 1 - round(S_depth / 765, 3)  # 765 = 3 * 255

            # Додавання координат і глибини до списку
            koords.append(f.pos_glub(w_p, h_p, size_pixel, S_depth))

            # Показ "пікселізації" зображення
            edited_image = f.ris_pixel(w_p, h_p, size_pixel, S_depth,
                                       edited_image, first_lap)
            if first_lap:
                first_lap = False

    return edited_image, size_pixel, koords


def save_g_to_file(name_file_G, Gcode):
    # Запис програми у файл
    f_gcode = open(name_file_G, "w")
    f_gcode.write(Gcode)
    f_gcode.close()

    return None
