import pytools
import time
import os
import termcolor
import sys
import threading

class flags:
    display = True
    exitf = False
    apiKey = ""
    pythonf = False
    
class system:
    def start():
        if flags.pythonf == False:
            for n in os.environ["path"].split(";"): 
                if n.find("\\Python\\") != -1:
                    flags.pythonf = n
        if flags.pythonf == False:
            flags.pythonf = input("Please specify the folder containing the python executable: ")
        if flags.apiKey == "":
            flags.apiKey = input("Please specify apiKey: ")
        if flags.apiKey != "":
            os.system("copy \"" + flags.pythonf + "python.exe\" \".\\ambience.exe\" /y")
            os.system("start /min "" ambience.exe main.py \"" + flags.apiKey + "\"")
            system.status.active = True
    
    def stop():
        os.system("taskkill /f /im ambience.exe")
        os.system("taskkill /f /im clock.exe")
        os.system("taskkill /f /im fireplace.exe")
        os.system("taskkill /f /im window.exe")
        os.system("taskkill /f /im outside.exe")
        os.system("taskkill /f /im windown.exe")
        os.system("taskkill /f /im light.exe")
        pytools.IO.saveFile(".\\working\\clocks\\running\\gwcont.derp", "derp")
        pytools.IO.saveFile(".\\working\\clocks\\running\\wcont.derp", "derp")
        system.status.active = False
    
    class status:
        active = False

class menu:
    def handler():
        try:
            menu.main()
            system.stop()
            exit(0)
        except:
            flags.exitf = True
            system.stop()
            crash["null"]
    
    def main():
        f = True
        j = False
        while True:
            if f:
                error = os.system("choice /c m /n")
            f = True
            os.system("mode con cols=200 lines=63")
            flags.display = False
            time.sleep(0.5)
            i = 0
            while i < 63:
                n = 0
                while n < 200:
                    pytools.IO.console.printAt(n, i, "          ")
                    n = n + 10
                i = i + 1
            printColor(0, 0, "Main Menu", "green")
            printColor(0, 1, "---------", "green")
            printColor(0, 3, "(r) - Return", "green")
            printColor(0, 4, "(p) - Open Plugin Inspector", "green")
            printColor(0, 5, "(s) - Start System", "green")
            printColor(0, 6, "(h) - Stop System", "green")
            printColor(0, 7, "(e) - Exit", "green")
            if j:
                printColor(0, 8, "---Error: Please start system before opening plugin menu.", "red")
                j = False
            error = os.system("choice /c rpshe /n")
            if error == 1:
                i = 0
                while i < 63:
                    n = 0
                    while n < 200:
                        pytools.IO.console.printAt(n, i, "          ")
                        n = n + 10
                    i = i + 1
                flags.display = True
            if error == 2:
                if system.status.active == True:
                    menu.pluginMenu()
                else:
                    j = True
                f = False
            if error == 3:
                system.start()
                f = False
            if error == 4:
                system.stop()
                f = False
            if error == 5:
                flags.exitf = True
                return 0
                
    plugN = 0
    plugI = 0
    plugR = False
    strF = " -------------------------------------------------------------------"
    plugF = 0
    
    def pluginMenu():
        f = True
        while f:
            i = 0
            while i < 63:
                n = 0
                while n < 200:
                    pytools.IO.console.printAt(n, i, "          ")
                    n = n + 10
                i = i + 1
            keys = "0123456789abcdefghijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            letters = "r"
            i = 0
            choices = {}
            printColor(0, 0, "Plugin Inspector", "green")
            printColor(0, 1, "----------------", "green")
            printColor(0, 3, "(r) - Return to main menu.", "green")
            for plugin in os.listdir(".\\vars\\pluginVarsjson"):
                printColor(0, i + 4, "(" + keys[i] + ") - Plugin " + plugin.split("_keys")[0] + ".", "green")
                choices[i + 2] = plugin
                letters = letters + keys[i]
                i = i + 1
            choice = os.system("choice /c " + letters + " /n /cs")
            if choice != 1:
                plugin = choices[choice]
                menu.plugN = 2
                menu.plugI = 0
                printColor(40, 0, plugin, "green")
                json = pytools.IO.getJson(".\\vars\\pluginVarsJson\\" + plugin)
                for key in json:
                    menu.readInfo(json[key], key)
                    menu.plugN = menu.plugN + 1
                    if menu.plugN > 62:
                        menu.plugN = 0
                        menu.plugI = menu.plugI + 40
                printColor(40 + menu.plugI, menu.plugN + 1, "(r) - Return to plugin menu.", "green")
                error = os.system("choice /c r /n")
            else:
                f = False
        
    
    def readInfo(json, key):
        menu.plugF = menu.plugF + 1
        if str(json)[0] == "{":
            if menu.plugR:
                menu.plugN = menu.plugN + 1
                if menu.plugN > 62:
                    menu.plugN = 0
                    menu.plugI = menu.plugI + 40
                menu.plugR = False
            printColor(40 + menu.plugI, menu.plugN, menu.strF[0:menu.plugF] + str(key) + ":", "green")
            menu.plugN = menu.plugN + 1
            if menu.plugN > 62:
                menu.plugN = 0
                menu.plugI = menu.plugI + 40
            for keyf in json:
                menu.readInfo(json[keyf], keyf)
                menu.plugN = menu.plugN + 1
                if menu.plugN > 62:
                    menu.plugN = 0
                    menu.plugI = menu.plugI + 40
        elif str(json)[0] == "[":
            printColor(40 + menu.plugI, menu.plugN, menu.strF[0:menu.plugF] + str(key) + ":", "green")
            menu.plugN = menu.plugN + 1
            if menu.plugN > 62:
                menu.plugN = 0
                menu.plugI = menu.plugI + 40
            i = 0
            for keyf in json:
                menu.readInfo(keyf, "-" + str(i))
                i = i + 1
                menu.plugN = menu.plugN + 1
                if menu.plugN > 62:
                    menu.plugN = 0
                    menu.plugI = menu.plugI + 40
        else:
            printColor(40 + menu.plugI, menu.plugN, menu.strF[0:menu.plugF] + str(key) + ": " + str(json), "green")
            menu.plugR = True
        menu.plugF = menu.plugF - 1
            
        
