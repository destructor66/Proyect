import RPi.GPIO as GPIO
import time

# Definir los pines que se utilizarán en la Raspberry Pi
# Asegúrate de conectar correctamente los pines del motor a estos pines GPIO
coil_A_1_pin = 18
coil_A_2_pin = 23
coil_B_1_pin = 24
coil_B_2_pin = 25

# Define una secuencia de pasos
# Aquí estoy utilizando una secuencia básica. Puedes ajustarla según las especificaciones de tu motor.
# Consulta la hoja de datos del motor para obtener información específica sobre la secuencia de pasos.
StepCount = 4
Seq = range(0, StepCount)
Seq[0] = [1, 0, 0, 0]
Seq[1] = [0, 1, 0, 0]
Seq[2] = [0, 0, 1, 0]
Seq[3] = [0, 0, 0, 1]

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Función para avanzar un paso
def set_step(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

# Función para girar el motor en una dirección durante un número determinado de pasos
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            set_step(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

# Establecer la velocidad del motor y el número de pasos
# Ajusta estos valores según sea necesario
delay = 5 / 1000.0  # Velocidad del motor (en segundos)
steps = 100  # Número de pasos

# Girar el motor en una dirección
forward(delay, steps)

# Limpiar los pines GPIO
GPIO.cleanup()