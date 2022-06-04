import time
import pytools

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

def hello():
    time.sleep(5)
    return 0

def run():
    while True:
        hello()
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True
