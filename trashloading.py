import time
import sys
import random

def boot_loading():
    print("SYSTEM BOOT INITIATED...")
    time.sleep(1)
    
    for _ in range(20):
        percent = random.randint(1, 100)
        sys.stdout.write(f"\rLoading modules... {percent}%")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\nACCESS GRANTED")

boot_loading()