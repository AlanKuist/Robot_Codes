import RPi.GPIO as GPIO
import time
import curses
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.IN)

try:
    while True:

        char = screen.getch()
        if char == ord('q'):
            break

     elif char == ord('z'):

        while True:
            GPIO.output(10,True)
            GPIO.output(16,True)
            GPIO.output(18,True)
            GPIO.output(8,False)
            GPIO.output(3,False)
            GPIO.output(5,False)

            while True:
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
                if distance < 20:
                    break
                GPIO.output(8,True)
                GPIO.output(16,True)
                GPIO.output(18,True)
                GPIO.output(10,False)
                GPIO.output(3,False)
                GPIO.output(5,False)
                time.sleep(3)
                GPIO.output(16,True)
                GPIO.output(18,True)
                GPIO.output(3,False)
                GPIO.output(5,True)
                GPIO.output(10,True)
                GPIO.output(8,False)
                time.sleep(3)


    elif char == 10:
        GPIO.output(16,False)
        GPIO.output(18,False)
        GPIO.output(5,False)
        GPIO.output(3,False)
        GPIO.output(8,False)
        GPIO.output(10,False)
GPIO.cleanup()
