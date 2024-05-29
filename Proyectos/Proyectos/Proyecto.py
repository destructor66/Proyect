
from gpiozero import OutputDevice
from time import sleep
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

# Definir los pines GPIO de la Raspberry Pi
ENA = OutputDevice(27)  # Habilitar/Deshabilitar el puente H
IN1 = OutputDevice(17)  # Control de la bobina A del motor paso a paso
IN2 = OutputDevice(18)  # Control de la bobina A del motor paso a paso
IN3 = OutputDevice(22)  # Control de la bobina B del motor paso a paso
IN4 = OutputDevice(23)  # Control de la bobina B del motor paso a paso

# Definir la secuencia de pasos del motor paso a paso (esta es una secuencia de 8 pasos)
# Ajusta la secuencia según el tipo de motor paso a paso que estés utilizando
secuencia_pasos_a = [
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 1, 0),
    (0, 0, 1, 1),
    (0, 0, 0, 1),
    (1, 0, 0, 1)
]

secuencia_pasos = [
    (1, 0, 0, 1),
    (0, 0, 0, 1),
    (0, 0, 1, 1),
    (0, 0, 1, 0),
    (0, 1, 1, 0),
    (0, 1, 0, 0),
    (1, 1, 0, 0),
    (1, 0, 0, 0)
]

# Función para configurar los pines del puente H según la secuencia de pasos
def set_pins(secuencia):
    IN1.value, IN2.value, IN3.value, IN4.value = secuencia

# Función para girar el motor un número específico de pasos en una dirección
def girar_motor(direccion, pasos_totales, velocidad=0.001):
    # Activar el puente H
    ENA.on()
    
    # Determinar la dirección del giro
    if direccion == "adelante":
        pasos = secuencia_pasos_a
    elif direccion == "atras":
        pasos = secuencia_pasos
    else:
        raise ValueError("Dirección desconocida. Use 'adelante' o 'atras'.")
    
    # Realizar los pasos necesarios
    for _ in range(pasos_totales):
        for paso in pasos:
            set_pins(paso)
            sleep(velocidad)
    
    # Desactivar el puente H
    ENA.off()

# Girar el motor 800 pasos hacia adelante
def girar_800_pasos_adelante():
    girar_motor("adelante", 800)
    
# Girar el motor 239 pasos hacia adelante
def girar_239_pasos_adelante():
    girar_motor("adelante", 239)

# Girar el motor 120 pasos hacia adelante
def girar_120_pasos_adelante():
    girar_motor("adelante", 120)
    
# Girar el motor 121 pasos hacia adelante
def girar_121_pasos_adelante():
    girar_motor("adelante", 122)
    
# Girar el motor 122 pasos hacia adelante
def girar_122_pasos_adelante():
    girar_motor("adelante", 126)
    
# Girar el motor 275 pasos hacia adelante
def girar_265_pasos_adelante():
    girar_motor("adelante", 260)
    
# Girar el motor 877 pasos hacia atrás
def girar_870_pasos_atras():
    girar_motor("atras", 870)
    
    
    
# Girar el motor 800 pasos hacia atrás
def girar_800_pasos_atras():
    girar_motor("atras", 800)

class Formulario(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selecciona tu bebida")
        self.setStyleSheet("background-color: black;")
        self.resize(800, 480)  # Establecer el tamaño del formulario en 800x480

        layout = QHBoxLayout()

        # Cargar el archivo de estilo QSS
        with open('styles.qss', 'r') as f:
            self.setStyleSheet(f.read())

        # Botón para la bebida Paloma
        btn_paloma = QPushButton(self)
        btn_paloma.setIconSize(QSize(200, 200))  # Tamaño del icono más grande
        self.set_button_icon(btn_paloma, "palomaa.png")
        btn_paloma.clicked.connect(self.preparar_paloma)
        btn_paloma.setCursor(Qt.PointingHandCursor)
        layout.addWidget(btn_paloma, alignment=Qt.AlignCenter)

        # Botón para la bebida Charro Negro
        btn_charro_negro = QPushButton(self)
        btn_charro_negro.setIconSize(QSize(200, 200))  # Tamaño del icono más grande
        self.set_button_icon(btn_charro_negro, "charroo.png")
        btn_charro_negro.clicked.connect(self.preparar_charro_negro)
        btn_charro_negro.setCursor(Qt.PointingHandCursor)
        layout.addWidget(btn_charro_negro, alignment=Qt.AlignCenter)

        # Botón para la bebida Paris de Noche
        btn_paris_noche = QPushButton(self)
        btn_paris_noche.setIconSize(QSize(200, 200))  # Tamaño del icono más grande
        self.set_button_icon(btn_paris_noche, "pariss.png")
        btn_paris_noche.clicked.connect(self.preparar_paris_noche)
        btn_paris_noche.setCursor(Qt.PointingHandCursor)
        layout.addWidget(btn_paris_noche, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def set_button_icon(self, button, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(150, Qt.SmoothTransformation)  # Ajustar el tamaño de la imagen
        icon = QIcon(pixmap)
        button.setIcon(icon)

    def mostrar_mensaje(self, bebida):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Preparando bebida")
        msgBox.setText(f"Preparando {bebida}...")
        msgBox.setStyleSheet("QLabel{ color: white; }"
                             "QMessageBox{ background-color: black; }")  # Cambiar el fondo a negro y el texto a blanco
        msgBox.setFixedSize(200, 120)  # Establecer tamaño fijo
        msgBox.exec_()

        # Simulación de la preparación de la bebida
        self.preparar_bebida(bebida)

        msgBox2 = QMessageBox()
        msgBox2.setWindowTitle("Bebida lista")
        msgBox2.setText(f"{bebida} listo!")
        msgBox2.setStyleSheet("QLabel{ color: white; }"
                              "QMessageBox{ background-color: black; }")  # Cambiar el fondo a negro y el texto a blanco
        msgBox2.setFixedSize(200, 120)  # Establecer tamaño fijo
        msgBox2.exec_()

    def preparar_bebida(self, bebida):
        if bebida == "Paloma":
            girar_239_pasos_adelante()
            sleep(1)
            girar_120_pasos_adelante()
            
            girar_121_pasos_adelante()
            
            girar_122_pasos_adelante()
            sleep(1)
            girar_265_pasos_adelante()
            sleep(1)
            girar_870_pasos_atras()
            sleep(1)
           
            #girar_800_pasos_atras()
        elif bebida == "Charro Negro":
            girar_239_pasos_adelante()
            sleep(1)
            girar_120_pasos_adelante()
            
            girar_121_pasos_adelante()
            sleep(1)
            girar_122_pasos_adelante()
            
            girar_265_pasos_adelante()
            sleep(1)
            girar_870_pasos_atras()
            sleep(1)
        elif bebida == "Paris de Noche":
            girar_239_pasos_adelante()
            
            girar_120_pasos_adelante()
            sleep(1)
            girar_121_pasos_adelante()
            sleep(1)
            girar_122_pasos_adelante()
            
            girar_265_pasos_adelante()
            sleep(1)
            girar_870_pasos_atras()
            sleep(1)
        else:
            print(f"Bebida {bebida} desconocida")
		

    def preparar_paloma(self):
        self.mostrar_mensaje("Paloma")

    def preparar_charro_negro(self):
        self.mostrar_mensaje("Charro Negro")

    def preparar_paris_noche(self):
        self.mostrar_mensaje("Paris de Noche")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Formulario()
    ventana.show()
    sys.exit(app.exec_())

# Limpiar los pines GPIO al finalizar
ENA.close()
IN1.close()
IN2.close()
IN3.close()
IN4.close()
