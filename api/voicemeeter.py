import pytools
import os
import time
import psutil

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

def main():
    while True:
        if os.path.exists("C:\Program Files (x86)\VB\Voicemeeter\\voicemeeter8.exe"):
            if os.path.exists("..\..\Voicemeeter.lnk"):
                if ("voicemeeter8.exe" in (p.name() for p in psutil.process_iter())) == False:
                    os.system("taskkill /f /im voicemeeter8.exe")
                    os.system('start /b "" ..\..\Voicemeeter.lnk')
        time.sleep(5)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()