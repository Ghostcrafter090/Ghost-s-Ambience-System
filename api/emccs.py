import pytools
import time
import os

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

def getOutStatus():
    out = 0
    if os.path.isfile('nomufflewn.derp') == True:
        out = 1
    return out

def getTestStatus():
    out = 0
    if os.path.isfile('testemccs.derp') == True:
        out = 1
    return out

def main():
    startBool = 0
    while True:
        time.sleep(1)
        dateArray = pytools.clock.getDateTime()
        if dateArray[1] == 12:
            if getTestStatus() == 1:
                startBool = 0
            if 23 < dateArray[2] < 27:
                if startBool != 1:
                    try:
                        os.system('del testemccs.derp /f /q')
                    except:
                        pass
                    pytools.sound.main.playSoundAll("emcc-test.mp3", 20, 1, 0, 1)
                    startBool = 1
                if dateArray[3] == 10:
                    if dateArray[4] == 6:
                        pytools.sound.main.playSound("emccw1.mp3", 0, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw1.mp3", 1, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw1.mp3", 4, 20, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 11:
                    if dateArray[4] == 6:
                        pytools.sound.main.playSound("emccw2.mp3", 0, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw2.mp3", 1, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw2.mp3", 4, 20, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 12:
                    if dateArray[4] == 6:
                        pytools.sound.main.playSound("emccw3.mp3", 0, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw3.mp3", 1, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw3.mp3", 4, 20, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 13:
                    if dateArray[4] == 6:
                        pytools.sound.main.playSound("emccw4.mp3", 0, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw4.mp3", 1, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw4.mp3", 4, 20, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 14:
                    if dateArray[4] == 6:
                        pytools.sound.main.playSound("emccw5.mp3", 0, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw5.mp3", 1, 20, 1, 0, 0)
                        pytools.sound.main.playSound("emccw5.mp3", 4, 20, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 15:
                    if dateArray[4] == 0:
                        pytools.sound.main.playSound("s1.mp3", 0, 35, 1, 0, 0)
                        pytools.sound.main.playSound("s1.mp3", 1, 35, 1, 0, 0)
                        pytools.sound.main.playSound("s1.mp3", 4, 35, 1, 0, 1)
                        pytools.sound.main.playSound("s2.mp3", 0, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s2.mp3", 1, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s2.mp3", 4, 70, 1, 0, 1)
                if dateArray[3] == 16:
                    if dateArray[4] == 20:
                        pytools.sound.main.playSoundWindow("s3.mp3;s3_nm.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 17:
                    if dateArray[4] == 40:
                        pytools.sound.main.playSoundWindow("s4.mp3;s4_nm.mp3", 70, 1, 0, 1)
                        pytools.sound.main.playSoundWindow("s5.mp3;s5_nm.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 18:
                    if dateArray[4] == 0:
                        pytools.sound.main.playSound("s6.mp3", 4, 100, 1, 0, 1)
                        pytools.sound.main.playSound("s7.mp3", 4, 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 18:
                    if dateArray[4] == 10:
                        pytools.sound.main.playSound("s8_window.mp3", 4, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s8_door.mp3", 0, 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 18:
                    if dateArray[4] == 30:
                        pytools.sound.main.playSound("s9_window.mp3", 4, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s9_inside.mp3", 0, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s9_inside.mp3", 1, 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 21:
                    if dateArray[4] == 0:
                        pytools.sound.main.playSoundAll("s10.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] == 22:
                    if dateArray[4] == 30:
                        pytools.sound.main.playSound("s11_fireplace.mp3", 1, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s11_window.mp3", 3, 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  1:
                    if dateArray[4] == 0:
                        pytools.sound.main.playSound("s12_window.mp3", 4, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s12_inside.mp3", 0, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s12_inside.mp3", 1, 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  1:
                    if dateArray[4] == 20:
                        pytools.sound.main.playSoundAll("s13.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  1:
                    if dateArray[4] == 30:
                        pytools.sound.main.playSoundAll("s14.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  1:
                    if dateArray[4] == 50:
                        pytools.sound.main.playSound("s15_window.mp3", 4, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s15_inside.mp3", 0, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s15_inside.mp3", 1, 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  2:
                    if dateArray[4] == 0:
                        pytools.sound.main.playSound("s16_window.mp3", 4, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s16_fireplace.mp3", 1, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s16_clock.mp3", 0, 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  2:
                    if dateArray[4] == 20:
                        pytools.sound.main.playSoundAll("s17.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  2:
                    if dateArray[4] == 40:
                        pytools.sound.main.playSoundAll("s18.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  3:
                    if dateArray[4] == 0:
                        pytools.sound.main.playSoundAll("s19.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  3:
                    if dateArray[4] == 25:
                        pytools.sound.main.playSoundAll("s20.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  3:
                    if dateArray[4] == 45:
                        pytools.sound.main.playSoundAll("s21.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  4:
                    if dateArray[4] == 0:
                        pytools.sound.main.playSoundAll("s22.mp3", 70, 1, 0, 1)
                        time.sleep(60)
                if dateArray[3] ==  8:
                    if dateArray[4] == 0 :
                        pytools.sound.main.playSound("s23_window.mp3", 4, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s23_fireplace.mp3", 1, 70, 1, 0, 0)
                        pytools.sound.main.playSound("s23_clock.mp3", 0, 70, 1, 0, 1)
                        time.sleep(60)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()