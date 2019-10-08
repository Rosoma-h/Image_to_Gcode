from PIL import Image, ImageDraw


def ris_pixel(h_p, w_p, size_pixel, S, image, ris=1):
    """Функція для заповнення квадратної області пікселями"""
    # Імітація пікселізації
    # Вигляд рисунку пікселя: 1 - суцільний квадрат
    # 2 - ромб з розміром рівним або меншим розміру пікселя, в залежності 
    # від величини Diam (від 0,1 до 1)
    # ris = 1  
    
    draw = ImageDraw.Draw(image)
    if ris == 1:       
                for i in range(size_pixel):
                    for j in range(size_pixel):
                        draw.point((i + w_p, j + h_p), (S, S, S))
    # elif ris == 2:
        # if size_pixel % 2 != 0:
            # size_pixel -= 1
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
        if tochka_Z >= filtr_z: # Умова потрібна для введення фільтра
            GcodeBody += ("G0" + "X" + str(tochka[0]) +
                                "Y" + str(tochka[1]) +
                                "Z" + str(z_safe) + "\n"
                             )
            GcodeBody += ("G1" + "Z-" + str(tochka_Z) + "F" 
            + str(feed_z) + "\n" +
                            "G0" + "Z" + str(z_safe) + "\n"
                            )
    return GcodeBody
                        










