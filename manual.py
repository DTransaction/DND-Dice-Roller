import RPi.GPIO as GPIO #Library for the GPIO Pins
from time import sleep #Library for time-related tasks

GPIO.setmode(GPIO.BOARD) #Sets the way we reference the GPIO Pins

pins = [37, 35, 33, 31, 15, 13, 11, 16]

dat = pins[0]
ltc = pins[1]
clk = pins[2]
clr = pins[3]
d1 = pins[4]
d2 = pins[5]
d3 = pins[6]
d4 = pins[7]

for i in range(4): #Sets up GPIO pins as outputs
    GPIO.setup(dat, GPIO.OUT) 
    GPIO.setup(ltc, GPIO.OUT) 
    GPIO.setup(clk, GPIO.OUT) 
    GPIO.setup(clr, GPIO.OUT) 
for i in range(4): #Sets up GPIO pins as outputs
    GPIO.setup((d1, d2, d3, d4), GPIO.OUT) 

GPIO.output((dat, clr), 1)
GPIO.output((clk, ltc, d1, d4, d2, d3), 0)

sleep(1)

for x in [1, 1, 0, 1, 1, 0, 1, 0]: 
    GPIO.output(dat, x)
    GPIO.output(clk, 0)
    GPIO.output(clk, 1)


GPIO.output(ltc, 1)
GPIO.output(ltc, 0)

sleep(3)

GPIO.cleanup()