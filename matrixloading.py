import time
import random

def matrix_loading():
    chars = "01"
    for _ in range(30):
        line = "".join(random.choice(chars) for _ in range(60))
        print(line)
        time.sleep(0.05)
    print(">> SYSTEM READY")

matrix_loading()