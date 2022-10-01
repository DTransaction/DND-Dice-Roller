import time 
import RPi.GPIO as GPIO 

#General Setup 
pin = 37
GPIO.setmode(GPIO.BOARD)  # Sets how we reference GPIO pins 
GPIO.setup(pin, GPIO.OUT)
GPIO.setwarnings(False)
print("Begin")

try:
    while True:
        user_input = ""
        user_input = input("turn on LED? enter '1'\n")
        if user_input == "1":
            GPIO.output(pin, 1)
            time.sleep(3)
            GPIO.output(pin, 0)

except KeyboardInterrupt:
    GPIO.cleanup() #cleansup all of the GPIO pins used within the script
    print("Done") #informs the user the program is finished running