# import curses and GPIO
import curses
import RPi.GPIO as GPIO
#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

# Get the curses window, turn off echoig of keyboard to screen, turn on
# install (no waiting) key response, and use special values for cursor keys
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
stdscr = curses.initscr()
stdscr.keypad(True)
try:
    while True:

        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            GPIO.output(10,True)
            GPIO.output(16,True)
            GPIO.output(18,True)
            GPIO.output(8,False)
            GPIO.output(3,False)
            GPIO.output(5,False)
        elif char == curses.KEY_DOWN:
            GPIO.output(8,True)
            GPIO.output(16,True)
            GPIO.output(18,True)
            GPIO.output(10,False)
            GPIO.output(3,False)
            GPIO.output(5,False)
        elif char == curses.KEY_RIGHT:
            GPIO.output(16,True)
            GPIO.output(18,True)
            GPIO.output(3,False)
            GPIO.output(5,True)
            GPIO.output(10,True)
            GPIO.output(8,False)
        elif char == curses.KEY_W: 
            GPIO.output(16,True)
            GPIO.output(18,True)
            GPIO.output(5,False)
            GPIO.output(3,True)
            GPIO.output(8,True)
            GPIO.output(10,False)
        elif char == 10:
            GPIO.output(16,False)
            GPIO.output(18,False)
            GPIO.output(5,False)
            GPIO.output(3,False)
            GPIO.output(8,False)
            GPIO.output(10,False)
        elif char == curses.KEY_LEFT:
            GPIO.output(16,True)
            GPIO.output(18,True)
            GPIO.output(5,False)
            GPIO.output(3,True)
            GPIO.output(10,True)
            GPIO.output(8,False)
        elif char == curses.KEY_Y:
            GPIO.output(16,True)
            GPIO.output(18,True)
            GPIO.output(3,False)
            GPIO.output(5,True)
            GPIO.output(8,True)
            GPIO.output(10,False)
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak();screen.keypad(0);curses.echo()
    curses.endwin()
