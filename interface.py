#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QMainWindow, QGridLayout, QHBoxLayout,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
from functions import path_info_text


class L_Edit(QtWidgets.QLineEdit):
    """Параметри стандартного поля вводу."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Валидатор
        input_validator = QDoubleValidator(0.0, 100.0, 2, self)
        self.setValidator(input_validator)
        self.setCursorPosition(0)
        self.setMaxLength(7)

        self.setFixedSize(110, 30)
        # Установки шрифта на поля ввода
        font_edit = QtGui.QFont()
        font_edit.setFamily("Consolas")
        font_edit.setPointSize(18)
        font_edit.setBold(True)
        font_edit.setItalic(False)
        font_edit.setWeight(50)
        font_edit.setStrikeOut(False)
        font_edit.setKerning(True)

        self.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.setFont(font_edit)


class L_Edit_int(L_Edit):
    """Параметри цілочисельного поля вводу."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        input_validator = QIntValidator(1, 1000, self)
        self.setValidator(input_validator)


class Butt(QtWidgets.QPushButton):
    """Параметри стандартної кнопки."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Установки шрифта на кнопки
        font_button = QtGui.QFont()
        font_button.setFamily('Consolas')
        font_button.setPointSize(18)
        font_button.setBold(True)
        font_button.setItalic(True)
        font_button.setWeight(50)
        font_button.setStrikeOut(False)
        font_button.setKerning(True)

        self.setFont(font_button)


class Nadpis(QtWidgets.QLabel):
    """Параметри стандарного надпису."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Установки шрифта на написах
        font_info = QtGui.QFont()
        font_info.setFamily('NewsGoth BT')
        font_info.setPointSize(14)

        self.setFont(font_info)


class TitleWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        self.setWindowIcon(QtGui.QIcon('Iconka.bmp'))

        self.statusBar()
        font_status = QtGui.QFont()
        font_status.setFamily('Consolas')
        font_status.setPointSize(18)
        self.statusBar().setFont(font_status)

        self.setGeometry(150, 150, 1600, 700)
        self.setWindowTitle('ImageToGcode')
        self.setMinimumSize(QtCore.QSize(1600, 700))
        self.setMaximumSize(QtCore.QSize(1920, 1080))

        # Кнопка загрузки изображения
        self.zagruzka = Butt('Завантаження', self)
        self.zagruzka.setFixedSize(200, 30)
        # self.zagruzka.setGeometry(QtCore.QRect(30, 30, 150, 50))

        # Кнопка просмотра редактированного изображения
        self.pixelization = Butt('Пікселізація', self)
        self.pixelization.setFixedSize(200, 30)
        # self.pixelization.setGeometry(QtCore.QRect(520, 65, 200, 50))

        # Кнопка рассчета программы
        self.calculate_path = Butt('Розрахувати траєкторію', self)
        self.calculate_path.setFixedSize(300, 30)
        self.calculate_path.setDisabled(True)

        # Кнопка сохранения Gcode
        self.save_doc = Butt('Зберегти файл', self)
        self.save_doc.setFixedSize(250, 50)
        # self.save_doc.setGeometry(QtCore.QRect(1150, 620, 250, 50))
        self.save_doc.setDisabled(True)

        # Информация про размер изображения
        self.info_picture = Nadpis('Розмір зображення: ', self)
        self.info_picture.setFixedSize(550, 30)
        # self.info_picture.setGeometry(QtCore.QRect(190, 30, 550, 30))
        self.info_picture.setFrameStyle(1)

        # Информация о параметрах редактирования изображения
        self.scale = Nadpis('Кратність: ', self)
        self.scale.setFixedSize(200, 30)
        # self.scale.setGeometry(QtCore.QRect(210, 60, 190, 30))
        self.size_pixel = Nadpis('Розмір пікселя: ', self)
        self.size_pixel.setFixedSize(200, 30)
        # self.size_pixel.setGeometry(QtCore.QRect(210, 90, 190, 30))

        # Вывод размера пикселя
        self.size_pixel_out = Nadpis(self)
        self.size_pixel_out.setFixedSize(110, 30)
        # self.size_pixel_out.setGeometry(QtCore.QRect(400, 90, 110, 30))
        self.size_pixel_out.setFrameStyle(1)
        self.size_pixel_out.setAlignment(QtCore.Qt.AlignRight |
                                         QtCore.Qt.AlignBaseline)

        # Елементы для просмотра загруженного и обработанного изображений
        self.origin_image = Nadpis(self)
        self.origin_image.setGeometry(QtCore.QRect(60, 150, 500, 500))
        self.origin_image.setFrameStyle(1)

        self.edited_image = Nadpis(self)
        self.edited_image.setGeometry(QtCore.QRect(580, 150, 500, 500))
        self.edited_image.setFrameStyle(1)

        # Інформаація про готову траєкторію

        self.path_info = Nadpis(path_info_text(), self)
        self.path_info.setFixedSize(450, 60)
        # self.path_info.setAlignment(QtCore.Qt.AlignVCenter |
                                         # QtCore.Qt.AlignBaseline)
        # self.path_info.setGeometry(QtCore.QRect(190, 30, 550, 30))
        self.path_info.setFrameStyle(1)
        self.path_info.setVisible(True)

        # Поля ввода для параметров редактирования изображения
        self.scale_input = L_Edit_int(self)
        self.scale_input.setGeometry(QtCore.QRect(400, 60, 110, 30))

        # Надписи названий полей
        self.rozmir = Nadpis(12 * ' ' + 'Розмір зони обробки', self)
        self.Width_size = Nadpis('Ширина', self)
        self.Height_size = Nadpis('Висота', self)
        self.blank = Nadpis('', self)
        self.feed_z_n = Nadpis('Вертикальна подача', self)
        self.z_safe_n = Nadpis('Висота безпеки', self)
        self.depth_Z_n = Nadpis('Максимальна глибина', self)
        self.filtr_z_n = Nadpis('Мінімальний поріг глибини', self)


        # Надписи единиц измерения
        self.unit1 = Nadpis('мм', self)
        self.unit2 = Nadpis('мм', self)
        self.unit3 = Nadpis('мм/хв', self)
        self.unit4 = Nadpis('мм', self)
        self.unit5 = Nadpis('мм', self)
        self.unit6 = Nadpis('мм', self)

        self.rozmir.setFixedSize(250, 30)
        self.blank.setFixedSize(150, 30)

        # Поля ввода для параметров для создания управляющей программы
        self.Width_size_input = L_Edit(self)
        self.Height_size_input = L_Edit(self)
        self.feed_z_input = L_Edit(self)
        self.z_safe_input = L_Edit(self)
        self.depth_Z_input = L_Edit(self)
        self.filtr_z_input = L_Edit(self)

        # Сетка из елементов інтерфейсу
        zagruz_pix = QGridLayout()
        self.setLayout(zagruz_pix)
        zagruz_pix.setSpacing(10)

        zagruz_pix.addWidget(self.zagruzka, 0, 0)
        zagruz_pix.addWidget(self.pixelization, 1, 0)

        zagruz_pix.addWidget(self.info_picture, 0, 1, 1, 3)
        zagruz_pix.addWidget(self.scale, 1, 1)
        zagruz_pix.addWidget(self.size_pixel, 2, 1)
        zagruz_pix.addWidget(self.scale_input, 1, 2)
        zagruz_pix.addWidget(self.size_pixel_out, 2, 2)

        # Розміри сітки елементів
        zagruz_pix.setGeometry(QtCore.QRect(30, 30, 1200, 90))

        # Група елеметів для показу зображень
        visualisation_elements = QHBoxLayout()
        self.setLayout(visualisation_elements)
        visualisation_elements.setSpacing(30)

        visualisation_elements.addWidget(self.origin_image)
        visualisation_elements.addWidget(self.edited_image)

        visualisation_elements.setGeometry(QtCore.QRect(50, 160, 1050, 500))

        # Сетка из елементов для параметров станка
        cnc_params = QGridLayout()
        self.setLayout(cnc_params)
        cnc_params.setSpacing(10)

        cnc_params.addWidget(self.rozmir, 1, 0, 1, 2)

        cnc_params.addWidget(self.Width_size, 2, 0)
        cnc_params.addWidget(self.Width_size_input, 2, 1)
        cnc_params.addWidget(self.unit2, 2, 2)

        cnc_params.addWidget(self.Height_size, 3, 0)
        cnc_params.addWidget(self.Height_size_input, 3, 1)
        cnc_params.addWidget(self.unit1, 3, 2)

        cnc_params.addWidget(self.blank, 4, 0)

        cnc_params.addWidget(self.feed_z_n, 5, 0)
        cnc_params.addWidget(self.feed_z_input, 5, 1)
        cnc_params.addWidget(self.unit3, 5, 2)

        cnc_params.addWidget(self.z_safe_n, 6, 0)
        cnc_params.addWidget(self.z_safe_input, 6, 1)
        cnc_params.addWidget(self.unit4, 6, 2)

        cnc_params.addWidget(self.depth_Z_n, 7, 0)
        cnc_params.addWidget(self.depth_Z_input, 7, 1,)
        cnc_params.addWidget(self.unit5, 7, 2)

        cnc_params.addWidget(self.filtr_z_n, 8, 0)
        cnc_params.addWidget(self.filtr_z_input, 8, 1,)
        cnc_params.addWidget(self.unit6, 8, 2)

        cnc_params.addWidget(self.calculate_path, 9, 0)

        cnc_params.addWidget(self.path_info, 10, 0, 1, 3)

        cnc_params.addWidget(self.save_doc, 12, 0)

        # Розміри сітки елементів
        cnc_params.setGeometry(QtCore.QRect(1110, 80, 590, 520))

        # Диалоговое окно вибора файла.
        self.openFile = QAction(QIcon('open.png'),
                                'Відкрити файл...    ',
                                self)
        self.openFile.setShortcut('Ctrl+O')
        self.openFile.setStatusTip('Відкрити новий файл')
        # openFile.triggered.connect(self.showDialog)

        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('&Файл')
        self.fileMenu.addAction(self.openFile)
        self.fileMenu = self.menubar.addMenu('&Інфо')

        self.show()

    def show_open_Dialog(self, loc='\Home'):

        fname = QFileDialog.getOpenFileName(self, 'Open file', loc,
                                'Image Files (*.png *.jpg *.bmp)')[0]
        return fname

    def show_save_Dialog(self, loc='\Home'):
        fname = QFileDialog.getSaveFileName(self, 'Save Gcode', loc,
            'G-Ccode (mm)(*.tap);;All files(*.*)')[0]
        return fname


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ex = TitleWindow()
    sys.exit(app.exec_())
