from PyQt5 import QtWidgets
import sys
from interface import Ui_MainWindow
from ImageToGcode import zagr_img
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
        width = zagr_img()[2]
        height = zagr_img()[3]
        ui.label.setText(shablon + str(width) +
                         " на " + str(height) + " пікс.")


ui.zagruzka.clicked.connect(perenos_texta)
# Run main loop

sys.exit(app.exec_())
