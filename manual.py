import RPi.GPIO as GPIO #Library for the GPIO Pins
from time import sleep #Library for time-related tasks

GPIO.setmode(GPIO.BOARD) #Sets the way we reference the GPIO Pins

PINS = [37, 35, 33, 31, 15, 13, 11, 16]

DATA = PINS[0]
LATCH = PINS[1]
CLOCK = PINS[2]
CLEAR = PINS[3]
DIGIT_1 = PINS[4]
DIGIT_2 = PINS[5]
DIGIT_3 = PINS[6]
DIGIT_4 = PINS[7]

CHARACTER = {
    "1": [0, 0, 0, 0, 0, 1, 1, 0],
    "2": [0, 1, 0, 1, 1, 0, 1, 1],
    "3": [0, 1, 0, 0, 1, 1, 1, 1],
    "4": [0, 1, 1, 0, 0, 1, 1, 0],
    "5": [0, 1, 1, 0, 1, 1, 0, 1],
    "6": [0, 1, 1, 1, 1, 1, 0, 1],
    "7": [0, 0, 0, 0, 0, 1, 1, 1],
    "8": [0, 1, 1, 1, 1, 1, 1, 1],
    "9": [0, 1, 1, 0, 1, 1, 1, 1],
    "0": [0, 0, 1, 1, 1, 1, 1, 1],
    "A": [0, 1, 1, 1, 0, 1, 1, 1],
    "B": [0, 1, 1, 1, 1, 1, 0, 0],
    "C": [0, 0, 1, 1, 1, 0, 0, 1],
    "D": [0, 1, 0, 1, 1, 1, 1, 0],
    "E": [0, 1, 1, 1, 1, 0, 0, 1],
    "F": [0, 1, 1, 1, 0, 0, 0, 1],
    "X": [0, 0, 0, 0, 0, 0, 0, 0]
}

GPIO.setup((DATA, LATCH, CLOCK, CLEAR, DIGIT_1, DIGIT_2, DIGIT_3, DIGIT_4), GPIO.OUT)
 
GPIO.output(CLEAR, 1)
GPIO.output((CLOCK, LATCH), 0)



"""Function definitions"""

def tick(): 
    GPIO.output(CLOCK, 1)
    GPIO.output(CLOCK, 0)

def release():
    GPIO.output(LATCH, 1)
    GPIO.output(LATCH, 0)

def clean():
    GPIO.output(CLEAR, 0)
    GPIO.output(CLEAR, 1)

def display_character(character: str): 
    for status in CHARACTER[character]:
        GPIO.output(DATA, status)
        tick()
    release()

def digit_select(digit: int):
    off_list = [DIGIT_1, DIGIT_2, DIGIT_3, DIGIT_4]
    off_list.remove(digit)
    for off_digit in off_list:
        GPIO.output(off_digit, 1)
    GPIO.output(digit, 0)

def four_digit(statement: str):
    digit_list = [DIGIT_1, DIGIT_2, DIGIT_3, DIGIT_4]
    for x in range(1000):
        for i in range(4): 
            clean() 
            digit_select(digit_list[i])
            display_character(statement[i])
            sleep(0.5)



"""Main script"""

try:
    four_digit("8XXX")
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()