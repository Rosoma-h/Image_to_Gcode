from PyQt5 import QtWidgets
import sys
from interface import Ui_MainWindow
from ImageToGcode import ZagrImg
# Create aplication

app = QtWidgets.QApplication(sys.argv)


# Create form and init UI

Form = QtWidgets.QWidget()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()

# Logi

# ui.lineEdit_1.setText("333")
# ui.lineEdit_1.clear()


def perenos_texta():
    text = ui.lineEdit_1.text()
    if text != "":
        chislo = int(text) / 3
        ui.lineEdit_2.setText(str(chislo))
        shablon = "Розмір зображення: "

        Kartinka = ZagrImg("acvalang.jpg")
        width = Kartinka.width()
        # height = Kartinka.height()

        ui.label.setText(shablon + str(width) +
                         " на " + str(height) + " пікс.")
    else:
        ui.lineEdit_1.setText('1')

ui.zagruzka.clicked.connect(perenos_texta)
# Run main loop

sys.exit(app.exec_())
