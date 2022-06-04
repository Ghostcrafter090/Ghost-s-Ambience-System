import pytools
import os
import random
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": [],
        "thunderIndex": 0
    }

class utils:
    def dataGrabber():
        out = pytools.IO.getList('.\\dataList.pyl')[1]
        if out == 1:
            out = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        return out
    
    def getHorrorIndex():
        if os.path.isfile("horrorindex.cx"):
            try:
                out = float(pytools.IO.getFile("horrorindex.cx").replace(" ", ""))
            except:
                out = 0
        else:
            out = 0
        return out

class sounds:
    def thunderStorm():
        pytools.sound.main.playSound('thunder_storm_lightning.mp3', 5, 100, 1.0, 0.0, 0)
        time.sleep(13)
        pytools.sound.main.playSoundAll('thunder_storm.mp3', 50, 1.0, 0.0, 1)
    
    def thunderHeat():
        pytools.sound.main.playSound('thunder_heat_lightning.mp3', 5, 100, 1.0, 0.0, 0)
        time.sleep(13)
        pytools.sound.main.playSoundAll('thunder_heat.mp3', 50, 1.0, 0.0, 1)


def main():
    while True:
        dataList = utils.dataGrabber()
        horrorIndex = utils.getHorrorIndex()
        dateArray = pytools.clock.getDateTime()
        if dataList[1][5] > 4:
            sounds.thunderStorm()
        if dataList[0][4] == "thunder":
            sounds.thunderStorm()
        tempc = dataList[0][7]
        if tempc < 16:
            tempc = 16
        if tempc < -7:
            tempc = 16 + ((tempc * (0 - 1)) - 7)
        chance = ((dateArray[3] ** 2) * (tempc - 15)) + horrorIndex
        status.vars['thunderIndex'] = chance
        print("Thunder Chance: " + str((chance * 100) / 32768) + "%")
        if (random.random() * 32768) < chance:
            if dataList[0][4] == 'rain':
                sounds.thunderStorm()
            else:
                sounds.thunderHeat()
        time.sleep(194)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()
    
    