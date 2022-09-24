from time import sleep
import random

for x in range(10):
    value = str(random.randint(1, 20))
    if len(value) == 1:
        value = "X" + value
    print("XX" + value)
    sleep(0.01*(x**2) + 0.1)