def printColor(x, y, text, color):
    os.system("color")
    pytools.IO.console.printAt(x, y, termcolor.colored(text, color))

spaces = "                                                                    "

def getSection():
    dateArray = pytools.clock.getDateTime()
    dayTimes = pytools.IO.getList(".\\working\\daytimes.pyl")[1]
    phases = ["Daylight Phase", "Uncanny Phase", "Dark Phase", "Evil Phase", "Sinister Phase", "Dying Phase P1", "Dying Phase P2", "Dying Phase P3", "Dying Phase P4", "Death Phase", "Necro Phase", "Reserect Phase", "Safe Phase"]
    if pytools.clock.dateArrayToUTC(dateArray) < pytools.clock.dateArrayToUTC(dayTimes[5]):
        return phases[0]
    else:
        if dateArray[3] > 12:
            if dateArray[3] < 22:
                if pytools.IO.getJson(".\\vars\\pluginVarsJson\\deathmode_keys.json")["death_wind"]["state"] == 0:
                    return phases[1]
                else:
                    if pytools.IO.getJson(".\\vars\\pluginVarsJson\\deathmode_keys.json")["monsters"]["state"] == 0:
                        return phases[2]
                    else:
                        if pytools.IO.getJson(".\\vars\\pluginVarsJson\\deathmode_keys.json")["ghosts"]["state"] == 0:
                            return phases[3]
                        else:
                            return phases[4]
            elif dateArray[3] == 22:
                if dateArray[4] < 15:
                    return phases[5]
                if dateArray[4] < 30:
                    return phases[6]
                if dateArray[4] < 45:
                    return phases[7]
                if dateArray[4] >= 45:
                    return phases[8]
            elif dateArray[3] == 23:
                return phases[9]
        elif dateArray[3] < (dayTimes[2][3] - 1):
            return phases[10]
        elif dateArray[3] == (dayTimes[2][3] - 1):
            return phases[11]
        else:
            return phases[12]

