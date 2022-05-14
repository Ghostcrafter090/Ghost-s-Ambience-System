import pytools
import random
import time

class status:
    apiKey = ""
    vars = {
        "lastLoop": [],
        "trickOrTreatIndex": 0
    }

def main():
    while True:
        dateArray = pytools.clock.getDateTime()
        if dateArray[1] == 10:
            if dateArray[2] >= 20:
                randf1 = 32768
                randf2 = randf1 * 1000
                randf3 = randf2 / 372
                randf4 = randf3 * dateArray[3]
                randf4 = (randf4 / 100) / ((32 - dateArray[2]) ** 2)
                status.vars['trickOrTreatIndex'] = randf4
                if (32768 * random.random()) < randf4:
                    pytools.sound.main.playSound('doorbell.mp3', 0, 100, 1.0, 0.0, 0)
                    time.sleep(10)
                    pytools.sound.main.playSound('distanttrt' + str(random.randint(0, 6)) + ".mp3", 0, 100, 1.0, 0.0, 0)
        time.sleep(300)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()