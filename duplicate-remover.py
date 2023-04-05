import time
import os

pt = os.path.dirname(__file__)
good = os.path.join(pt, "good.txt")

def empty_good():
    open(good, 'w').close()
    print(f"Emptied!")

empty_good()
