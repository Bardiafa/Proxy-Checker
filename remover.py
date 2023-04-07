import time
import os

pt = os.path.dirname(__file__)
good = os.path.join(pt, "good.txt")
ir = os.path.join(pt, "IR.txt")

def empty_good():
    open(good, 'w').close()
    open(ir, 'w').close()
    print(f"Emptied!")

empty_good()
