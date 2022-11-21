import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while True:
        print('ein')
        GPIO.output(11,True)
        time.sleep(1)
        print('out')
        GPIO.output(11,False)
        time.sleep(1)