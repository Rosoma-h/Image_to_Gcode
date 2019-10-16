import copy
from PIL import Image
from math import ceil
import functions as f
from settings import Settings

s = Settings()


def zagr_img(name_file):
    """Завантаження зображення."""
    return Image.open(name_file)


# def size_pixel_f(width, height, scale):
#     """Визначення розміру пікселя."""
#     # width = image.size[0]  # Определяем ширину.
#     # height = image.size[1]  # Определяем висоту.
#     size_pixel = int(ceil(min(width, height) / scale))

#     return size_pixel


def pixelisation_image(image, scale):
    """Візуалізація розбивки картинки на більші фрагменти."""
    edited_image = copy.deepcopy(image)
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем висоту.
    pix = image.load()
    # Первый проход
    first_lap = True
    koords = []
    # обчислення розму "пікселя" пікселізації
    size_pixel = int(ceil(min(width, height) / scale))
    range_size = range(size_pixel)
    # print("Розмір пікселя: ", size_pixel)
    range_h = int(height / size_pixel)
    range_w = int(width / size_pixel)
    box_h = range_h * size_pixel
    box_w = range_w * size_pixel
    # поправки для розміщення рамки в середині картинки
    de_w = int((width - box_w) / 2)
    de_h = int((height - box_h) / 2)
    for h in range(range_h):
        for w in range(range_w):
            # координати позиції для обчислення середнього кольору пікселя
            h_p = h * size_pixel + de_h
            w_p = w * size_pixel + de_w
            # Обчислення середнього кольору пікеля
            for i in range_size:
                for j in range_size:
                    # print(pix[i, j])
                    R = pix[i + w_p, j + h_p][0]
                    G = pix[i + w_p, j + h_p][1]
                    B = pix[i + w_p, j + h_p][2]
                    S = R + G + B
            S = int(S / 3)

            # Додавання координат і глибини до списку
            koords.append(f.pos_glub(h_p, w_p, size_pixel, S,
                                     s.max_Z, s.koef))

            # Імітація "пікселізації" зображення
            edited_image = f.ris_pixel(h_p, w_p, size_pixel, S, edited_image,
                                       first_lap)
            if first_lap:
                first_lap = False

    print('ok')
    return edited_image, size_pixel, koords


def save_g_to_file(name_file_G, Gcode):
    # Запис програми у файл
    f_gcode = open(name_file_G, "w")
    f_gcode.write(Gcode)
    f_gcode.close()

    return None


# def i_to_g(koords, name_file, name_file_G="GcFI.tap"):
#     # Створення і запис програми для станка у файл
#     GcodeBody = f.Gcode_Body(koords, s.z_safe, s.feed_z, s.max_Z, s.filtr_z)
#     f_gcode = open(r"Gcodes\\"[:-1] + name_file.split(".")[0] + "_" +
#                    name_file_G, "w")
#     f_gcode.write(f.head_end()[0] + GcodeBody + f.head_end()[1])
#     f_gcode.close()

#     print("Готово!")

#     return None
