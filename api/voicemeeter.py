import pytools
import os
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

def main():
    while True:
        os.system('start /b /wait "" ..\..\Voicemeeter.lnk')
        time.sleep(86400)
        os.system("taskkill /f /im voicemeeter8.exe")
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()