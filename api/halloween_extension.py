from datetime import datetime
import json
import random
import os
import sys
import pytools
import time
import threading

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": [],
        "horrorIndex": 0,
        "horrorStats": {
            "sections.ghostsChance-0": 0,
            "sections.ghostsChance-1": 0,
            "sections.ghostsChance-2": 0,
            "sections.draftChance": 0,
            "sections.breathChance": 0,
            "sections.moodChance": 0,
            "sections.knockChance": 0,
            "sections.chainChance": 0
        }
    }
    
class globals:
    run = False
    
class sunf:
    sunJson = {}
    dayTimes = []
    dateArray = []
    minZ = 0
    hourZ = 0
    
    def grab():
        while True:
            try:
                error = 1
                while error == 1:
                    try:
                        sunf.dayTimes = pytools.IO.getList("dayTimes.pyl")[1]
                        sunf.sunJson = {
                            "ceth": sunf.dayTimes[6][3],
                            "cetm": sunf.dayTimes[6][4],
                            "csth": sunf.dayTimes[2][3],
                            "cstm": sunf.dayTimes[2][4],
                            "cesth": sunf.dayTimes[5][3],
                            "cestm": sunf.dayTimes[5][4],
                            "neth": sunf.dayTimes[7][3],
                            "netm": sunf.dayTimes[7][4],
                            "aeth": sunf.dayTimes[8][3],
                            "aetm": sunf.dayTimes[8][4]
                        }
                        # sunf.sunJson = json.loads(("{\"" + getFile('sunf.dayTimes.cmd').replace("set ", "").replace("\n", "\", \"").replace("=", "\": \"") + "}").replace(", \"}", "}").replace(" \",", "\",").replace(" \"}", "\"}"))
                        doNull(sunf.sunJson['ceth'])
                        doNull(sunf.sunJson['cetm'])
                        doNull(sunf.sunJson['csth'])
                        doNull(sunf.sunJson['cstm'])
                        doNull(sunf.sunJson['cesth'])
                        doNull(sunf.sunJson['cestm'])
                        error = 0
                    except:
                        error = 1
            except:
                pass
            time.sleep(10)
    
    def getZ():
        error = True
        while error:
            try:
                dummy(sunf.sunJson['cetm'])
                error = False
            except:
                pass
        sunf.minZ = (int(sunf.sunJson['cetm']) + 30)
        sunf.hourZ = (int(sunf.sunJson['ceth']))
        if sunf.minZ < 0:
            sunf.minZ = sunf.minZ + 60
            sunf.hourZ = sunf.hourZ - 1

def dummy(var):
    pass

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
    sunf.dateArray = [1970, 1, 1, 0, 0, 0]
    sunf.dateArray[0] = int(str(daten).split(" ")[0].split("-")[0])
    sunf.dateArray[1] = int(str(daten).split(" ")[0].split("-")[1])
    sunf.dateArray[2] = int(str(daten).split(" ")[0].split("-")[2])
    sunf.dateArray[3] = int(str(daten).split(" ")[1].split(":")[0])
    sunf.dateArray[4] = int(str(daten).split(" ")[1].split(":")[1])
    sunf.dateArray[5] = int(str(daten).split(" ")[1].split(":")[2].split(".")[0])
    return sunf.dateArray
    
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
    if sunf.dateArray[3] == hour:
        if sunf.dateArray[2] > day:
            if sunf.dateArray[4] == minute:
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

class mainVars:
    noA = 0
    noB = 0
    noC = 0
    noD = 0

