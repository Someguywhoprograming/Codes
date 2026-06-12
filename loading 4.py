import sys
import time
from tkinter.ttk import Progressbar

def gepel(szoveg):
    for betu in szoveg:
        sys.stdout.write(betu)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

gepel("Kapcsolódás a szerverhez...")
Progressbar()