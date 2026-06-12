import time
import sys

def cyber_loading():
    print("Rendszer indítása...")
    time.sleep(1)
    
    for i in range(101):
        sys.stdout.write(f"\r[{'█'*(i//2)}{' '*(50-i//2)}] {i}%")
        sys.stdout.flush()
        time.sleep(0.03)
    
    print("\nHozzáférés engedélyezve!")

cyber_loading()