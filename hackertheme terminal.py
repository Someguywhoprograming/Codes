import sys
import time
import random
import os
from colorama import Fore, Style, init

init()

GREEN = Fore.GREEN + Style.BRIGHT
RESET = Style.RESET_ALL

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typewriter(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def fake_ip():
    return ".".join(str(random.randint(10, 255)) for _ in range(4))

def boot_sequence():
    clear()
    print(GREEN)
    typewriter("BOOTING SECURE TERMINAL v3.7.1")
    time.sleep(0.5)
    typewriter("Loading kernel modules...")
    time.sleep(0.5)
    typewriter("Establishing encrypted tunnel...")
    time.sleep(1)
    typewriter(f"Connected to remote host: {fake_ip()}")
    time.sleep(1)

def brute_force():
    typewriter("Initiating brute force attack...")
    time.sleep(1)
    
    for i in range(101):
        bar = "█" * (i // 2) + " " * (50 - (i // 2))
        sys.stdout.write(f"\rCRACKING PASSWORD [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.03)

    print("\nPassword found: ********")
    time.sleep(1)

def data_stream():
    print("\nExtracting data packets...\n")
    for _ in range(15):
        line = "".join(random.choice("01ABCDEF") for _ in range(70))
        print(line)
        time.sleep(0.05)

def access_granted():
    print("\n")
    typewriter(">>> ACCESS GRANTED <<<", 0.05)
    time.sleep(1)

def hacker_menu():
    clear()
    print(GREEN)
    print("========== ROOT TERMINAL ==========")
    print("1. System Scan")
    print("2. Network Map")
    print("3. Extract Data")
    print("4. Exit")
    print("===================================")
    print(RESET)

    choice = input("root@system:~# ")

    if choice == "1":
        typewriter("Scanning system vulnerabilities...")
    elif choice == "2":
        typewriter("Mapping network nodes...")
    elif choice == "3":
        typewriter("Extracting secure files...")
    elif choice == "4":
        typewriter("Disconnecting...")
        return
    else:
        typewriter("Unknown command.")

    time.sleep(2)
    hacker_menu()

# ===== FUTTATÁS =====
boot_sequence()
brute_force()
data_stream()
access_granted()
hacker_menu()