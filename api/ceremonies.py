import pytools
import os
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

class handlers:
    def stopSound(permBool: bool):
        os.system('killaudio.cmd')
        if permBool == 1:
            pytools.IO.saveFile('remember.derp', "derp")
    
    def startSound():
        os.system('del remember.derp /f /q')

class RDC:
    def run():
        handlers.stopSound(1)
        pytools.sound.globals.bypass = 1
        pytools.sound.main.playSoundAll('remember.mp3', 100, 1, 0, 1)
        pytools.sound.globals.bypass = 0
        handlers.startSound()

def main():
    while True:
        dateArray = pytools.clock.getDateTime()
        if dateArray[1] == 11:
            if dateArray[2] == 11:
                if dateArray[3] == 10:
                    if dateArray[4] == 58:
                        if dateArray[5] > 40:
                            RDC.run()
                    if dateArray[4] == 59:
                        RDC.run()
                if dateArray[3] == 11:
                    if dateArray[4] == 0:
                        RDC.run()
        else:
            time.sleep(193)
        time.sleep(1)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True
        
def run():
    main()