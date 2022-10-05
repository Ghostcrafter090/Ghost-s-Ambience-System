from datetime import datetime
import json
import random
import os
import sys
import threading
import time
import pytools

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": [],
        "heavenIndex": 0
    }

def getFile(path):
    error = 0
    try:
        file = open(path, "r")
        jsonData = file.read()
        file.close()
    except:
        # print("Unexpected error:", sys.exc_info())
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
        print("Unexpected error (fuck me):", sys.exc_info())
        error = 1
    return error

def getDateTime():
    daten = datetime.now()
    dateArray = [1970, 1, 1, 0, 0, 0]
    dateArray[0] = int(str(daten).split(" ")[0].split("-")[0])
    dateArray[1] = int(str(daten).split(" ")[0].split("-")[1])
    dateArray[2] = int(str(daten).split(" ")[0].split("-")[2])
    dateArray[3] = int(str(daten).split(" ")[1].split(":")[0])
    dateArray[4] = int(str(daten).split(" ")[1].split(":")[1])
    dateArray[5] = int(str(daten).split(" ")[1].split(":")[2].split(".")[0])
    return dateArray
    
def playSound(path, speaker, volume, speed, balence, waitBool):
    if speaker == 0:
        speakern = ["clock.exe"]
    elif speaker == 1:
        speakern = ["fireplace.exe"]
    elif speaker == 2:
        speakern = ["window.exe"]
    elif speaker == 3:
        speakern = ["outside.exe"]
    else:
        speakern = ["windown.exe"]
    if waitBool == 0:
        for n in speakern:
            os.system('cmd.exe /c start /b "" ' + n + ' runaudio.vbs ' + path + ' ' + str(volume) + ' ' + str(balence) + ' ' + str(speed) + ' ' + path.split(".")[0])
            print("Playing sound " + path + " on speaker " + n + " with volume " + str(volume) + " with speed of " + str(speed) + " with balence of " + str(balence) + "...")
    else:
        i = 0
        while i < len(speakern):
            if i == (len(speakern) - 1):
                os.system('cmd.exe /c start /b /wait "" ' + speakern[i] + ' runaudio.vbs ' + path + ' ' + str(volume) + ' ' + str(balence) + ' ' + str(speed) + ' ' + path.split(".")[0])
                print("Playing sound " + path + " on speaker " + speakern[i] + " with volume " + str(volume) + " with speed of " + str(speed) + " with balence of " + str(balence) + ". Waiting...")
            else:
                os.system('cmd.exe /c start /b "" ' + speakern[i] + ' runaudio.vbs ' + path + ' ' + str(volume) + ' ' + str(balence) + ' ' + str(speed) + ' ' + path.split(".")[0])
                print("Playing sound " + path + " on speaker " + speakern[i] + " with volume " + str(volume) + " with speed of " + str(speed) + " with balence of " + str(balence) + ". Waiting...")
            i = i + 1

def dayTic(dateArray):
    tic = (dateArray[3] * 60 * 60) + (dateArray[4] * 60) + dateArray[5]
    return tic

def closetosixTest(dateArray, hour, day, minute, noA):
    if dateArray[3] == hour:
        if dateArray[2] > day:
            if dateArray[4] == minute:
                if noA != 1:
                    playSound('closetomidnight.mp3', 0, 40, 1, 0, 0)
                    playSound('closetomidnight.mp3', 1, 40, 1, 0, 0)
                    playSound('closetomidnight.mp3', 2, 40, 1, 0, 0)
                    noA = 1
            else:
                noA = 0
        else:
            noA = 0
    else:
        noA = 0
    return noA
    
def doNull(val):
    return val

def detBellCurve(base, amp, span, pos, tic):
    c = 1 / (10000 * span)
    return amp * (base ** (-c * ((tic - pos) ** 2)))

def getDayTic(dateArray):
    if dateArray[1] == 11:
        out = (30 - dateArray[2]) + 25
    elif dateArray[1] == 12:
        out = 25 - dateArray[2]
    else:
        out = 1000
    if out < 1:
        out = 1
    return out

def getOutStatus():
    out = 0
    if os.path.isfile('nomufflewn.derp') == True:
        out = 1
    return out

def sn(*args):
    string = ""
    for x in args:
        string += x
    print(str(string))
    exec(str(string))
    exit()

