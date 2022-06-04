import pytools
import random
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": [],
        "explodingTreeIndex": 0
    }

class utils:
    def dataGrabber():
        out = pytools.IO.getList('.\\dataList.pyl')[1]
        if out == 1:
            out = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        return out

def main():
    while True:
        dataList = utils.dataGrabber()
        if (dataList[0][7] <= -2) or ((dataList[0][7] <= 3) and (dataList[0][4] == "snow")):
            intf = (dataList[0][7]) - 73
            if dataList[0][7] > -2:
                intf = intf - 4
            maxf = intf * 10
            minf = maxf / 3
            randa = -1
            while randa <= minf:
                randa = ((random.random() * 32768) / (32768 / maxf))
                if intf >= 68:
                    randa = randa * ((intf - 67) ** 2)
            print("Exploding Tree Wait Time: " + str(randa))
            status.vars['explodingTreeIndex'] = randa
            time.sleep(randa)
            randb = -1
            while randb <= 0:
                randb = ((random.random() * 32768) / (32768 / 5))
                pytools.sound.main.playSound("treecr1.wav", 6, 100, 1.0, 0.0, 1)
            pytools.sound.main.playSound("treeex" + str(randb) + ".wav", 6, 100, 1.0, 0.0, 1)
        else:
            time.sleep(60)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()
            