class sections:
    ghostsChance = [0, 0, 0]
    
    def testGhosts():
        ghostsChance = [0, 0, 0]
        while True:
            if globals.run:
                try:
                    deathGhostChance = 0
                    dyingGhostChance = 0
                    ghostChance = 0
                    if sunf.dateArray[2] > 24:
                        if sunf.dateArray[3] > sunf.hourZ:
                                deathGhostChance = (sunf.dateArray[3] - (int(sunf.hourZ + 2))) * sunf.dateArray[4]
                                deathGhostChance = deathGhostChance / (32 - sunf.dateArray[2])
                                if random.randrange(0, 37500) < (deathGhostChance / ((32 - sunf.dateArray[2]) / 3) + 1):
                                    ghSpeaker = 5
                                    while ghSpeaker == 5:
                                        ghSpeaker = random.randrange(0, 8)
                                    pytools.sound.main.playSound('death_ghost_' + str(random.randrange(0, 2)) + ".mp3", ghSpeaker, (0.5 + random.random()) * 40, 1, 0, 0)
                        elif sunf.dateArray[3] == sunf.hourZ:
                            if sunf.dateArray[4] >= sunf.minZ:
                                deathGhostChance = (sunf.dateArray[3] - (int(sunf.hourZ + 2))) * sunf.dateArray[4]
                                deathGhostChance = deathGhostChance / (32 - sunf.dateArray[2])
                                if random.randrange(0, 37500) < (deathGhostChance / ((32 - sunf.dateArray[2]) / 3) + 1):
                                    ghSpeaker = 5
                                    while ghSpeaker == 5:
                                        ghSpeaker = random.randrange(0, 8)
                                    pytools.sound.main.playSound('death_ghost_' + str(random.randrange(0, 2)) + ".mp3", ghSpeaker, (0.5 + random.random()) * 40, 1, 0, 0)
                    if sunf.dateArray[2] > 19:
                        if sunf.dateArray[3] > sunf.hourZ:
                            dyingGhostChance = (sunf.dateArray[3] - (int(sunf.hourZ + 1))) * sunf.dateArray[4]
                            dyingGhostChance = dyingGhostChance / (32 - sunf.dateArray[2])
                            if random.randrange(0, 37500) < (dyingGhostChance / ((32 - sunf.dateArray[2]) / 5) + 1):
                                ghSpeaker = 5
                                while ghSpeaker == 5:
                                    ghSpeaker = random.randrange(0, 8)
                                pytools.sound.main.playSound('dying_ghost_' + str(random.randrange(0, 3)) + ".mp3", ghSpeaker, (0.5 + random.random()) * 40, 1, 0, 0)
                        elif sunf.dateArray[3] == sunf.hourZ:
                            if sunf.dateArray[4] >= sunf.minZ:
                                dyingGhostChance = 0
                                if sunf.dateArray[3] < (24):
                                    dyingGhostChance = (sunf.dateArray[3] - (int(sunf.hourZ + 1))) * sunf.dateArray[4]
                                    dyingGhostChance = dyingGhostChance / (32 - sunf.dateArray[2])
                                if random.randrange(0, 37500) < (dyingGhostChance / ((32 - sunf.dateArray[2]) / 5) + 1):
                                    ghSpeaker = 5
                                    while ghSpeaker == 5:
                                        ghSpeaker = random.randrange(0, 8)
                                    pytools.sound.main.playSound('dying_ghost_' + str(random.randrange(0, 3)) + ".mp3", ghSpeaker, (0.5 + random.random()) * 40, 1, 0, 0)
                    if sunf.dateArray[2] > 9:
                        if sunf.dateArray[3] > sunf.hourZ:
                            ghostChance = 0
                            if sunf.dateArray[3] < (24):
                                ghostChance = (sunf.dateArray[3] - (int(sunf.hourZ))) * sunf.dateArray[4]
                                ghostChance = ghostChance / (32 - sunf.dateArray[2])
                            if random.randrange(0, 37500) < (ghostChance / ((32 - sunf.dateArray[2]) / 9) + 1):
                                ghSpeaker = 5
                                while ghSpeaker == 5:
                                    ghSpeaker = random.randrange(0, 8)
                                pytools.sound.main.playSound('ghost_' + str(random.randrange(0, 2)) + ".mp3", ghSpeaker, (0.5 + random.random()) * 40, 1, 0, 0)
                        elif sunf.dateArray[3] == sunf.hourZ:
                            if sunf.dateArray[4] >= sunf.minZ:
                                ghostChance = 0
                                if sunf.dateArray[3] < (24):
                                    ghostChance = (sunf.dateArray[3] - (int(sunf.hourZ))) * sunf.dateArray[4]
                                    ghostChance = ghostChance / (32 - sunf.dateArray[2])
                                if random.randrange(0, 37500) < (ghostChance / ((32 - sunf.dateArray[2]) / 9) + 1):
                                    ghSpeaker = 5
                                    while ghSpeaker == 5:
                                        ghSpeaker = random.randrange(0, 8)
                                    pytools.sound.main.playSound('ghost_' + str(random.randrange(0, 2)) + ".mp3", ghSpeaker, (0.5 + random.random()) * 40, 1, 0, 0)
                    time.sleep(0.1)
                    sections.ghostsChance = [(deathGhostChance / ((32 - sunf.dateArray[2]) / 3) + 1), (dyingGhostChance / ((32 - sunf.dateArray[2]) / 5) + 1), (ghostChance / ((32 - sunf.dateArray[2]) / 9) + 1)]
                except:
                    pass
            wait = True
            for n in sections.ghostsChance:
                if n > 1:
                    wait = False
            if wait:
                time.sleep(1)

    def closeMidTestRun():
        while True:
            if globals.run:
                try:
                    mainVars.noA = closetomidTest(sunf.dateArray, 23, 25, 10, mainVars.noA)
                    mainVars.noB = closetomidTest(sunf.dateArray, 23, 20, 15, mainVars.noB)
                    mainVars.noC = closetomidTest(sunf.dateArray, 23, 15, 30, mainVars.noC)
                    mainVars.noD = closetomidTest(sunf.dateArray, 23, 10, 45, mainVars.noD)
                except:
                    pass
            time.sleep(1)
    
    draftChance = 0
    
    def runDrafts():
        while True:
            if globals.run:
                try:
                    draftChance = 0
                    if sunf.dateArray[3] < 24:
                        draftChance = (sunf.dateArray[3] - (int(sunf.sunJson['cesth']))) * sunf.dateArray[4]
                    if sunf.dateArray[3] < (int(sunf.sunJson['csth'])):
                        draftChance = ((int(sunf.sunJson['csth'])) - sunf.dateArray[3]) * sunf.dateArray[4]
                    if random.randrange(0, 25000) < draftChance:
                        ghSpeaker = 5
                        while ghSpeaker == 5:
                            ghSpeaker = random.randrange(0, 8)
                        pytools.sound.main.playSound('draft_' + str(random.randrange(0, 3)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
                    sections.draftChance = draftChance
                    time.sleep(0.1)
                except:
                    pass
            if sections.draftChance <= 0:
                time.sleep(1)
        
    breathChance = 0
    
    def runBreaths():
        while True:
            if globals.run:
                try:
                    breathChance = 0
                    if sunf.dateArray[3] < (int(sunf.sunJson['csth'])):
                        breathChance = ((int(sunf.sunJson['csth'])) - sunf.dateArray[3]) * sunf.dateArray[4]
                    breathChance = breathChance / (32 - sunf.dateArray[2])
                    if random.randrange(0, 25000) < breathChance:
                        ghSpeaker = 5
                        while ghSpeaker == 5:
                            ghSpeaker = random.randrange(0, 8)
                        pytools.sound.main.playSound('h_breath_' + str(random.randrange(0, 4)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
                    sections.breathChance = breathChance
                    time.sleep(0.1)
                except:
                    pass
            if sections.draftChance <= 0:
                time.sleep(1)

    moodChance = [0, 0, 0, 0, 0, 0]

    def runMood():
        prevMin = -1
        while True:
            if globals.run:
                try:
                    moodChance = 0
                    if os.path.isfile('halloweenmode.derp') == True:
                        if prevMin != sunf.dateArray[4]:
                            monthS = pytools.clock.dateArrayToUTC([sunf.dateArray[0], 10, 1, 0, 0, 0])
                            monthE = pytools.clock.dateArrayToUTC([sunf.dateArray[0], 11, 1, 0, 0, 0])
                            monthC = pytools.clock.dateArrayToUTC(sunf.dateArray) - monthS
                            
                            hGeneralVol = 42 * (monthC / (monthE - monthS))
                            if hGeneralVol > 35:
                                hGeneralVol = 35
                            hGeneralSpeedModifier = 0.08
                            midnight = pytools.clock.dateArrayToUTC(pytools.clock.getMidnight(sunf.dateArray))
                            sunset = pytools.clock.dateArrayToUTC(sunf.dayTimes[5])
                            civil = pytools.clock.dateArrayToUTC(sunf.dayTimes[2])
                            sunrise = pytools.clock.dateArrayToUTC(sunf.dayTimes[3])
                            current = pytools.clock.dateArrayToUTC(sunf.dateArray)
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
                            if sunf.dateArray[1] != 11:
                                pytools.sound.main.playSoundAll('h_general.mp3', hGeneralVol, 1 - hGeneralSpeedModifier, 0, 0)
                            else:
                                pytools.sound.main.playSoundAll('h_general.mp3', hGeneralVol * (1 - (((sunf.dateArray[3] * 60 * 60) + (sunf.dateArray[4] * 60) + (sunf.dateArray[5])) / ((sunf.sunJson["csth"] * 60 * 60) + (sunf.sunJson["cstm"] * 60)))), 1 - hGeneralSpeedModifier, 0, 0)
                            prevMin = sunf.dateArray[4]
                        
                        moodChance = [0, 0, 0, 0, 0, 0]
                        
                        moodChance[0] = (sunf.dateArray[3] - (int(sunf.sunJson['cesth']))) * sunf.dateArray[4]
                        if sunf.dateArray[3] < (int(sunf.sunJson['csth'])):
                            moodChance[0] = ((int(sunf.sunJson['csth'])) - sunf.dateArray[3]) * sunf.dateArray[4]
                        
                        moodChance[1] = ((sunf.dateArray[3] - (int(sunf.sunJson['ceth']))) * sunf.dateArray[4] / 3) / (32 - sunf.dateArray[2])
                        if sunf.dateArray[3] < (int(sunf.sunJson['csth'])):
                            moodChance[1] = (((int(sunf.sunJson['csth'])) - sunf.dateArray[3]) * sunf.dateArray[4] / 3) / (32 - sunf.dateArray[2])
                        
                        moodChance[2] = ((sunf.dateArray[3] - (int(sunf.sunJson['neth']))) * sunf.dateArray[4] / 4) / (32 - sunf.dateArray[2])
                        if sunf.dateArray[3] < (int(sunf.sunJson['csth'])):
                            moodChance[2] = (((int(sunf.sunJson['csth'])) - sunf.dateArray[3]) * sunf.dateArray[4] / 4) / (32 - sunf.dateArray[2])
                        
                        moodChance[3] = ((sunf.dateArray[3] - (int(sunf.sunJson['aeth']))) * sunf.dateArray[4] / 5) / (32 - sunf.dateArray[2])
                        if sunf.dateArray[3] < (int(sunf.sunJson['csth'])):
                            moodChance[3] = (((int(sunf.sunJson['csth'])) - sunf.dateArray[3]) * sunf.dateArray[4] / 5) / (32 - sunf.dateArray[2])
                        
                        moodChance[4] = ((sunf.dateArray[3] - (int(sunf.sunJson['aeth']) + 1)) * sunf.dateArray[4]) / ((32 - sunf.dateArray[2]) / 2)
                        if sunf.dateArray[3] < (int(sunf.sunJson['csth'])):
                            moodChance[4] = (((int(sunf.sunJson['csth'])) - sunf.dateArray[3]) * sunf.dateArray[4]) / ((32 - sunf.dateArray[2]) / 2)
                        
                        moodChance[5] = ((sunf.dateArray[3] - (int(sunf.sunJson['aeth']) + 2)) * sunf.dateArray[4]) / ((32 - sunf.dateArray[2]) / 4)
                        if sunf.dateArray[3] < (int(sunf.sunJson['csth'])):
                            moodChance[5] = (((int(sunf.sunJson['csth'])) - sunf.dateArray[3]) * sunf.dateArray[4]) / ((32 - sunf.dateArray[2]) / 4)
                        
                        if random.randrange(0, 25000) < moodChance[0]:
                            pytools.sound.main.playSoundAll('h_general_mood.mp3', hGeneralVol, 1, 0, 0)
                        if random.randrange(0, 25000) < moodChance[1]:
                            pytools.sound.main.playSoundAll('h_general_dark.mp3', hGeneralVol, 1, 0, 0)
                        if random.randrange(0, 25000) < moodChance[2]:
                            pytools.sound.main.playSoundAll('h_general_evil.mp3', hGeneralVol, 1, 0, 0)
                        if random.randrange(0, 25000) < moodChance[3]:
                            pytools.sound.main.playSoundAll('h_general_sinister.mp3', hGeneralVol, 1, 0, 0)
                        if random.randrange(0, 25000) < moodChance[4]:
                            pytools.sound.main.playSoundAll('h_general_dying.mp3', hGeneralVol, 1, 0, 0)
                        if random.randrange(0, 25000) < moodChance[5]:
                            pytools.sound.main.playSoundAll('h_general_death.mp3', hGeneralVol * (1 + (random.random() / 5)), 1, 0, 0)
                    sections.moodChance = moodChance
                except:
                    pass
                time.sleep(0.1)
            wait = True
            for n in sections.moodChance:
                if n > 0:
                    wait = False
            if wait:
                time.sleep(1)
        
        
    knockChance = 0
        
    def runKnocks():
        while True:
            if globals.run:
                try:
                    knockChance = 0
                    if sunf.dateArray[3] < 24:
                        knockChance = (sunf.dateArray[3] - (int(sunf.sunJson['cesth']))) * sunf.dateArray[4]
                    knockChance = knockChance / (32 - sunf.dateArray[2])
                    if random.randrange(0, 15000) < knockChance:
                        ghSpeaker = 5
                        while ghSpeaker == 5:
                            ghSpeaker = random.randrange(0, 8)
                        pytools.sound.main.playSound('h_knock_' + str(random.randrange(0, 6)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
                    sections.knockChance = knockChance
                except:
                    pass
                time.sleep(0.1)
            if sections.knockChance <= 0:
                time.sleep(1)
        
    chainChance = 0
    
    def runChains():
        while True:
            if globals.run:
                try:
                    chainChance = 0
                    if sunf.dateArray[3] < 24:
                        chainChance = (sunf.dateArray[3] - (int(sunf.sunJson['cesth']) + 2)) * sunf.dateArray[4]
                    chainChance = chainChance / (32 - sunf.dateArray[2])
                    if random.randrange(0, 15000) < chainChance:
                        ghSpeaker = 5
                        while ghSpeaker == 5:
                            ghSpeaker = random.randrange(0, 8)
                        pytools.sound.main.playSound('h_chains_' + str(random.randrange(0, 3)) + ".mp3", ghSpeaker, 40, 1, 0, 0)
                    sections.chainChance = chainChance
                except:
                    pass
                time.sleep(0.1)
            if sections.chainChance <= 0:
                time.sleep(1)

def main():
    mainVars.noA = 0
    mainVars.noB = 0
    mainVars.noC = 0
    mainVars.noD = 0
    pHorr = False
    noE = 0
    noF = 0
    noG = 0
    
    sunfGrabber = threading.Thread(target=sunf.grab)
    ghostsRunner = threading.Thread(target=sections.testGhosts)
    closeToMidTester = threading.Thread(target=sections.closeMidTestRun)
    draftsRunner = threading.Thread(target=sections.runDrafts)
    breathsRunner = threading.Thread(target=sections.runBreaths)
    moodRunner = threading.Thread(target=sections.runMood)
    knocksRunner = threading.Thread(target=sections.runKnocks)
    chainsRunner = threading.Thread(target=sections.runChains)
    
    sunfGrabber.start()
    ghostsRunner.start()
    closeToMidTester.start()
    draftsRunner.start()
    breathsRunner.start()
    moodRunner.start()
    knocksRunner.start()
    chainsRunner.start()

    while True:
        sunf.dateArray = pytools.clock.getDateTime()
        
        globals.run = (sunf.dateArray[1] == 10) or ((sunf.dateArray[1] == 11) and (sunf.dateArray[2] == 1) and (sunf.dateArray[3] < sunf.sunJson["csth"]))
        
        if globals.run:
            
            sunf.getZ()
            
            if sunf.dateArray[2] > 19:
                if sunf.dateArray[4] == 35:
                    if noE != 1:
                        if random.randrange(sunf.dateArray[3], 24) == 23:
                            rumbleNum = random.randrange(0, 2)
                            pytools.sound.main.playSoundAll('h_rumble_' + str(rumbleNum) + '.mp3', 40, 1, 0, 0)
                        noE = 1
                else:
                    noE = 0
            else:
                noE = 0
            
            if sunf.dateArray[2] > 24:
                if sunf.dateArray[4] == 20:
                    if noF != 1:
                        if random.randrange(sunf.dateArray[3], 24) == 23:
                            rumbleNum = random.randrange(0, 2)
                            pytools.sound.main.playSoundAll('h_rumble_' + str(rumbleNum) + '.mp3', 40, 1, 0, 0)
                        noF = 1
                elif sunf.dateArray[4] == 40:
                    if noF != 1:
                        if random.randrange(sunf.dateArray[3], 24) == 23:
                            rumbleNum = random.randrange(0, 2)
                            pytools.sound.main.playSoundAll('h_rumble_' + str(rumbleNum) + '.mp3', 40, 1, 0, 0)
                        noF = 1
                else:
                    noF = 0
            else:
                noF = 0
            
            if sunf.dateArray[3] == int(sunf.sunJson['cesth']):
                if sunf.dateArray[4] == int(sunf.sunJson['cestm']):
                    if noG != 1:
                        if random.randrange(sunf.dateArray[2], 31) == 31:
                            pytools.sound.main.playSoundWindow('h_sunset.mp3;h_sunset.mp3', [40, 80], 1, 0, 0)
                        noG = 1
                else:
                    noG = 0
            else:
                noG = 0
            
            if sections.breathChance < 0:
                sections.breathChance = 0
            horrorIndex = sections.ghostsChance[0] + sections.ghostsChance[1] + sections.ghostsChance[2] + sections.draftChance + sections.breathChance + sections.moodChance[0] + sections.moodChance[1] + sections.moodChance[2] + sections.moodChance[3] + sections.moodChance[4] + sections.moodChance[5] + sections.knockChance + sections.chainChance
            
            time.sleep(1)
            
            status.vars["horrorStats"]["sections.ghostsChance-0"] = sections.ghostsChance[0]
            status.vars["horrorStats"]["sections.ghostsChance-1"] = sections.ghostsChance[1]
            status.vars["horrorStats"]["sections.ghostsChance-2"] = sections.ghostsChance[2]
            status.vars["horrorStats"]["sections.draftChance"] = sections.draftChance
            status.vars["horrorStats"]["sections.breathChance"] = sections.breathChance
            status.vars["horrorStats"]["sections.moodChance"] = sections.moodChance
            status.vars["horrorStats"]["sections.knockChance"] = sections.knockChance
            status.vars["horrorStats"]["sections.chainChance"] = sections.chainChance
            
            if (sunf.dateArray[5] % 2) == 0:
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
                        
            
            
            
            
                        
                    
                        
            
                    
                    
                
            
            
                    