from datetime import datetime
import json
import random
import os
import sys

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
                    playSound('death_ghost_' + str(random.randrange(0, 2)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
        elif dateArray[3] > hourZ:
            deathGhostChance = 0
            if dateArray[3] < (24):
                deathGhostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                deathGhostChance = deathGhostChance / (32 - dateArray[2])
            if random.randrange(0, 500000000) < deathGhostChance:
                playSound('death_ghost_' + str(random.randrange(0, 2)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
    if dateArray[2] > 19:
        if dateArray[3] >= hourZ:
            if dateArray[4] >= minZ:
                dyingGhostChance = 0
                if dateArray[3] < (24):
                    dyingGhostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                    dyingGhostChance = dyingGhostChance / (32 - dateArray[2])
                if random.randrange(0, 500000000) < dyingGhostChance:
                    playSound('dying_ghost_' + str(random.randrange(0, 3)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
        elif dateArray[3] > hourZ:
            dyingGhostChance = 0
            if dateArray[3] < (24):
                dyingGhostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                dyingGhostChance = dyingGhostChance / (32 - dateArray[2])
            if random.randrange(0, 500000000) < dyingGhostChance:
                playSound('dying_ghost_' + str(random.randrange(0, 3)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
    if dateArray[2] > 9:
        if dateArray[3] >= hourZ:
            if dateArray[4] >= minZ:
                ghostChance = 0
                if dateArray[3] < (24):
                    ghostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                    ghostChance = ghostChance / (32 - dateArray[2])
                if random.randrange(0, 500000000) < ghostChance:
                    playSound('ghost_' + str(random.randrange(0, 2)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
        elif dateArray[3] > hourZ:
            ghostChance = 0
            if dateArray[3] < (24):
                ghostChance = (dateArray[3] - (int(hourZ))) * dateArray[4]
                ghostChance = ghostChance / (32 - dateArray[2])
            if random.randrange(0, 500000000) < ghostChance:
                playSound('ghost_' + str(random.randrange(0, 2)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
    return [deathGhostChance, dyingGhostChance, ghostChance]

def main():
    noA = 0
    noB = 0
    noC = 0
    noD = 0
    noE = 0
    noF = 0
    noG = 0
    prevMin = 0
    ghostsChance = [0, 0, 0]
    while True:
        dateArray = getDateTime()
        error = 1
        while error == 1:
            try:
                sunJson = json.loads(("{\"" + getFile('daytimes.cmd').replace("set ", "").replace("\n", "\", \"").replace("=", "\": \"") + "}").replace(", \"}", "}").replace(" \",", "\",").replace(" \"}", "\"}"))
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
                playSound('draft_' + str(random.randrange(0, 3)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
            
            breathChance = 0
            if dateArray[3] < (int(sunJson['csth'])):
                breathChance = ((int(sunJson['csth'])) - dateArray[3]) * dateArray[4]
            breathChance = breathChance / (32 - dateArray[2])
            if random.randrange(0, 100000000) < breathChance:
                playSound('h_breath_' + str(random.randrange(0, 4)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
            
            moodChance = 0
            if os.path.isfile('halloweenmode.derp') == True:
                if prevMin != dateArray[4]:
                    playSound('h_general.mp3', 0, 25, 1, 0, 0)
                    playSound('h_general.mp3', 1, 25, 1, 0, 0)
                    playSound('h_general.mp3', 2, 25, 1, 0, 0)
                    prevMin = dateArray[4]
                moodChance = 0
                if dateArray[3] < 24:
                    moodChance = (dateArray[3] - (int(sunJson['cesth']))) * dateArray[4]
                if dateArray[3] < (int(sunJson['csth'])):
                    moodChance = ((int(sunJson['csth'])) - dateArray[3]) * dateArray[4]
                if random.randrange(0, 100000000) < moodChance:
                    playSound('h_general_mood.mp3', 0, 40, 1, 0, 0)
                    playSound('h_general_mood.mp3', 1, 40, 1, 0, 0)
                    playSound('h_general_mood.mp3', 2, 40, 1, 0, 0)
                    
            knockChance = 0
            if dateArray[3] < 24:
                knockChance = (dateArray[3] - (int(sunJson['cesth']))) * dateArray[4]
            knockChance = knockChance / (32 - dateArray[2])
            if random.randrange(0, 60000000) < knockChance:
                playSound('h_knock_' + str(random.randrange(0, 6)) + ".mp3", random.randrange(0, 3), 40, 1, 0, 0)
                
            if dateArray[2] > 19:
                if dateArray[4] == 35:
                    if noE != 1:
                        if random.randrange(dateArray[3], 24) == 23:
                            playSound('h_rumble.mp3', 0, 40, 1, 0, 0)
                            playSound('h_rumble.mp3', 1, 40, 1, 0, 0)
                            playSound('h_rumble.mp3', 2, 40, 1, 0, 0)
                        noE = 1
                else:
                    noE = 0
            else:
                noE = 0
            
            if dateArray[2] > 24:
                if dateArray[4] == 20:
                    if noF != 1:
                        if random.randrange(dateArray[3], 24) == 23:
                            playSound('h_rumble.mp3', 0, 40, 1, 0, 0)
                            playSound('h_rumble.mp3', 1, 40, 1, 0, 0)
                            playSound('h_rumble.mp3', 2, 40, 1, 0, 0)
                        noF = 1
                elif dateArray[4] == 40:
                    if noF != 1:
                        if random.randrange(dateArray[3], 24) == 23:
                            playSound('h_rumble.mp3', 0, 40, 1, 0, 0)
                            playSound('h_rumble.mp3', 1, 40, 1, 0, 0)
                            playSound('h_rumble.mp3', 2, 40, 1, 0, 0)
                        noF = 1
                else:
                    noF = 0
            else:
                noF = 0
            
            if dateArray[3] == int(sunJson['cesth']):
                if dateArray[4] == int(sunJson['cestm']):
                    if noG != 1:
                        if random.randrange(dateArray[2], 32) == 31:
                            playSound('h_sunset.mp3', 2, 40, 1, 0, 0)
                        noG = 1
                else:
                    noG = 0
            else:
                noG = 0
            
            if breathChance < 0:
                breathChance = 0
            horrorIndex = ghostsChance[0] + ghostsChance[1] + ghostsChance[2] + draftChance + breathChance + moodChance + knockChance
            saveFile('horrorindex.cx', str(horrorIndex))

def run():       
    main()
                        
            
            
            
            
                        
                    
                        
            
                    
                    
                
            
            
                    