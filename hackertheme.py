import sys
import time
import random
from colorama import Fore, Style, init

init()

def typewriter(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def hacker_loading():
    print(Fore.GREEN + Style.BRIGHT)
    
    typewriter("Initializing secure connection...")
    time.sleep(0.5)
    typewriter("Bypassing firewall...")
    time.sleep(0.5)
    typewriter("Injecting payload...")
    time.sleep(0.5)
    
    # Loading bar
    for i in range(101):
        bar = "█" * (i // 2) + " " * (50 - (i // 2))
        sys.stdout.write(f"\rACCESSING TARGET [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.03)
    
    print("\n")
    time.sleep(0.5)
    
    # Random data stream
    for _ in range(20):
        line = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(60))
        print(line)
        time.sleep(0.05)
    
    typewriter("\nACCESS GRANTED.")
    print(Style.RESET_ALL)

hacker_loading()