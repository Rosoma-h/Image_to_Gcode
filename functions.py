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


def calculate_gcode(Width_size, Height_size, feed_z, z_safe,
                    depth_Z, filtr_z, koords, pict_size):
    """Функція створює управляючу програму для станка
        на основі списку координат"""
    scale_gcode, rotate_angle = resize_rectangle((Width_size, Height_size),
                                                 pict_size)
    head_gcode, end_gcode = head_end()
    body_gcode = ''
    first_move = True

    for tochka in koords:

        tochka_X = round(tochka[0] * scale_gcode, 2)
        tochka_Y = round(tochka[1] * scale_gcode, 2)
        tochka_Z = round(- depth_Z * tochka[2], 2)

        # Додавання координати з глибиною більшою за filtr_z

        if abs(tochka_Z) >= filtr_z:



            if first_move:
                body_gcode += ('G0' + 'X' + str(tochka_X) +
                               'Y' + str(tochka_Y) +
                               'Z' + str(50) + '\n'
                               )
                first_move = False

            body_gcode += ('G0' + 'X' + str(tochka_X) +
                           'Y' + str(tochka_Y) +
                           'Z' + str(z_safe) + '\n'
                           )
            body_gcode += ('G1' + 'Z' + str(tochka_Z) + 'F' +
                           str(feed_z) + '\n' +
                           'G0' + 'Z' + str(z_safe) + '\n'
                           )

    Gcode = head_gcode + body_gcode + end_gcode

    return Gcode


def convert_pil_image_to_QtPixmap(image):
    """ """
    image_data = ImageQt.ImageQt(image)
    image_pixmap = QPixmap.fromImage(image_data)
    image_pixmap = image_pixmap.scaled(QtCore.QSize(500, 500), 1, 1)

    return image_pixmap


def check_input_values(ui, def_set, Kartinka):
    """Перевірка наявності параметрів в полях вводу, а при їх наявності -
    конвертація строкового формату в числовий."""

    # Зчитування налаштувань по замовчуванню
    default_parameters = [def_set.W_size,
                          def_set.H_size,
                          def_set.feed_z,
                          def_set.z_safe,
                          def_set.depth_Z,
                          def_set.filtr_z
                          ]

    input_fields = [ui.Width_size_input,
                    ui.Height_size_input,
                    ui.feed_z_input,
                    ui.z_safe_input,
                    ui.depth_Z_input,
                    ui.filtr_z_input
                    ]

    W_size = ui.Width_size_input.text()
    H_size = ui.Height_size_input.text()

    # Якщо картинка завантажена і розміри області обробки не задано -
    # задати область відповідно розмірам зображення
    if (
        Kartinka and
        (not(W_size) or W_size == '0') and
        (not(H_size) or H_size == '0')
    ):

        ui.Width_size_input.setText(str(Kartinka.size[0]))
        ui.Height_size_input.setText(str(Kartinka.size[1]))

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

    params = map(check, default_parameters, input_fields)
    work_parameters = [convert_to_digit(x) for x in params]

    return work_parameters


def path_info_text(len_Z_down_feed='0', len_rapid_feed='0'):
    """Функція, яка форматує вивід інформаціі про траєкторію."""
    text_info_path = ('Довжина подачі врізання: ' +
                      len_Z_down_feed + ' мм\n' +
                      'Довжина швидких переміщень: ' +
                      len_rapid_feed + ' мм')

    return text_info_path


def resize_rectangle(size_user_input_rect=(1, 1), size__loaded_image=(1, 1)):
    """Функція яка визначає пропорції для визначення координат."""
    scale_out, rotate_angle = 0, 0
    for k, s1 in enumerate(size__loaded_image):
        for n, s2 in enumerate(size_user_input_rect):
            scale = s2 / s1
            line = scale * size__loaded_image[k - 1]
            if line <= size_user_input_rect[n - 1]:
                if scale_out < scale:
                    scale_out = scale
                    if k != n:
                        rotate_angle = 1

    return round(scale_out, 3), rotate_angle


def convert_str_to_digit(digits):
    """Функція конвертує строку в число, в ціле або з плаваючою точкою."""
    if len(digits):
        if '.' in digits:
            digits = float(digits)
        else:
            digits = int(digits)

    return digits


def change_of_position(current_move_point, prev_move_point):
    """Фунція обчислює величину переміщення відносно попередньої
        точки(строки) і повертає відстань і тип переміщення
        (rapid moves or feed moves)"""
    change_pos = {'X': 0, 'Y': 0, 'Z': 0}
    quad_sum = 0

    for key in change_pos.keys():
        if current_move_point[key] != prev_move_point[key]:
            change_pos[key] = current_move_point[key] - prev_move_point[key]
            quad_sum += change_pos[key] ** 2

    quad_sum = quad_sum ** 0.5

    return current_move_point['kommand'], round(quad_sum, 4)


def path_lenght(Gcode):
    """Функція для обчислення довжини робочої подачі
         і холостого ходу при виконанні програми на станку."""

    # current_move_point, prev_move_point = (0, 0, 0), (0, 0, 0)
    cut_feed, rapid_feed = 0, 0
    current_move_point = {'X': None, 'Y': None, 'Z': None}
    prev_move_point = {'X': None, 'Y': None, 'Z': None}
    # x_koord, y_koord, z_koord = 0, 0, 0
    flag = ''
    Gcode = Gcode.split('\n')

    for n, stroka in enumerate(Gcode, 1):
        print('\n', n, ': ')
        stroka += '*'  # Add symbol end of string
        digits = ''
        flag = ''
        kommand = stroka[0:2]
        params = stroka[2:]

        if kommand == 'G0' or kommand == 'G1':

            current_move_point['kommand'] = kommand
            for char in params:

                if char.isalpha():

                    digits = convert_str_to_digit(digits)
                    if flag:
                        current_move_point[flag] = digits
                    print(flag, digits, sep='', end='')
                    print(' ', end='')
                    flag = char
                    digits = ''

                elif char.isdigit() or char == '.' or char == '-':
                    digits += char

                if char == '*':

                    digits = convert_str_to_digit(digits)
                    if flag:
                        current_move_point[flag] = digits

                    print(flag, digits, sep='', end='')

        # print('\n', n, ': ')
        print('\n', 'Попередня: ', prev_move_point)
        prev_move_point.update(current_move_point)
        print(' Теперішня: ', current_move_point)

    cut_feed, rapid_feed

    return cut_feed, rapid_feed
