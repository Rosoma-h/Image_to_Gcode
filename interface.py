# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zad_1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 372)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1980, 1080))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian,
                                            QtCore.QLocale.Ukraine))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored,
                                           QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
        self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.zagruzka = QtWidgets.QPushButton(self.centralwidget)
        self.zagruzka.setGeometry(QtCore.QRect(50, 50, 100, 50))
        self.prosmotr = QtWidgets.QPushButton(self.centralwidget)
        self.prosmotr.setGeometry(QtCore.QRect(200, 50, 100, 50))

        font_button = QtGui.QFont()
        font_button.setFamily("Consolas")
        font_button.setPointSize(16)
        font_button.setBold(False)
        font_button.setItalic(True)
        font_button.setWeight(50)
        font_button.setStrikeOut(False)
        font_button.setKerning(True)

        self.zagruzka.setFont(font_button)
        self.zagruzka.setCheckable(False)
        self.zagruzka.setObjectName("pushButton")
        self.prosmotr.setFont(font_button)
        self.prosmotr.setCheckable(False)
        self.prosmotr.setObjectName("prosmotr_btn")

        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(400, 50, 40, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.lineEdit_1.setFont(font)

        self.lineEdit_1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        # self.lineEdit_1.setInputMethodHints
        # (QtCore.Qt.ImhDialableCharactersOnly
        # |QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly
        # |QtCore.Qt.ImhNoPredictiveText)

        # Валидатор
        reg_ex = QRegExp("[0-9]+[0-9]")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_1)
        self.lineEdit_1.setValidator(input_validator)
        self.lineEdit_1.setInputMask("")

        self.lineEdit_1.setCursorPosition(0)
        self.lineEdit_1.setMaxLength(5)
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setClearButtonEnabled(False)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 90, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # MainWindow.setCentralWidget(self.centralwidget)

        # Інформація про розмір зображення
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 12, 330, 30))
        font_l = QtGui.QFont()
        font_l.setFamily("NewsGoth BT")
        font_l.setPointSize(14)
        self.label.setFont(font_l)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("ImageToGcode", "ImageToGcode"))
        self.zagruzka.setText(_translate("MainWindow", "Загр."))
        self.prosmotr.setText(_translate("MainWindow", "Просм."))
        self.label.setText(_translate("MainWindow", "Розмір зображення: "))
