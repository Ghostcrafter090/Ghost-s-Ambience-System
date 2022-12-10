import sound
import sys
import time
import traceback

try:
    path = str(sys.argv[1])
except:
    path = "null"
try:
    volume = float(sys.argv[2])
except:
    volume = 100
try:
    speed = float(sys.argv[3])
except:
    speed = 1
try:
    balence = float(sys.argv[4])
except:
    balence = 0.0
try:
    speaker = str(sys.argv[5])
except:
    speaker = "window"

try:
    sound.play(path, volume, speed, [speaker])
except:
    print(traceback.format_exc())