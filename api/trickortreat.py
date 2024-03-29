import pytools
import random
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": [],
        "trickOrTreatIndex": 0
    }

def main():
    while True:
        dateArray = pytools.clock.getDateTime()
        dayTimes = pytools.IO.getList("dayTimes.pyl")[1]
        if pytools.clock.dateArrayToUTC([dateArray[0], dateArray[1], dateArray[2], dayTimes[5][3] - 4, dayTimes[5][4], dayTimes[5][5]]) < pytools.clock.dateArrayToUTC(dateArray):
            if dateArray[1] == 10:
                if dateArray[2] >= 20:
                    randf1 = 32768
                    randf2 = randf1 * 1000
                    randf3 = randf2 / 372
                    randf4 = randf3 * dateArray[3]
                    randf4 = (randf4 / 100) / ((32 - dateArray[2]) ** 2)
                    status.vars['trickOrTreatIndex'] = randf4
                    print("trickOrTreatIndex: " + str(randf4))
                    if (32768 * random.random()) < randf4:
                        pytools.sound.main.playSound('doorbell.mp3', 0, 40, 1.0, 0.0, 0)
                        time.sleep(10)
                        pytools.sound.main.playSound('distanttrt' + str(random.randint(1, 5)) + ".mp3", 0, 100, 1.0, 0.0, 0)
        time.sleep(300)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()