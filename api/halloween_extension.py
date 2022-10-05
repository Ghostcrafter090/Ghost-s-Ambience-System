from datetime import datetime
import json
import random
import os
import sys
import pytools

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": [],
        "horrorIndex": 0,
        "horrorStats": {
            "ghostsChance-0": 0,
            "ghostsChance-1": 0,
            "ghostsChance-2": 0,
            "draftChance": 0,
            "breathChance": 0,
            "moodChance": 0,
            "knockChance": 0
        }
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
        speakern = "clock.exe"
    elif speaker == 1:
        speakern = "fireplace.exe"
    else:
        speakern = "windown.exe"
    if waitBool == 0:
        os.system('cmd.exe /c start /b "" ' + speakern + ' runaudio.vbs ' + path + ' ' + str(volume) + ' ' + str(balence) + ' ' + str(speed) + ' ' + path.split(".")[0])
        print("Playing sound " + path + " on speaker " + speakern + " with volume " + str(volume) + " with speed of " + str(speed) + " with balence of " + str(balence) + "...")
    else:
        os.system('cmd.exe /c start /b /wait "" ' + speakern + ' runaudio.vbs ' + path + ' ' + str(volume) + ' ' + str(balence) + ' ' + str(speed) + ' ' + path.split(".")[0])
        print("Playing sound " + path + " on speaker " + speakern + " with volume " + str(volume) + " with speed of " + str(speed) + " with balence of " + str(balence) + ". Waiting...")

def closetomidTest(dateArray, hour, day, minute, noA):
    if dateArray[3] == hour:
        if dateArray[2] > day:
            if dateArray[4] == minute:
                if noA != 1:
                    pytools.sound.main.playSoundAll('closetomidnight.mp3', 40, 1, 0, 0)
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

