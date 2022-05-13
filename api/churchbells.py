import pytools
import time
import os

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

def playDeath():
    if os.path.isfile("halloweenmode.derp"):
        pytools.sound.main.playSoundWindow("dnwbella.mp3;dnwbella.mp3", [20, 100], 1.0, 0, 1)

def main():
    while True:
        weekDay = pytools.clock.getDayOfWeek()
        dateArray = pytools.clock.getDateTime()
        if dateArray[3] == 9:
            if dateArray[4] == 5:
                pytools.sound.main.playSoundWindow("cb1.mp3;cb1.mp3", [10, 100], 1.0, 0, 1)
                playDeath()
        if dateArray[3] == 14:
            if dateArray[4] == 5:
                pytools.sound.main.playSoundWindow("cb4.mp3;cb4.mp3", [10, 100], 1.0, 0, 1)
                playDeath()
        if dateArray[3] == 18:
            if dateArray[4] == 5:
                pytools.sound.main.playSoundWindow("cb5.mp3;cb5.mp3", [10, 100], 1.0, 0, 1)
                playDeath()
        if weekDay == 0:
            if dateArray[3] == 10:
                if dateArray[4] == 35:
                    pytools.sound.main.playSoundWindow("cb2.mp3;cb3.mp3", [10, 100], 1.0, 0, 1)
                    playDeath()
            if dateArray[3] == 11:
                if dateArray[4] == 50:
                    pytools.sound.main.playSoundWindow("cb2.mp3;cb3.mp3", [10, 100], 1.0, 0, 1)
                    playDeath()
        time.sleep(60)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()