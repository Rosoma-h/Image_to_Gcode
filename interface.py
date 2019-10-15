#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QMainWindow, QGridLayout,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtCore import QRegExp
# QWidget,  QTextEdit,  QLabel,  QSizePolicy)
from PyQt5.QtGui import QIcon, QRegExpValidator


class L_Edit(QtWidgets.QLineEdit):
    """Параметри стандартного поля вводу."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Валидатор
        reg_ex = QRegExp("[0-9]+[0-9]")
        input_validator = QRegExpValidator(reg_ex, self)
        self.setValidator(input_validator)
        self.setInputMask("")
        self.setCursorPosition(0)
        self.setMaxLength(5)
        self.setFrame(True)
        self.setClearButtonEnabled(False)

        self.setFixedSize(100, 30)
        # Установки шрифта на поля ввода
        font_edit = QtGui.QFont()
        font_edit.setFamily("Consolas")
        font_edit.setPointSize(22)
        font_edit.setBold(True)
        font_edit.setItalic(False)
        font_edit.setWeight(50)
        font_edit.setStrikeOut(False)
        font_edit.setKerning(True)

        self.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.setFont(font_edit)


class Butt(QtWidgets.QPushButton):
    """Параметри стандартної кнопки."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Установки шрифта на кнопки
        font_button = QtGui.QFont()
        font_button.setFamily("Consolas")
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
        font_info.setFamily("NewsGoth BT")
        font_info.setPointSize(14)

        self.setFont(font_info)


class TitleWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar()
        self.setGeometry(150, 150, 1600, 700)
        self.setWindowTitle("ImageToGcode")
        self.setMinimumSize(QtCore.QSize(1200, 700))
        self.setMaximumSize(QtCore.QSize(1920, 1080))

        # Кнопка загрузки изображения
        self.zagruzka = Butt('Загрузка', self)
        self.zagruzka.setGeometry(QtCore.QRect(30, 30, 150, 50))

        # Кнопка просмотра редактированного изображения
        self.prosmotr = Butt('Перегляд', self)
        self.prosmotr.setGeometry(QtCore.QRect(510, 65, 150, 50))

        # Кнопка сохранения Gcode
        self.save_doc = Butt('Зберегти файл', self)
        self.save_doc.setGeometry(QtCore.QRect(1150, 620, 250, 50))

        # Информация про размер изображения
        self.info_picture = Nadpis("Розмір зображення: ", self)
        self.info_picture.setGeometry(QtCore.QRect(190, 30, 550, 30))
        self.info_picture.setFrameStyle(1)

        # Информация о параметрах редактирования изображения
        self.scale_show = Nadpis("Кратність: ", self)
        self.scale_show.setGeometry(QtCore.QRect(210, 60, 190, 30))
        self.size_pixel = Nadpis("Розмір пікселя: ", self)
        self.size_pixel.setGeometry(QtCore.QRect(210, 90, 190, 30))

        # Вывод размера пикселя
        self.size_pixel_out = Nadpis(self)
        self.size_pixel_out.setGeometry(QtCore.QRect(400, 90, 100, 30))
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

        # Поля ввода для параметров редактирования изображения
        self.scale_input = L_Edit(self)
        self.scale_input.setGeometry(QtCore.QRect(400, 60, 100, 30))

        # # Поля ввода Размеров заготовки
        self.rozmir = Nadpis('Розмір заготовки', self)
        self.Vertic_size = Nadpis('Висота', self)
        self.Horiz_size = Nadpis('Ширина', self)
        self.unit1 = Nadpis('мм', self)
        self.unit2 = Nadpis('мм', self)

        self.Vertic_size_input = L_Edit(self)
        self.Horiz_size_input = L_Edit(self)

        # Сетка из елементов для размеров заготовки
        zagotovka = QGridLayout()
        self.setLayout(zagotovka)
        zagotovka.setSpacing(10)

        zagotovka.addWidget(self.rozmir, 1, 1, 1, 5)

        zagotovka.addWidget(self.Vertic_size, 2, 0)
        zagotovka.addWidget(self.Vertic_size_input, 2, 1)
        zagotovka.addWidget(self.unit1, 2, 3)

        zagotovka.addWidget(self.Horiz_size, 3, 0)
        zagotovka.addWidget(self.Horiz_size_input, 3, 1)
        zagotovka.addWidget(self.unit2, 3, 3)

        zagotovka.setGeometry(QtCore.QRect(1280, 80, 230, 100))

        # Надписи названий полей
        self.max_Z_n = Nadpis('Максимальна глибина', self)
        self.z_safe_n = Nadpis('Висота безпеки', self)
        self.feed_z_n = Nadpis('Вертикальна подача', self)
        self.filtr_z_n = Nadpis('Мінімальний поріг глибини', self)

        # Надписи единиц измерения
        self.unit3 = Nadpis('мм', self)
        self.unit4 = Nadpis('мм', self)
        self.unit5 = Nadpis('мм/хв', self)
        self.unit6 = Nadpis('мм', self)

        # Поля ввода для параметров для создания управляющей программы
        self.max_Z_input = L_Edit(self)
        self.z_safe_input = L_Edit(self)
        self.feed_z_input = L_Edit(self)
        self.filtr_z_input = L_Edit(self)

        # Сетка из елементов для параметров станка
        cnc_params = QGridLayout()
        self.setLayout(cnc_params)
        cnc_params.setSpacing(10)

        cnc_params.addWidget(self.max_Z_n, 1, 0)
        cnc_params.addWidget(self.max_Z_input, 1, 1)
        cnc_params.addWidget(self.unit3, 1, 2)

        cnc_params.addWidget(self.z_safe_n, 2, 0)
        cnc_params.addWidget(self.z_safe_input, 2, 1)
        cnc_params.addWidget(self.unit4, 2, 2)

        cnc_params.addWidget(self.feed_z_n, 3, 0)
        cnc_params.addWidget(self.feed_z_input, 3, 1,)
        cnc_params.addWidget(self.unit5, 3, 2)

        cnc_params.addWidget(self.filtr_z_n, 4, 0)
        cnc_params.addWidget(self.filtr_z_input, 4, 1,)
        cnc_params.addWidget(self.unit6, 4, 2)

        cnc_params.setGeometry(QtCore.QRect(1110, 240, 415, 150))

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

    def showDialog(self, loc="\Home"):

        fname = QFileDialog.getOpenFileName(self, 'Open file', loc)[0]
        return fname


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ex = TitleWindow()
    sys.exit(app.exec_())
