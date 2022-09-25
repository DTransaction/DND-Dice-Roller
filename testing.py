import time
import RPi.GPIO as GPIO

#General Setup
pins = [40]
GPIO.setmode(GPIO.BOARD)  # Sets how we reference GPIO pins
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setwarnings(False)
print("Begin")

try:
    while True:
        while GPIO.input(40) == GPIO.HIGH:
            print("hi")

except KeyboardInterrupt:
    GPIO.cleanup() #cleansup all of the GPIO pins used within the script
    print("Done") #informs the user the program is finished running