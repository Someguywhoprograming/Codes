import time
import os

def rocket():
    for i in range(10):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" * (10 - i))
        print("   🚀")
        print("   ||")
        print("   ||")
        print("  /||\\")
        time.sleep(0.3)

    print("Kilövés sikeres!")

rocket()