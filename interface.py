#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QMainWindow, QPushButton,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtCore import QRegExp
# QWidget,  QTextEdit,  QLabel,  QSizePolicy)
from PyQt5.QtGui import QIcon, QRegExpValidator


class L_Edit(QtWidgets.QLineEdit):
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Установки шрифта на кнопки
        font_button = QtGui.QFont()
        font_button.setFamily("Consolas")
        font_button.setPointSize(22)
        font_button.setBold(True)
        font_button.setItalic(True)
        font_button.setWeight(50)
        font_button.setStrikeOut(False)
        font_button.setKerning(True)

        self.setFont(font_button)


class TitleWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar()
        self.setGeometry(150, 150, 1500, 700)
        self.setWindowTitle("ImageToGcode")
        self.setMinimumSize(QtCore.QSize(1200, 700))
        self.setMaximumSize(QtCore.QSize(1920, 1080))

        # Установки шрифта на кнопки
        font_button = QtGui.QFont()
        font_button.setFamily("Consolas")
        font_button.setPointSize(22)
        font_button.setBold(True)
        font_button.setItalic(True)
        font_button.setWeight(50)
        font_button.setStrikeOut(False)
        font_button.setKerning(True)

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
        self.info_picture = QtWidgets.QLabel("Розмір зображення: ", self)
        self.info_picture.setGeometry(QtCore.QRect(190, 30, 550, 30))

        font_info = QtGui.QFont()
        font_info.setFamily("NewsGoth BT")
        font_info.setPointSize(20)

        self.info_picture.setFont(font_info)
        self.info_picture.setFrameStyle(1)

        # Информация о параметрах редактирования изображения
        self.sclale_show = QtWidgets.QLabel("Кратність: ", self)
        self.sclale_show.setGeometry(QtCore.QRect(210, 60, 190, 30))
        self.size_pixel = QtWidgets.QLabel("Розмір пікселя: ", self)
        self.size_pixel.setGeometry(QtCore.QRect(210, 90, 190, 30))

        self.sclale_show.setFont(font_info)
        self.size_pixel.setFont(font_info)

        font_info_edit = font_info
        font_info_edit.setFamily("Consolas")

        self.size_pixel_out = QtWidgets.QLabel(self)
        self.size_pixel_out.setGeometry(QtCore.QRect(400, 90, 100, 30))
        self.size_pixel_out.setFrameStyle(1)
        self.size_pixel_out.setFont(font_info_edit)
        self.size_pixel_out.setAlignment(QtCore.Qt.AlignRight |
                                         QtCore.Qt.AlignBaseline)



        # Елементы для просмотра загруженного и обработанного изображений
        self.origin_image = QtWidgets.QLabel(self)
        self.origin_image.setGeometry(QtCore.QRect(60, 150, 500, 500))
        self.origin_image.setFrameStyle(1)

        self.edited_image = QtWidgets.QLabel(self)
        self.edited_image.setGeometry(QtCore.QRect(580, 150, 500, 500))
        self.edited_image.setFrameStyle(1)

        # Поля ввода для параметров редактирования изображения
        self.scale_input = L_Edit(self)
        self.scale_input.setGeometry(QtCore.QRect(400, 60, 100, 30))

        # Поля ввода для параметров для создания управляющей программы
        self.max_Z_input = L_Edit(self)
        self.max_Z_input.setGeometry(QtCore.QRect(1250, 220, 100, 30))

        self.z_safe_input = L_Edit(self)
        self.z_safe_input.setGeometry(QtCore.QRect(1250, 255, 100, 30))

        self.feed_z_input = L_Edit(self)
        self.feed_z_input.setGeometry(QtCore.QRect(1250, 290, 100, 30))

        self.filtr_z_input = L_Edit(self)
        self.filtr_z_input.setGeometry(QtCore.QRect(1250, 325, 100, 30))

        # self.scale_input = L_Edit(self)
        # self.scale_input.setGeometry(QtCore.QRect(1250, 360, 100, 30))

        # self.scale_input = L_Edit(self)
        # self.scale_input.setGeometry(QtCore.QRect(1250, 395, 100, 30))

        # self.scale_input = L_Edit(self)
        # self.scale_input.setGeometry(QtCore.QRect(1250, 430, 100, 30))




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
