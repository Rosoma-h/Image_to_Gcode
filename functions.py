from PIL import ImageDraw


def ris_pixel(h_p, w_p, size_pixel, S, image, first_lap, ris=2):
    """Функція для заповнення квадратної області пікселями"""
    # Імітація пікселізації
    # Вигляд рисунку пікселя: 1 - суцільний квадрат
    # 2 - ромб з розміром рівним або меншим розміру пікселя, в залежності
    # від величини Diam (від 0,1 до 1)
    # ris = 1

    #     Draws an ellipse inside the given bounding box.
# PIL.ImageDraw.ImageDraw.ellipse(xy, fill=None, outline=None, width=0)
# Parameters:
# xy – Two points to define the bounding box.
# Sequence of either [(x0, y0), (x1, y1)] or [x0, y0, x1, y1],
# where x1 >= x0 and y1 >= y0.
# outline – Color to use for the outline.
# fill – Color to use for the fill.
# width –
# The line width, in pixels.

# Очистка заднього фону
    # draw = ImageDraw.Draw(image)
    # draw.rectangle((0, 0, width, height), (255, 0, 0))

    # rectangle(xy, fill=None, outline=None, width=0)
    # range_size = range(size_pixel)
    h_p_add = h_p + size_pixel
    w_p_add = w_p + size_pixel

    draw = ImageDraw.Draw(image)
    if first_lap:
        width = image.size[0]  # Определяем ширину.
        height = image.size[1]  # Определяем висоту.
        draw.rectangle((0, 0, width, height), (255, 0, 0))

    if ris == 1:
        if size_pixel != 1:
            draw.rectangle((w_p, h_p, w_p_add, h_p_add), (S, S, S))
        else:
            for i in range(size_pixel):
                for j in range(size_pixel):
                    draw.point((i + w_p, j + h_p), (S, S, S))
    elif ris == 2:
        draw.ellipse((w_p, h_p, w_p_add, h_p_add), (S, S, S))

        # for i in range(int(size_pixel / 2)):
            # for j in range(int(size_pixel / 2)):
                # wi = i + w_p
                # he =  j + h_p
                # draw.point((wi, he), (S, S, S))

    return image


def pos_glub(h_p, w_p, size_pixel, S, max_Z, koef):
    """Функція для визначення позиції і глибини точки на заготовці"""

    # Визначення позиції точки в пікселях
    half_pixel = size_pixel / 2
    X = w_p + half_pixel
    Y = h_p + half_pixel
    # Визначення позиції точки в міліметрах, koef=4 pix/mm
    X /= koef
    Y /= koef
    # Визначення глибини опускання фрези у міліметрах
    Z = S / 255 * max_Z

    return X, Y, round(Z, 1)


def head_end():
    """Функція повертає оформлені початок і закінчення файлу з G-кодом"""

    GcodeHead = '''M3
G0Z50.000
G0X50.000Y50.000S18000 \n'''
    GcodeEnd = '''G0Z50.000
G0X50.000Y50.000
G0Z50.000
G0X0Y0
M30'''

    return GcodeHead, GcodeEnd


def Gcode_Body(koords, z_safe, feed_z, max_Z, filtr_z):
    """Функція створює управляючу програму для станка
        на основі списку координат"""

    # z_safe=0.5, feed_z=100
    GcodeBody = ""
    for tochka in koords:
        # tochka_Z = tochka[2] - "негатив" зображення
        # tochka_Z = max_Z - tochka[2] "позитив" зображення
        tochka_Z = round(max_Z - tochka[2], 2)
        if tochka_Z >= filtr_z:  # Умова потрібна для введення фільтра
            GcodeBody += ("G0" + "X" + str(tochka[0]) +
                                 "Y" + str(tochka[1]) +
                                 "Z" + str(z_safe) + "\n"
                          )
            GcodeBody += ("G1" + "Z-" + str(tochka_Z) + "F" +
                          str(feed_z) + "\n" +
                          "G0" + "Z" + str(z_safe) + "\n"
                          )
    return GcodeBody