def main():
    i = 0
    os.system("mode con cols=200 lines=63")
    flash = 0
    while i < 63:
        n = 0
        while n < 200:
            pytools.IO.console.printAt(n, i, "          ")
            n = n + 10
        i = i + 1
    while True:
        if flags.exitf == True:
            exit()
        if flags.display == True:
            if (pytools.clock.getDateTime()[5] % 30) == 0:
                os.system("mode con cols=200 lines=63")
                i = 0
                while i < 63:
                    n = 0
                    while n < 200:
                        pytools.IO.console.printAt(n, i, "          ")
                        n = n + 10
                    i = i + 1
            weather = pytools.IO.getFile(".\\vars\\dispstring.cx")
            if weather[0:23] == 'Temperature (C)      : ':
                pytools.IO.console.printAt(0, 0, "Ambience System Console")
                pytools.IO.console.printAt(0, 1, "-----------------------")
                pytools.IO.console.printAt(0, 3, weather)
                i = 4 + len(weather.split("\n"))
                for plugin in os.listdir(".\\vars\\pluginVarsjson"):
                    pytools.IO.console.printAt(2, i, plugin.split("_keys")[0][0:19])
                    pInfo = pytools.IO.getJson(".\\vars\\pluginVarsJson\\" + plugin)
                    if system.status.active == True:
                        if os.path.exists(".\\vars\\plugins\\plugin." + plugin.split("_keys")[0] + ".run()-error.cx"):
                            pError = pytools.IO.getFile(".\\vars\\plugins\\plugin." + plugin.split("_keys")[0] + ".run()-error.cx")
                            if flash == 0:
                                try:
                                    if (pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) - pytools.clock.dateArrayToUTC(pInfo["lastLoop"])) > 600:
                                        printColor(0, i, "!", "red")
                                    else:
                                        printColor(0, i, "!", "yellow")
                                except:
                                    printColor(0, i, "!", "red")
                            else:
                                pytools.IO.console.printAt(0, i, " ")
                            printColor(37, i, " ;;; " + pError, "yellow")
                        else:
                            pytools.IO.console.printAt(0, i, " ")
                    if system.status.active == True:
                        try:
                            pytools.IO.console.printAt(20, i, " : ")
                            if (pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) - pytools.clock.dateArrayToUTC(pInfo["lastLoop"])) > 600:
                                printColor(23, i, "Inactive." + spaces[len("Inactive."):14], "yellow")
                            else:
                                printColor(23, i, "Active." + spaces[len("Active."):14], "green")
                        except:
                            printColor(23, i, "Nonresponsive.", "red")
                    else:
                        printColor(23, i, "Offline." + spaces[len("Offline."):14], "magenta")
                    i = i + 1
                
                y = i
                
                soundsClock = pytools.IO.getFile(".\\vars\\sounds\\clock.cxl").split("\n")
                soundsFireplace = pytools.IO.getFile(".\\vars\\sounds\\fireplace.cxl").split("\n")
                soundsOutside = pytools.IO.getFile(".\\vars\\sounds\\outside.cxl").split("\n")
                soundsWindow = pytools.IO.getFile(".\\vars\\sounds\\window.cxl").split("\n")
                
                pytools.IO.console.printAt(50, 0, "Clock Speaker Sounds")
                pytools.IO.console.printAt(50, 1, "--------------------")
                i = 3
                for f in soundsClock:
                    if system.status.active == True:
                        pytools.IO.console.printAt(50, i, f + spaces[len(f):30])
                        i = i + 1
                f = i
                while i < (f + 10):
                    pytools.IO.console.printAt(50, i, spaces[0:30])
                    i = i + 1
                
                pytools.IO.console.printAt(80, 0, "Fireplace Speaker Sounds")
                pytools.IO.console.printAt(80, 1, "------------------------")
                i = 3
                for f in soundsFireplace:
                    if system.status.active == True:
                        pytools.IO.console.printAt(80, i, f + spaces[len(f):30])
                        i = i + 1
                f = i
                while i < (f + 10):
                    pytools.IO.console.printAt(80, i, spaces[0:30])
                    i = i + 1
                
                pytools.IO.console.printAt(110, 0, "Window Speaker Sounds")
                pytools.IO.console.printAt(110, 1, "--------------------")
                i = 3
                for f in soundsWindow:
                    if system.status.active == True:
                        pytools.IO.console.printAt(110, i, f + spaces[len(f):30])
                        i = i + 1
                f = i
                while i < (f + 10):
                    pytools.IO.console.printAt(110, i, spaces[0:30])
                    i = i + 1
                    
                pytools.IO.console.printAt(140, 0, "Outside Speaker Sounds")
                pytools.IO.console.printAt(140, 1, "--------------------")
                i = 3
                for f in soundsOutside:
                    if system.status.active == True:
                        pytools.IO.console.printAt(140, i, f + spaces[len(f):30])
                        i = i + 1
                f = i
                while i < (f + 10):
                    pytools.IO.console.printAt(140, i, spaces[0:30])
                    i = i + 1
                if system.status.active == True:
                    if os.path.exists(".\\working\\halloweenmode.derp"):
                        if flash == 0:
                            printColor(3, y + 4, "        X", "red")
                            printColor(3, y + 5, "       X X", "red")
                            printColor(3, y + 6, "      X   X", "red")
                            printColor(3, y + 7, "     X  X  X", "red")
                            printColor(3, y + 8, "    X   X   X", "red")
                            printColor(3, y + 9, "   X    X    X", "red")
                            printColor(3, y + 10, "  X           X", "red")
                            printColor(3, y + 11, " X      X      X", "red")
                            printColor(3, y + 12, "X               X", "red")
                            printColor(3, y + 13, "XXXXXXXXXXXXXXXXX", "red")
                        else:
                            r = 0
                            while r < 14:
                                pytools.IO.console.printAt(3, y + r, "                  ")
                                r = r + 1
                        section = getSection()
                        printColor(23, y + 6, "DEATH NIGHT ACTIVITY", "red")
                        printColor(23, y + 7, "--------------------", "red")
                        printColor(23, y + 9, "Horror Index        : " + pytools.IO.getFile(".\\working\\horrorIndex.cx") + "Hi" + spaces[0:10], "red")
                        printColor(23, y + 10, "Whispering Index    : " + str(pytools.IO.getJson(".\\vars\\pluginVarsJson\\deathmode_keys.json")["whisperIndex"]) + "Hi" + spaces[0:10], "red")
                        printColor(23, y + 11, "Hallowed Wolf Index : " + str(pytools.IO.getJson(".\\vars\\pluginVarsJson\\deathmode_keys.json")["hallowedWolfIndex"]) + "Hi" + spaces[0:10], "red")
                        printColor(23, y + 12, "Current Section     : " + section + spaces[0:10], "red")
            if flash == 0:
                flash = 1
            else:
                flash = 0
            printColor(0, 62, "(m &+ enter) - Goto Menu", "green")
        time.sleep(0.3)

startf = False
runf = False
en = True
try:
    for n in sys.argv:
        if runf:
            if n == "--start":
                startf = True
            elif n.split("=")[0] == "--apiKey":
                flags.apiKey = n.split("=")[1]
            elif n == "--help":
                print("Ghosts Ambience System Console Usage")
                print("------------------------------------")
                print("--run: Start the console")
                print("--start: Start the system automatically upon console load.")
                print("   ^ --apiKey=<apiKey>: must be specified api key on launch.")
                print("                        This will be your Open Weather Map API Key.")
                print("--help: Print this help text.")
            else:
                print("Invalid Syntax. Type --help for more options.")
                en = False
        if n == "--run":
            runf = True
except:
    pass

if startf:
    if en:
        system.start()

if runf:
    if en:
        thread0 = threading.Thread(target=main)
        thread1 = threading.Thread(target=menu.handler)
        thread0.start()
        thread1.start()