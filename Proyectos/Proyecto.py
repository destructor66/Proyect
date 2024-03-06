
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Hola mundo")
        self.resize(580,400)
        self.setMaximumSize(600,400)
        self.setMinimumSize(280,100)

        boton = QPushButton("Que onda guapo")
        self.setCentralWidget(boton)

        #boton.clicked.connect(self.clickear)
        #boton.pressed.connect(self.presionar)
        #boton.released.connect(self.liberar)
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_alternado)
        self.boton = boton


    def presionar(self):
        print("Boton presionado")

    def liberar(self):
        print("Boton liberado")

    def clickear(self):
        print("Boton clickeado")


    def boton_alternado(self, valor):
        print(valor)
        if valor:
            self.boton.setText("Te veo")
        else:
            self.boton.setText("Apoco si tilin")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())