def main():
    ticOld = 0
    santaLandingDate = -1
    mmcbellsn = -1
    pmch = -1
    while True:
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        dateArray = getDateTime()
        error = 1
        tic = dayTic(dateArray)
        while error == 1:
            try:
                dayTimes = pytools.IO.getList("daytimes.pyl")[1]
                sunJson = {
                    "ceth": dayTimes[6][3],
                    "cetm": dayTimes[6][4],
                    "csth": dayTimes[3][3],
                    "cstm": dayTimes[3][4],
                    "cesth": dayTimes[5][3],
                    "cestm": dayTimes[5][4]
                }
                # sunJson = json.loads(("{\"" + getFile('daytimes.cmd').replace("set ", "").replace("\n", "\", \"").replace("=", "\": \"") + "}").replace(", \"}", "}").replace(" \",", "\",").replace(" \"}", "\"}"))
                # doNull(sunJson['ceth'])
                # doNull(sunJson['cetm'])
                # doNull(sunJson['csth'])
                # doNull(sunJson['cstm'])
                # doNull(sunJson['cesth'])
                # doNull(sunJson['cestm'])
                error = 0
            except:
                error = 1
        if dateArray[1] > 10:
            if ((dateArray[1] == 11) and (dateArray[2] > 11)) or (dateArray[1] == 12):
                # noA = closetosixTest(dateArray, 6, 9, 10, noA)
                # noB = closetosixTest(dateArray, 5, 14, 13, noB)
                # noC = closetosixTest(dateArray, 4, 19, 33, noC)
                # noD = closetosixTest(dateArray, 3, 24, 48, noD)
                minZ = (int(sunJson['cetm']) + 30)
                hourZ = (int(sunJson['ceth']))
                if minZ < 0:
                    minZ = minZ + 60
                    hourZ = hourZ - 1
                
                bellsChance = 0
                bellsChance = detBellCurve(2, 1900, 10800, 54000, tic) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < bellsChance:
                    playSound('sleighbells_' + str(random.randrange(0, 5)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)

                outsideBandChance = 0
                outsideBandChance = detBellCurve(2, 1900, 7800, 43200, tic) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < outsideBandChance:
                    if int(sunJson['ceth']) > dateArray[3]:
                        if int(sunJson['csth']) < dateArray[3]:
                            if getOutStatus() == 1:
                                n = 'playSound("outside_band.mp3", 0, 20, 1, 0, 0)'
                                th1 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_band.mp3", 1, 20, 1, 0, 0)'
                                th2 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_band_nm.mp3", 4, 20, 1, 0, 0)'
                                th3 = threading.Thread(target=sn, args=n)

                                th1.start()
                                th2.start()
                                th3.start()

                                th1.join()
                                th2.join()
                                th3.join()
                            else:
                                n = 'playSound("outside_band.mp3", 0, 10, 1, 0, 0)'
                                th1 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_band.mp3", 1, 10, 1, 0, 0)'
                                th2 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_band_nm.mp3", 3, 10, 1, 0, 0)'
                                th3 = threading.Thrjead(target=sn, args=n)
                                n = 'playSound("outside_band_wn.mp3", 2, 10, 1, 0, 0)'
                                th4 = threading.Thread(target=sn, args=n)

                                th1.start()
                                th2.start()
                                th3.start()
                                th4.start()

                                th1.join()
                                th2.join()
                                th3.join()
                                th4.join()

                outsideBellsChance = 0
                outsideBellsChance = detBellCurve(2, 1900, 8800, 39600, tic) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < outsideBellsChance:
                    if int(sunJson['ceth']) > dateArray[3]:
                        if int(sunJson['csth']) < dateArray[3]:
                            if getOutStatus() == 1:
                                n = 'playSound("outside_bells.mp3", 0, 10, 1, 0, 0)'
                                th1 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_bells.mp3", 1, 10, 1, 0, 0)'
                                th2 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_bells_nm.mp3", 4, 10, 1, 0, 0)'
                                th3 = threading.Thread(target=sn, args=n)

                                th1.start()
                                th2.start()
                                th3.start()

                                th1.join()
                                th2.join()
                                th3.join()
                            else:
                                n = 'playSound("outside_bells.mp3", 0, 10, 1, 0, 0)'
                                th1 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_bells.mp3", 1, 10, 1, 0, 0)'
                                th2 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_bells_nm.mp3", 3, 10, 1, 0, 0)'
                                th3 = threading.Thread(target=sn, args=n)
                                n = 'playSound("outside_bells_wn.mp3", 2, 10, 1, 0, 0)'
                                th4 = threading.Thread(target=sn, args=n)

                                th1.start()
                                th2.start()
                                th3.start()
                                th4.start()

                                th1.join()
                                th2.join()
                                th3.join()
                                th4.join()

                musicBoxChance = 0
                musicBoxChance = detBellCurve(2, 1900, 8800, 72000, tic) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < musicBoxChance:
                    if random.randrange(0, 2) == 1:
                        playSound("jinglebells_mb.mp3", random.randrange(0, 3), 5, 1, 0, 0)
                    else:
                        playSound("merrychristmas_mb.mp3", random.randrange(0, 3), 5, 1, 0, 0)

                if dateArray[3] == 3:
                    if dateArray[4] == 5:
                        if random.randrange(0, getDayTic(dateArray)) < 3:
                            if ambells != dateArray[2]:
                                ambells = dateArray[2]
                                n = 'playSound("3am_bells.mp3", 0, 5, 1, 0, 0)'
                                th1 = threading.Thread(target=sn, args=n)
                                n = 'playSound("3am_bells.mp3", 1, 5, 1, 0, 0)'
                                th2 = threading.Thread(target=sn, args=n)
                                n = 'playSound("3am_bells.mp3", 4, 5, 1, 0, 0)'
                                th3 = threading.Thread(target=sn, args=n)

                                th1.start()
                                th2.start()
                                th3.start()

                                th1.join()
                                th2.join()
                                th3.join()

                if dateArray[3] == 18:
                    if dateArray[4] == 10:
                        if dateArray[2] != pmch:
                            pmch = dateArray[2]
                            n = 'playSound("6pm_ch.mp3", 0, 15, 1, 0, 0)'
                            th1 = threading.Thread(target=sn, args=n)
                            n = 'playSound("6pm_ch.mp3", 1, 15, 1, 0, 0)'
                            th2 = threading.Thread(target=sn, args=n)
                            n = 'playSound("6pm_ch.mp3", 4, 15, 1, 0, 0)'
                            th3 = threading.Thread(target=sn, args=n)

                            th1.start()
                            th2.start()
                            th3.start()

                            th1.join()
                            th2.join()
                            th3.join()
                
                lateNightChoirChance = 0
                lateNightChoirChance = detBellCurve(2, 1900, 7200, 10800, tic) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < lateNightChoirChance:
                    n = 'playSound("latenight_choir.mp3", 0, 10, 1, 0, 0)'
                    th1 = threading.Thread(target=sn, args=n)
                    n = 'playSound("latenight_choir.mp3", 1, 10, 1, 0, 0)'
                    th2 = threading.Thread(target=sn, args=n)
                    n = 'playSound("latenight_choir.mp3", 4, 10, 1, 0, 0)'
                    th3 = threading.Thread(target=sn, args=n)

                    th1.start()
                    th2.start()
                    th3.start()

                    th1.join()
                    th2.join()
                    th3.join()
                    

                lateDayBellsChance = 0
                lateDayBellsChance = (detBellCurve(2, 1900, 7200, 82800, tic) + detBellCurve(2, 1900, 7200, 25200, tic)) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < lateDayBellsChance:
                    n = 'playSound("lateday_bells.mp3", 0, 10, 1, 0, 0)'
                    th1 = threading.Thread(target=sn, args=n)
                    n = 'playSound("lateday_bells.mp3", 1, 10, 1, 0, 0)'
                    th2 = threading.Thread(target=sn, args=n)
                    n = 'playSound("lateday_bells.mp3", 4, 10, 1, 0, 0)'
                    th3 = threading.Thread(target=sn, args=n)

                    th1.start()
                    th2.start()
                    th3.start()

                    th1.join()
                    th2.join()
                    th3.join()

                if dateArray[3] == 21:
                    if dateArray[4] == 23:
                        if random.randrange(0, getDayTic(dateArray)) < 5:
                            if getDayTic(dateArray) > 2:
                                if mmcbellsn != dateArray[2]:
                                    mmcbellsn = dateArray[2]
                                    n = 'playSound("mmcbells.mp3", 0, 100, 1, 0, 0)'
                                    th1 = threading.Thread(target=sn, args=n)
                                    n = 'playSound("mmcbells.mp3", 1, 100, 1, 0, 0)'
                                    th2 = threading.Thread(target=sn, args=n)
                                    n = 'playSound("mmcbells.mp3", 2, 100, 1, 0, 0)'
                                    th3 = threading.Thread(target=sn, args=n)

                                    th1.start()
                                    th2.start()
                                    th3.start()

                                    th1.join()
                                    th2.join()
                                    th3.join()
                
                mmcidleChance = 0
                mmcidleChance = detBellCurve(2, 1900, 12600, 43200, tic) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < mmcidleChance:
                    playSound("mmcidle.mp3", 2, 20, 1, 0, 0)
                
                santaLandingChance = 0
                santaLandingChance = detBellCurve(2, 1900, 3600, 10800, tic) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < santaLandingChance:
                    if santaLandingDate != dateArray[2]:
                        santaLandingDate = dateArray[2]
                        if getOutStatus() == 1:
                            n = 'playSound("santalanding.mp3", 0, 10, 1, 0, 0)'
                            th1 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding.mp3", 1, 10, 1, 0, 0)'
                            th2 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding_nm.mp3", 4, 10, 1, 0, 0)'
                            th3 = threading.Thread(target=sn, args=n)

                            th1.start()
                            th2.start()
                            th3.start()

                            th1.join()
                            th2.join()
                            th3.join()
                        else:
                            n = 'playSound("santalanding.mp3", 0, 10, 1, 0, 0)'
                            th1 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding.mp3", 1, 10, 1, 0, 0)'
                            th2 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding_nm.mp3", 3, 10, 1, 0, 0)'
                            th3 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding_wn.mp3", 2, 10, 1, 0, 0)'
                            th4 = threading.Thread(target=sn, args=n)

                            th1.start()
                            th2.start()
                            th3.start()
                            th4.start()

                            th1.join()
                            th2.join()
                            th3.join()
                            th4.join()
                
                if dateArray[3] > 4:
                    if santaLandingDate != dateArray[2]:
                        santaLandingDate = dateArray[2]
                        if getOutStatus() == 1:
                            n = 'playSound("santalanding.mp3", 0, 10, 1, 0, 0)'
                            th1 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding.mp3", 1, 10, 1, 0, 0)'
                            th2 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding_nm.mp3", 4, 10, 1, 0, 0)'
                            th3 = threading.Thread(target=sn, args=n)

                            th1.start()
                            th2.start()
                            th3.start()

                            th1.join()
                            th2.join()
                            th3.join()
                        else:
                            n = 'playSound("santalanding.mp3", 0, 10, 1, 0, 0)'
                            th1 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding.mp3", 1, 10, 1, 0, 0)'
                            th2 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding_nm.mp3", 3, 10, 1, 0, 0)'
                            th3 = threading.Thread(target=sn, args=n)
                            n = 'playSound("santalanding_wn.mp3", 2, 10, 1, 0, 0)'
                            th4 = threading.Thread(target=sn, args=n)

                            th1.start()
                            th2.start()
                            th3.start()
                            th4.start()

                            th1.join()
                            th2.join()
                            th3.join()
                            th4.join()

                sleighPassingChance = 0
                sleighPassingChance = detBellCurve(2, 1900, 3600, 10800, tic) / (getDayTic(dateArray) * 1.5)
                if random.randrange(0, 100000000) < sleighPassingChance:
                    if santaLandingDate != dateArray[2]:
                        if getOutStatus() == 1:
                            n = 'playSound("sleigh_passing.mp3", 0, 10, 1, 0, 0)'
                            th1 = threading.Thread(target=sn, args=n)
                            n = 'playSound("sleigh_passing.mp3", 1, 10, 1, 0, 0)'
                            th2 = threading.Thread(target=sn, args=n)
                            n = 'playSound("sleigh_passing_nm.mp3", 4, 10, 1, 0, 0)'
                            th3 = threading.Thread(target=sn, args=n)

                            th1.start()
                            th2.start()
                            th3.start()

                            th1.join()
                            th2.join()
                            th3.join()
                        else:
                            n = 'playSound("sleigh_passing.mp3", 0, 10, 1, 0, 0)'
                            th1 = threading.Thread(target=sn, args=n)
                            n = 'playSound("sleigh_passing.mp3", 1, 10, 1, 0, 0)'
                            th2 = threading.Thread(target=sn, args=n)
                            n = 'playSound("sleigh_passing_nm.mp3", 3, 10, 1, 0, 0)'
                            th3 = threading.Thread(target=sn, args=n)
                            n = 'playSound("sleigh_passing_wn.mp3", 2, 10, 1, 0, 0)'
                            th4 = threading.Thread(target=sn, args=n)

                            th1.start()
                            th2.start()
                            th3.start()
                            th4.start()

                            th1.join()
                            th2.join()
                            th3.join()
                            th4.join()
                
                if tic != ticOld:
                    ticOld = tic
                    heavenIndex = bellsChance + outsideBandChance + outsideBellsChance + musicBoxChance + lateNightChoirChance + lateDayBellsChance + mmcidleChance + santaLandingChance + sleighPassingChance
                    print("Heaven Index: " + str(heavenIndex) + "Hi")
                    status.vars['heavenIndex'] = heavenIndex
                    saveFile('heavenindex.cx', str(heavenIndex))
        status.finishedLoop = True

def run():           
    main()
                        
            
            
            
            
                        
                    
                        
            
                    
                    
                
            
            
                    