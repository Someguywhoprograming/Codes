import winsound
import time

uzenet = "WELCOME"

for betu in uzenet:
    print(betu, end="", flush=True)
    winsound.Beep(1000, 100)
    time.sleep(0.1)

print()
