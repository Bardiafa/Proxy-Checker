import time
import os

pt = os.path.dirname(__file__)
good = os.path.join(pt, "good.txt")

def empty_good():
    open(good, 'w').close()
    print(f"Emptied!")

while True:
    empty_good()
    time.sleep(900) # set custom time to remove all proxy (in sec)
