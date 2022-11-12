import pytools
import os
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

def main():
    while True:
        # if os.path.exists("server.derp"):
        time.sleep(1)
        status.finishedLoop = True
        status.vars["lastLoop"] = pytools.clock.getDateTime()

def run():
    main()