def testGhosts(hourZ, minZ, dateArray):
    deathGhostChance = 0
    dyingGhostChance = 0
    ghostChance = 0
    if dateArray[2] > 24:
        if dateArray[3] >= hourZ:
            if dateArray[4] >= minZ:
                deathGhostChance = 0
                if dateArray[3] < (24):
                    deathGhostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                    deathGhostChance = deathGhostChance / (32 - dateArray[2])
                if random.randrange(0, 500000000) < deathGhostChance:
                    ghSpeaker = 5
                    while ghSpeaker == 5:
                        ghSpeaker = random.randrange(0, 8)
                    pytools.sound.main.playSound('death_ghost_' + str(random.randrange(0, 2)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
        elif dateArray[3] > hourZ:
            deathGhostChance = 0
            if dateArray[3] < (24):
                deathGhostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                deathGhostChance = deathGhostChance / (32 - dateArray[2])
            if random.randrange(0, 500000000) < deathGhostChance:
                ghSpeaker = 5
                while ghSpeaker == 5:
                    ghSpeaker = random.randrange(0, 8)
                pytools.sound.main.playSound('death_ghost_' + str(random.randrange(0, 2)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
    if dateArray[2] > 19:
        if dateArray[3] >= hourZ:
            if dateArray[4] >= minZ:
                dyingGhostChance = 0
                if dateArray[3] < (24):
                    dyingGhostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                    dyingGhostChance = dyingGhostChance / (32 - dateArray[2])
                if random.randrange(0, 500000000) < dyingGhostChance:
                    ghSpeaker = 5
                    while ghSpeaker == 5:
                        ghSpeaker = random.randrange(0, 8)
                    pytools.sound.main.playSound('dying_ghost_' + str(random.randrange(0, 3)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
        elif dateArray[3] > hourZ:
            dyingGhostChance = 0
            if dateArray[3] < (24):
                dyingGhostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                dyingGhostChance = dyingGhostChance / (32 - dateArray[2])
            if random.randrange(0, 500000000) < dyingGhostChance:
                ghSpeaker = 5
                while ghSpeaker == 5:
                    ghSpeaker = random.randrange(0, 8)
                pytools.sound.main.playSound('dying_ghost_' + str(random.randrange(0, 3)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
    if dateArray[2] > 9:
        if dateArray[3] >= hourZ:
            if dateArray[4] >= minZ:
                ghostChance = 0
                if dateArray[3] < (24):
                    ghostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                    ghostChance = ghostChance / (32 - dateArray[2])
                if random.randrange(0, 500000000) < ghostChance:
                    ghSpeaker = 5
                    while ghSpeaker == 5:
                        ghSpeaker = random.randrange(0, 8)
                    pytools.sound.main.playSound('ghost_' + str(random.randrange(0, 2)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
        elif dateArray[3] > hourZ:
            ghostChance = 0
            if dateArray[3] < (24):
                ghostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                ghostChance = ghostChance / (32 - dateArray[2])
            if random.randrange(0, 500000000) < ghostChance:
                ghSpeaker = 5
                while ghSpeaker == 5:
                    ghSpeaker = random.randrange(0, 8)
                pytools.sound.main.playSound('ghost_' + str(random.randrange(0, 2)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
    return [deathGhostChance, dyingGhostChance, ghostChance]

def main():
    noA = 0
    noB = 0
    noC = 0
    noD = 0
    pHorr = False
    noE = 0
    noF = 0
    noG = 0
    prevMin = 0
    ghostsChance = [0, 0, 0]
    while True:
        dateArray = pytools.clock.getDateTime()
        error = 1
        while error == 1:
            try:
                dayTimes = pytools.IO.getList("daytimes.pyl")[1]
                sunJson = {
                    "ceth": dayTimes[6][3],
                    "cetm": dayTimes[6][4],
                    "csth": dayTimes[2][3],
                    "cstm": dayTimes[2][4],
                    "cesth": dayTimes[5][3],
                    "cestm": dayTimes[5][4]
                }
                # sunJson = json.loads(("{\"" + getFile('daytimes.cmd').replace("set ", "").replace("\n", "\", \"").replace("=", "\": \"") + "}").replace(", \"}", "}").replace(" \",", "\",").replace(" \"}", "\"}"))
                doNull(sunJson['ceth'])
                doNull(sunJson['cetm'])
                doNull(sunJson['csth'])
                doNull(sunJson['cstm'])
                doNull(sunJson['cesth'])
                doNull(sunJson['cestm'])
                error = 0
            except:
                error = 1
            
        if dateArray[1] == 10:
            noA = closetomidTest(dateArray, 23, 25, 10, noA)
            noB = closetomidTest(dateArray, 23, 20, 15, noB)
            noC = closetomidTest(dateArray, 23, 15, 30, noC)
            noD = closetomidTest(dateArray, 23, 10, 45, noD)
            minZ = (int(sunJson['cetm']) + 30)
            hourZ = (int(sunJson['ceth']))
            if minZ < 0:
                minZ = minZ + 60
                hourZ = hourZ - 1
            
            ghostsChance = testGhosts(hourZ, minZ, dateArray)
            
            draftChance = 0
            if dateArray[3] < 24:
                draftChance = (dateArray[3] - (int(sunJson['cesth']))) * dateArray[4]
            if dateArray[3] < (int(sunJson['csth'])):
                draftChance = ((int(sunJson['csth'])) - dateArray[3]) * dateArray[4]
            if random.randrange(0, 100000000) < draftChance:
                ghSpeaker = 5
                while ghSpeaker == 5:
                    ghSpeaker = random.randrange(0, 8)
                pytools.sound.main.playSound('draft_' + str(random.randrange(0, 3)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
            
            breathChance = 0
            if dateArray[3] < (int(sunJson['csth'])):
                breathChance = ((int(sunJson['csth'])) - dateArray[3]) * dateArray[4]
            breathChance = breathChance / (32 - dateArray[2])
            if random.randrange(0, 100000000) < breathChance:
                ghSpeaker = 5
                while ghSpeaker == 5:
                    ghSpeaker = random.randrange(0, 8)
                pytools.sound.main.playSound('h_breath_' + str(random.randrange(0, 4)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
            
            moodChance = 0
            if os.path.isfile('halloweenmode.derp') == True:
                if prevMin != dateArray[4]:
                    monthS = pytools.clock.dateArrayToUTC([dateArray[0], 10, 1, 0, 0, 0])
                    monthE = pytools.clock.dateArrayToUTC([dateArray[0], 11, 1, 0, 0, 0])
                    monthC = pytools.clock.dateArrayToUTC(dateArray) - monthS
                    
                    hGeneralVol = 42 * (monthC / (monthE - monthS))
                    if hGeneralVol > 35:
                        hGeneralVol = 35
                    hGeneralSpeedModifier = 0.08
                    midnight = pytools.clock.dateArrayToUTC(pytools.clock.getMidnight(dateArray))
                    sunset = pytools.clock.dateArrayToUTC(dayTimes[5])
                    civil = pytools.clock.dateArrayToUTC(dayTimes[2])
                    sunrise = pytools.clock.dateArrayToUTC(dayTimes[3])
                    current = pytools.clock.dateArrayToUTC(dateArray)
                    try:
                        if current > sunset:
                            hGeneralSpeedModifier = 0.08 * (((midnight - sunset) - (midnight - current)) / (midnight - sunset))
                        elif (midnight - current) > 82800:
                            hGeneralSpeedModifier = 0.08 * (1 - ((midnight - current - 83160) / 3600))
                        elif current < civil:
                            hGeneralSpeedModifier = 0.1
                        elif current < sunrise:
                            hGeneralSpeedModifier =  0.1 * (((sunrise - civil) / ((sunrise - civil + 1) - (sunrise - current))) - 1)
                        else:
                            hGeneralSpeedModifier = 0
                    except:
                        pass
                    if hGeneralSpeedModifier > 0.4:
                        hGeneralSpeedModifier = 0.4
                    elif hGeneralSpeedModifier < 0:
                        hGeneralSpeedModifier = 0
                    hGeneralSpeedModifier = hGeneralSpeedModifier * (monthC / (monthE - monthS))
                    pytools.sound.main.playSoundAll('h_general.mp3', hGeneralVol, 1 - hGeneralSpeedModifier, 0, 0)
                    prevMin = dateArray[4]
                moodChance = 0
                if dateArray[3] < 24:
                    moodChance = (dateArray[3] - (int(sunJson['cesth']))) * dateArray[4]
                if dateArray[3] < (int(sunJson['csth'])):
                    moodChance = ((int(sunJson['csth'])) - dateArray[3]) * dateArray[4]
                if random.randrange(0, 100000000) < moodChance:
                    pytools.sound.main.playSoundAll('h_general_mood.mp3', 40, 1, 0, 0)
                    
            knockChance = 0
            if dateArray[3] < 24:
                knockChance = (dateArray[3] - (int(sunJson['cesth']))) * dateArray[4]
            knockChance = knockChance / (32 - dateArray[2])
            if random.randrange(0, 60000000) < knockChance:
                ghSpeaker = 5
                while ghSpeaker == 5:
                    ghSpeaker = random.randrange(0, 8)
                pytools.sound.main.playSound('h_knock_' + str(random.randrange(0, 6)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
                
            if dateArray[2] > 19:
                if dateArray[4] == 35:
                    if noE != 1:
                        if random.randrange(dateArray[3], 24) == 23:
                            rumbleNum = random.randrange(0, 2)
                            pytools.sound.main.playSoundAll('h_rumble_' + str(rumbleNum) + '.mp3', 40, 1, 0, 0)
                        noE = 1
                else:
                    noE = 0
            else:
                noE = 0
            
            if dateArray[2] > 24:
                if dateArray[4] == 20:
                    if noF != 1:
                        if random.randrange(dateArray[3], 24) == 23:
                            rumbleNum = random.randrange(0, 2)
                            pytools.sound.main.playSoundAll('h_rumble_' + str(rumbleNum) + '.mp3', 40, 1, 0, 0)
                        noF = 1
                elif dateArray[4] == 40:
                    if noF != 1:
                        if random.randrange(dateArray[3], 24) == 23:
                            rumbleNum = random.randrange(0, 2)
                            pytools.sound.main.playSoundAll('h_rumble_' + str(rumbleNum) + '.mp3', 40, 1, 0, 0)
                        noF = 1
                else:
                    noF = 0
            else:
                noF = 0
            
            if dateArray[3] == int(sunJson['cesth']):
                if dateArray[4] == int(sunJson['cestm']):
                    if noG != 1:
                        if random.randrange(dateArray[2], 32) == 31:
                            pytools.sound.main.playSoundWindow('h_sunset.mp3;h_sunset.mp3', [40, 80], 1, 0, 0)
                        noG = 1
                else:
                    noG = 0
            else:
                noG = 0
            
            if breathChance < 0:
                breathChance = 0
            horrorIndex = ghostsChance[0] + ghostsChance[1] + ghostsChance[2] + draftChance + breathChance + moodChance + knockChance
            status.vars["horrorStats"]["ghostsChance-0"] = ghostsChance[0]
            status.vars["horrorStats"]["ghostsChance-1"] = ghostsChance[1]
            status.vars["horrorStats"]["ghostsChance-2"] = ghostsChance[2]
            status.vars["horrorStats"]["draftChance"] = draftChance
            status.vars["horrorStats"]["breathChance"] = breathChance
            status.vars["horrorStats"]["moodChance"] = moodChance
            status.vars["horrorStats"]["knockChance"] = knockChance
            
            if (dateArray[5] % 2) == 0:
                if pHorr == False:
                    print("Current Horror Index: " + str(horrorIndex))
                    status.vars['horrorIndex'] = horrorIndex
                    saveFile('horrorindex.cx', str(horrorIndex))
                    pHorr = True
            else:
                pHorr = False
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True


def run():       
    main()
                        
            
            
            
            
                        
                    
                        
            
                    
                    
                
            
            
                    