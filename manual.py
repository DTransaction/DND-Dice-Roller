import RPi.GPIO as GPIO #Library for the GPIO Pins
from time import sleep#Library for time-related tasks

GPIO.setmode(GPIO.BOARD) #Sets the way we reference the GPIO Pins

pins = [26, 19, 13, 6, 22, 27, 17, 23]

dat = pins[0]
ltc = pins[1]
clk = pins[2]
clr = pins[3]
d1 = pins[4]
d2 = pins[5]
d3 = pins[6]
d4 = pins[7]

for i in range(4): #Sets up GPIO pins as outputs
    GPIO.setup((dat, clk, ltc, clr), GPIO.OUT) 
for i in range(4): #Sets up GPIO pins as outputs
    GPIO.setup((d1, d2, d3, d4), GPIO.OUT) 

GPIO.output((dat, clr, d1, d2, d3), 1)
GPIO.output((clk, ltc, d4), 0)

sleep(1)

for blip in range(8): 
    GPIO.output(clk, 0)
    GPIO.output(clk, 1)


GPIO.output(ltc, 1)
sleep(0.1)
GPIO.output(ltc, 0)

sleep(5)
GPIO.cleanup()