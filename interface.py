#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QMainWindow, QPushButton,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtCore import QRegExp
# QWidget,  QTextEdit,  QLabel,  QSizePolicy)
from PyQt5.QtGui import QIcon, QRegExpValidator


class TitleWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar()
        self.setGeometry(200, 200, 1200, 700)
        self.setWindowTitle("ImageToGcode")
        self.setMinimumSize(QtCore.QSize(800, 400))
        self.setMaximumSize(QtCore.QSize(1600, 900))

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
        self.zagruzka = QPushButton('Загрузка', self)
        self.zagruzka.setGeometry(QtCore.QRect(30, 30, 150, 50))
        self.zagruzka.setFont(font_button)

        # Кнопка просмотра редактированного изображения
        self.prosmotr = QPushButton('Перегляд', self)
        self.prosmotr.setGeometry(QtCore.QRect(210, 30, 150, 50))
        self.prosmotr.setFont(font_button)

        # Информация про размер изображения
        self.info_picture = QtWidgets.QLabel("Розмір зображення: ", self)
        self.info_picture.setGeometry(QtCore.QRect(390, 30, 550, 30))

        font_info = QtGui.QFont()
        font_info.setFamily("NewsGoth BT")
        # font_info.setFamily("NewsGoth BT")
        font_info.setPointSize(20)

        self.info_picture.setFont(font_info)
        self.info_picture.setFrameStyle(1)

        # Информация о параметрах редактирования изображения
        self.sclale_show = QtWidgets.QLabel("Кратність: ", self)
        self.sclale_show.setGeometry(QtCore.QRect(410, 60, 190, 30))
        self.size_pixel = QtWidgets.QLabel("Розмір пікселя: ", self)
        self.size_pixel.setGeometry(QtCore.QRect(410, 90, 190, 30))

        self.sclale_show.setFont(font_info)
        self.size_pixel.setFont(font_info)

        # Поля ввода для параметров редактирования изображения
        self.scale_input = QtWidgets.QLineEdit(self)
        self.scale_input.setGeometry(QtCore.QRect(600, 60, 100, 30))
        self.scale_input.setAlignment(QtCore.Qt.AlignRight |
                                      QtCore.Qt.AlignBottom)
        font_info_edit = font_info
        font_info_edit.setFamily("Consolas")

        self.scale_input.setFont(font_info_edit)

        self.size_pixel_out = QtWidgets.QLabel(self)
        self.size_pixel_out.setGeometry(QtCore.QRect(600, 90, 100, 30))
        self.size_pixel_out.setFrameStyle(1)
        self.size_pixel_out.setFont(font_info_edit)
        self.size_pixel_out.setAlignment(QtCore.Qt.AlignRight |
                                         QtCore.Qt.AlignBaseline)

        # Валидатор
        reg_ex = QRegExp("[0-9]+[0-9]")
        input_validator = QRegExpValidator(reg_ex, self.scale_input)
        self.scale_input.setValidator(input_validator)
        self.scale_input.setInputMask("")

        self.scale_input.setCursorPosition(0)
        self.scale_input.setMaxLength(5)
        self.scale_input.setFrame(True)
        self.scale_input.setClearButtonEnabled(False)
        self.scale_input.setObjectName("scale_input")

        # Елементы для просмотра загруженного и обработанного изображений
        # set a scaled pixmap to a w x h window keeping its aspect ratio
        self.origin_image = QtWidgets.QLabel(self)
        self.origin_image.setGeometry(QtCore.QRect(60, 150, 500, 500))
        self.origin_image.setFrameStyle(1)

        self.edited_image = QtWidgets.QLabel(self)
        self.edited_image.setGeometry(QtCore.QRect(580, 150, 500, 500))
        self.edited_image.setFrameStyle(1)

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
