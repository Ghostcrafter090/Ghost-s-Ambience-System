import pytools
import time

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

class utils:
    def dataGrabber():
        out = pytools.IO.getList('.\\dataList.pyl')[1]
        if out == 1:
            out = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        return out

def main():
    count = 0
    while True:
        dataList = utils.dataGrabber()
        dateArray = pytools.clock.getDateTime()
        if (dataList[1][5] > 4) or (dataList[0][4] == "thunder"):
            count = count + 1
            pytools.sound.main.playSoundAll("tornado_sirens.mp3", 100, 1.0, 0.0, 0)
            if count == 2:
                pytools.sound.main.playSound("radio_thunder_start.mp3", 0, 100, 1.0, 0.0, 0)
            time.sleep(104)
        else:
            if count > 0:
                pytools.sound.main.playSound("radio_thunder_end.mp3", 0, 100, 1.0, 0.0, 0)
                count = 0
        if (dateArray[2] == 1) or (dateArray[2] == 15):
            if dateArray[3] == 12:
                if dateArray[4] == 20:
                    pytools.sound.main.playSoundAll("tornado_sirens_test.mp3", 100, 1.0, 0.0, 0)
                    time.sleep(55)
        time.sleep(10)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()
        
