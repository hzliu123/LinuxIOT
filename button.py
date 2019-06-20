import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
while (True):
    print(GPIO.input(4))
    sleep(0.3)
