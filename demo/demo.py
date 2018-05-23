import math # Modul math
import time # Modul time


#Stream starten
motion service start

#Motoren starten
from aufraeumen import *
from setup import * # GPIO Setup importieren und ausführen

try:
        while 1:
                losfahren()
                pr.start(50) # Motor A, speed Tastverhältnis
                pl.start(10) # Motor B, speed Tastverhältnis

except KeyboardInterrupt:
        bremsen()
        aufraeumen()

#Servo-Test starten
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)

try:
        while True:
                p.ChangeDutyCycle(7.5) # turn towards 90 degree
                time.sleep(1) # sleep 1 second
                p.ChangeDutyCycle(2.5) # turn towards 0 degree
                time.sleep(1) # sleep 1 second
                p.ChangeDutyCycle(12.5) # turn towards 180 degree
                time.sleep(1) # sleep 1 second