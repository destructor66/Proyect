import RPi.GPIO as GPIO
import time
from pathlib import Path


# pines GPIO
GPIO.setmode(GPIO.BOARD)

#pines para el control del motor a pasos
StepPins = [11, 12, 13, 15] 

# pines como salidas
for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

# secuencia de pasos para un motor a pasos de 4 fases
Seq = [[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]]

#cantidad de pasos por vuelta
StepCount = len(Seq)

# velocidad del motor (en segundos por paso)
StepDelay = 0.01

# Función para avanzar el motor un paso
def step_forward():
    for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)

    global StepCount
    StepCounter += 1

    # Si hemos llegado al final de la secuencia, volvemos al principio
    if (StepCounter == StepCount):
        StepCounter = 0
    if (StepCounter < 0):
        StepCounter = StepCount-1

# Función para retroceder el motor un paso
def step_backward():
    for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)

    global StepCount
    StepCounter -= 1

    # Si hemos llegado al principio de la secuencia, volvemos al final
    if (StepCounter == StepCount):
        StepCounter = 0
    if (StepCounter < 0):
        StepCounter = StepCount-1

# Inicializa el contador de pasos
StepCounter = 0

#Hacer que el motor avance 512 pasos y luego retroceda 512 pasos
try:
    while True:
        for i in range(512):
            step_forward()
            time.sleep(StepDelay)
        for i in range(512):
            step_backward()
            time.sleep(StepDelay)

except KeyboardInterrupt:
    GPIO.cleanup()
