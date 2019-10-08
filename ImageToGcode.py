from PIL import Image, ImageDraw
from math import ceil
import functions as f
from settings import Settings

s = Settings()


class ZagrImg():
    """Завантажене зображення"""

    def __init__(self, name_file):
        """Ініціалізація зображення."""
        self.name_file = "acvalang.jpg"
        self.image = Image.open(r"Image\\"[:-1] + self.name_file)
        self.draw = ImageDraw.Draw(self.image)  # Создаем инстр для рисования.
        self.width = self.image.size[0]  # Определяем ширину.
        self.height = self.image.size[1]  # Определяем висоту.
        self.pix = self.image.load()  # Вигружаем значения пикселей.

    # return image, draw, width, height, pix, name_file


# image, draw, width, height, pix, name_file = zagr_img()
# print(zagr_img()[2], zagr_img()[3])
# name_file_G = "GcFI.tap"
# koords = []
# scale = int(input("Деталізація: "))
# # обчислення розму "пікселя" пікселізації
# size_pixel = int(ceil(min(width, height) / scale))
# print("Розмір пікселя: ", size_pixel)
# range_h = int(height / size_pixel)
# range_w = int(width / size_pixel)
# box_h = range_h * size_pixel
# box_w = range_w * size_pixel
# # поправки для розміщення рамки в середині картинки
# de_w = int((width - box_w) / 2)
# de_h = int((height - box_h) / 2)
# for h in range(range_h):
#     for w in range(range_w):
#         # координати позиції для обчислення середнього кольору пікселя
#         h_p = h * size_pixel + de_h
#         w_p = w * size_pixel + de_w
#         # Обчислення середнього кольору пікеля
#         for i in range(size_pixel):
#             for j in range(size_pixel):
#                 # print(pix[i, j])
#                 R = pix[i + w_p, j + h_p][0]
#                 G = pix[i + w_p, j + h_p][1]
#                 B = pix[i + w_p, j + h_p][2]
#                 S = R + G + B
#         S = int(S / 3)
#         # Додавання координат і глибини до списку
#         koords.append(f.pos_glub(h_p, w_p, size_pixel, S,
#                                  s.max_Z, s.koef))
#         # Імітація "пікселізації" зображення
#         image = f.ris_pixel(h_p, w_p, size_pixel, S, image)
# # Створення і запис програми для станка у файл
# GcodeBody = f.Gcode_Body(koords, s.z_safe, s.feed_z, s.max_Z, s.filtr_z)
# f_gcode = open(r"Gcodes\\"[:-1] + name_file.split(".")[0] + "_" +
#                name_file_G, "w")
# f_gcode.write(f.head_end()[0] + GcodeBody + f.head_end()[1])
# f_gcode.close()
# print("Кльксть точок: ", h * w)
# image.save(r"Imgage\\"[:-1] + "_edited_" + name_file, "JPEG")
# print("Готово!")
# del draw
# input()
