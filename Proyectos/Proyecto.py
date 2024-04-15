
import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QStatusBar, QAction, QMessageBox, QLineEdit,  QPlainTextEdit, QFormLayout, QFileDialog, QFontDialog
from PyQt5.QtGui import QIcon

def absPath(nombre):
    return str( Path(__file__).parent.absolute()/ nombre)


class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.resize(600, 400)
        
        self.construir_menu()
        
        self.boton = QPushButton("Bienvenido a Barbuq")
        self.setCentralWidget(self.boton)
        self.boton.clicked.connect(self.abrir)

    def abrir(self):
        print("Ingresando a Barbuq")

    def construir_menu(self):
        menu = self.menuBar()
        menuBebidas = menu.addMenu("&Bebidas")
        menuBebidas.addAction("A&brir")
        submenu = menuBebidas.addMenu("Sub&menu")
        submenu.addAction("EscogerBebibas")
        submenu.addAction("BebidasEstablecidas")
        submenu.addSeparator()

        actionMensaje = QAction("Men&saje", self)
        actionMensaje.setIcon(QIcon(absPath("Bebida en proceso")))
        actionMensaje.setShortcut("Ctrl-m")
        actionMensaje.triggered.connect(self.mostrar_mensaje)
        menuBebidas.addAction(actionMensaje)
        menuBebidas.setStatusTip("Un comando informativo")

        menuControl = menu.addMenu("Control")

    def mostrar_mensaje(self):
        print("Bebida iniciada")
        #QMessageBox.information(self, "Informacion", "texto informativo")
        #QMessageBox.warning(self, "Informacion", "texto informativo")
        #QMessageBox.critical(self, "Informacion", "texto informativo")
        #QMessageBox.question(self, "Informacion", "texto informativo")
        #QMessageBox.about(self, "Informacion", "texto informativo")
     

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())