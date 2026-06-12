import time
import sys

def progress_bar(total=30):
    for i in range(total + 1):
        percent = int((i / total) * 100)
        bar = "█" * i + "-" * (total - i)
        sys.stdout.write(f"\r|{bar}| {percent}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nKész!")

progress_bar()