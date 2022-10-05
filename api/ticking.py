import pytools
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

def main():
    dateArray = pytools.clock.getDateTime()
    diaa = dateArray[4]
    diab = diaa + 30
    while diab >= 60:
        diab = diab - 60
    while True:
        dateArray = pytools.clock.getDateTime()
        if dateArray[4] == diaa:
            pytools.sound.main.playSound("ticking.mp3", 0, 100, 1.0, 0.0, 0, clock=False)
        if dateArray[4] == diab:
            pytools.sound.main.playSound("ticking.mp3", 0, 100, 1.0, 0.0, 0, clock=False)
        time.sleep(60)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()
        