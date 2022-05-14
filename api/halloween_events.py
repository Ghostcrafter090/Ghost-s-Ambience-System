import pytools
import os
import time

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

class utils:
    def dayTimesGrabber():
        dayTimes = pytools.IO.getList('daytimes.pyl')[1]
        if dayTimes == 1:
            dayTimes = [[2022, 5, 11, 3, 45, 15], [2022, 5, 11, 4, 34, 10], [2022, 5, 11, 5, 16, 33], [2022, 5, 11, 5, 48, 29], [2022, 5, 11, 13, 10, 47], [2022, 5, 11, 20, 33, 6], [2022, 5, 11, 21, 5, 2], [2022, 5, 11, 21, 47, 25], [2022, 5, 11, 22, 36, 20]]
        return dayTimes

def main():
    while True:
        dateArray = pytools.clock.getDateTime()
        dayTimes = utils.dayTimesGrabber()
        cestj = dayTimes[5][3] - 1
        halloweenMode = False
        if (dateArray[1] == 10) or ((dateArray[1] == 11) and (dateArray[2] == 1) and (dateArray[3] < 12)):
            halloweenMode = True
            if os.path.isfile("halloweenmode.derp") == False:
                pytools.IO.saveFile('halloweenmode.derp', "1")
        elif dateArray[1] == 11:
            if dateArray[2] == 1:
                if dateArray[3] < 12:
                    halloweenMode = True
                    if os.path.isfile("halloweenmode.derp") == False:
                        pytools.IO.saveFile('halloweenmode.derp', "1")
        if halloweenMode:
            if dateArray[3] == dayTimes[5][3]:
                if dateArray[4] == dayTimes[5][4]:
                    pytools.sound.main.playSoundAll("darkrumble.mp3", 100, 1.0, 0.0, 0)
                    time.sleep(60)
            if dateArray[3] == cestj:
                if dateArray[4] == dayTimes[5][4]:
                    pytools.sound.main.playSoundAll("darkrumble.mp3", 100, 1.0, 0.0, 0)
                    time.sleep(60)
            if dateArray[3] == dayTimes[6][3]:
                if dateArray[4] == dayTimes[6][4]:
                    pytools.sound.main.playSoundAll("darkrumble.mp3", 100, 1.0, 0.0, 0)
                    time.sleep(60)
            if dateArray[3] == dayTimes[7][3]:
                if dateArray[4] == dayTimes[7][4]:
                    pytools.sound.main.playSoundAll("darkrumble.mp3", 100, 1.0, 0.0, 0)
                    time.sleep(60)
            if dateArray[3] == dayTimes[8][3]:
                if dateArray[4] == dayTimes[8][4]:
                    pytools.sound.main.playSoundAll("darkrumble.mp3", 100, 1.0, 0.0, 0)
                    time.sleep(60)
            if dateArray[2] == 31:
                if dateArray[3] == 23:
                    if dateArray[4] == 45:
                        pytools.sound.main.playSoundAll("midnightonhalloween.mp3", 100, 1.0, 0.0, 0)
                        time.sleep(60)
            if dateArray[1] == 10:
                if dateArray[2] >= 25:
                    if dateArray[3] == 11:
                        if dateArray[4] == 11:
                            pytools.sound.main.playSoundWindow("draculasrevenge.mp3;draculasrevenge.mp3", [50, 100], 1.0, 0.0, 0)
                            time.sleep(60)
            if (dateArray[1] == 10) or ((dateArray[1] == 11) and (dateArray[2] == 1)):
                if dateArray[2] >= 20:
                    if dateArray[3] == 3:
                        if dateArray[4] == 11:
                            pytools.sound.main.playSoundWindow("comelittlechildren.mp3;comelittlechildren.mp3", [50, 100], 1.0, 0.0, 0)               
        else:
            os.system('del .\\halloweenmode.derp /f /s /q')
            time.sleep(55)
        time.sleep(5)

def run():
    main()

