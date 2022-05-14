import psutil
import time
import sys
import pytools

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

def getFile(path):
    error = 0
    try:
        file = open(path, "r")
        jsonData = file.read()
        file.close()
    except:
        print("Unexpected error:", sys.exc_info())
        error = 1
    if error != 0:
        jsonData = error
    return jsonData

def saveFile(path, jsonData):
    error = 0
    try:
        file = open(path, "w")
        file.write(jsonData)
        file.close()
    except:
        print("Unexpected error:", sys.exc_info())
        error = 1
    return error

def getProcesses():
    window = []
    clock = []
    fireplace = []
    outside = []
    windown = []
    windownI = 0
    outsideI = 0
    windowI = 0
    clockI = 0
    fireplaceI = 0
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.cmdline()
            if processName == "window.exe":
                windowI = windowI + 1
                window.append(processID)
            if processName == "clock.exe":
                clockI = clockI + 1
                clock.append(processID)
            if processName == "fireplace.exe":
                fireplaceI = fireplaceI + 1
                fireplace.append(processID)
            if processName == "outside.exe":
                outsideI = outsideI + 1
                outside.append(processID)
            if processName == "windown.exe":
                windownI = windownI + 1
                windown.append(processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return [clock, fireplace, window, outside, windown]

def main():
    while True:
        clocksounds = ""
        windowsounds = ""
        firesounds = ""
        outsidesounds = ""
        windownsounds = ""
        processes = getProcesses()
        # print(processes)
        i = 0
        try:
            while i < len(processes[0][0]):
                # print(processes[0][0][i])
                if processes[0][0][i] != "clock.exe":
                    if processes[0][0][i] != "runaudio.vbs":
                        if (processes[0][0][i].find(".vbs") != -1) or (processes[0][0][i].find(".mp3") != -1):
                            clocksounds = clocksounds + "\n       = " + processes[0][0][i].replace(".vbs", "").replace(".mp3", "").replace("_", " ")
                i = i + 1
        except:
            pass
        i = 0
        try:
            while i < len(processes[1][0]):
                print(processes[1][0][i])
                # print(processes[1][0][i])
                if processes[1][0][i] != "fireplace.exe":
                    if processes[1][0][i] != "runaudio.vbs":
                        if (processes[1][0][i].find(".vbs") != -1) or (processes[1][0][i].find(".mp3") != -1):
                            firesounds = firesounds + "\n       = " + processes[1][0][i].replace(".vbs", "").replace(".mp3", "").replace("_", " ")
                i = i + 1
        except:
            pass
        i = 0
        try:
            while i < len(processes[2][0]):
                # print(processes[2][0][i])
                if processes[2][0][i] != "window.exe":
                    if processes[2][0][i] != "runaudio.vbs":
                        if (processes[2][0][i].find(".vbs") != -1) or (processes[2][0][i].find(".mp3") != -1):
                            windowsounds = windowsounds + "\n       = " + processes[2][0][i].replace(".vbs", "").replace(".mp3", "").replace("_", " ")
                i = i + 1
        except:
            pass
            
        i = 0
        try:
            while i < len(processes[3][0]):
                # print(processes[2][0][i])
                if processes[3][0][i] != "outside.exe":
                    if processes[3][0][i] != "runaudio.vbs":
                        if (processes[3][0][i].find(".vbs") != -1) or (processes[3][0][i].find(".mp3") != -1):
                            outsidesounds = outsidesounds + "\n       = " + processes[3][0][i].replace(".vbs", "").replace(".mp3", "").replace("_", " ")
                i = i + 1
        except:
            pass
        
        i = 0
        try:
            while i < len(processes[4][0]):
                # print(processes[2][0][i])
                if processes[4][0][i] != "windown.exe":
                    if processes[4][0][i] != "runaudio.vbs":
                        if (processes[4][0][i].find(".vbs") != -1) or (processes[4][0][i].find(".mp3") != -1):
                            windownsounds = windownsounds + "\n       = " + processes[4][0][i].replace(".vbs", "").replace(".mp3", "").replace("_", " ")
                i = i + 1
        except:
            pass

        saveFile("..\\vars\\sounds\\clock.cxl", clocksounds)
        saveFile("..\\vars\\sounds\\fireplace.cxl", firesounds)
        saveFile("..\\vars\\sounds\\window.cxl", windowsounds + windownsounds)
        saveFile("..\\vars\\sounds\\outside.cxl", outsidesounds + windownsounds)
        time.sleep(1)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()
    
                