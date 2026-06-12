from colorama import Fore, init
import time
import sys

init()

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA]

for i in range(50):
    color = colors[i % len(colors)]
    sys.stdout.write(f"\r{color}Betöltés... {i*2}%")
    sys.stdout.flush()
    time.sleep(0.1)

print("\nKész!")