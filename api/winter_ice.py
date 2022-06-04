import pytools
import os
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

class utils:
    def dataGrabber():
        out = pytools.IO.getList('.\\dataList.pyl')[1]
        if out == 1:
            out = [[0, 0, 0, 0], [0, 0, 0, 0]]
        return out
    
    def testWindow():
        out = 0
        if os.path.exists(".\\nomufflewn.derp") == True:
            out = 1
        return out

def main():
    while True:
        error = 1
        while error == 1:
            try:
                data = utils.dataGrabber()
                pytools.dummy(str(data[0][1]))
                error = 0
            except:
                error = 1
        temp = data[0][7]
        no = 0
        if temp >= 2:
            no = 1
        if temp > 2:
            temp = 2
        temp = temp - 2
        speed = 1.15 ** (-(((temp ** 2) ** 0.5) - 10))
        speed = float('{0:.3f}'.format(speed))
        vol = (((temp ** 2) ** 0.5) / 10)
        print(str(vol) + " ;;; " + str(speed))
        if vol > 1:
            vol = 1
        vol = vol * 100
        if no != 1:
            print("Playing sound...")
            if utils.testWindow() == 1:
                pytools.sound.main.playSound('ice_wall.mp3', 0, vol / 2, speed, 0, 0)
                pytools.sound.main.playSound('ice_wall.mp3', 1, vol / 2, speed, 0, 0)
                pytools.sound.main.playSound('ice_nm.mp3', 6, vol, speed, 0, 0)
            else:
                pytools.sound.main.playSound('ice_wall.mp3', 0, vol / 2, speed, 0, 0)
                pytools.sound.main.playSound('ice_wall.mp3', 1, vol / 2, speed, 0, 0)
                pytools.sound.main.playSound('ice_wn.mp3', 2, vol, speed, 0, 0)
                pytools.sound.main.playSound('ice_nm.mp3', 3, vol, speed, 0, 0)
            time.sleep(300 / speed)
        time.sleep(1)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()