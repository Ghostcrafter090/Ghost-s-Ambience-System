import pytools
import time
import random

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }
    
def main():
    while True:
        time.sleep(100)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()