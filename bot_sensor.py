import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.IN)

GPIO.output(11,True)
time.sleep(0.0001)
GPIO.output(11,False)

while GPIO.input(13) == False:
    start = time.time()

while GPIO.input(13) == True:
    end = time.time()

sig_time = end-start

#cm:
distance = sig_time / 0.000058

print('Distance: {} cm'.format(distance))

GPIO.cleanup()
