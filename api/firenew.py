import time
import sys
import os
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
    
def getTemp():
    temp = pytools.IO.getList("dataList.pyl")[1][0][7] + 273
    return temp
    
def playMatch():
    print("Lighting fireplace...")
    os.system('cmd.exe /c start /b /d ".\\lighting\\fire" "" ..\\..\\light.exe match_light.vbs & start /b /wait "" /d ".\\sound\\fire" ..\\..\\fireplace.exe match.vbs ')

def playFire():
    print("Playing standard fire effect...")
    os.system('cmd.exe /c start /b  "" /d ".\\sound\\fire" ..\\..\\fireplace.exe fire.vbs & start /b /d ".\\lighting\\fire" "" ..\\..\\light.exe fire_light.vbs')
    
def playFireStart():
    print("Playing standard fire_starting effect...")
    os.system('cmd.exe /c start /b  "" /d ".\\sound\\fire" ..\\..\\fireplace.exe fire_start.vbs & start /b /d ".\\lighting\\fire" "" ..\\..\\light.exe fire_start_light.vbs')
    
def playFireEnd():
    print("Playing standard fire_ending effect...")
    os.system('cmd.exe /c start /b  "" /d ".\\sound\\fire" ..\\..\\fireplace.exe fire_end.vbs & start /b /wait /d ".\\lighting\\fire" "" ..\\..\\light.exe fire_end_light.vbs')
    
def playFireiLog():
    print("Playing standard fire_ilog effect...")
    os.system('cmd.exe /c start /b  "" /d ".\\sound\\fire" ..\\..\\fireplace.exe fire_ilog.vbs & start /b /d ".\\lighting\\fire" "" ..\\..\\light.exe fire_ilog_light.vbs')

def playFireStartNew():
    pytools.sound.main.playSound('fire_start_new.mp3', 1, 60, 1, 0, 0)
    pytools.sound.main.playSound('fire_start_new_light.mp3', 5, 100, 1, -100, 0)
    
def playFireCont():
    pytools.sound.main.playSound('fire_cont.mp3', 1, 60, 1, 0, 0)
    pytools.sound.main.playSound('fire_cont_light.mp3', 5, 100, 1, -100, 0)

def playGetLogs():
    if testWindow() == 1:
        pytools.sound.main.playSound('wood_chopper_nm.mp3', 6, 100, 1, 0, 0)
        pytools.sound.main.playSound('wood_chopper_wall.mp3', 0, 25, 1, 0, 0)
        pytools.sound.main.playSound('wood_chopper_wall.mp3', 1, 25, 1, 0, 0)
    else:
        pytools.sound.main.playSound('wood_chopper_nm.mp3', 3, 100, 1, 0, 0)
        pytools.sound.main.playSound('wood_chopper_wn.mp3', 2, 25, 1, 0, 0)
        pytools.sound.main.playSound('wood_chopper_wall.mp3', 0, 25, 1, 0, 0)
        pytools.sound.main.playSound('wood_chopper_wall.mp3', 1, 25, 1, 0, 0)

def testforCond():
    temp = getTemp()
    if temp < 281:
        fire = 1
    else:
        fire = 0
    return fire

def testWindow():
    out = 0
    if os.path.exists(".\\nomufflewn.derp") == True:
        out = 1
    return out

def main():
    getLogs = 0
    logs = 10
    while True:
        fireCond = testforCond()
        if fireCond == 1:
            logs = logs - 3
            playMatch()
            playFireStart()
            time.sleep(194)
            while fireCond == 1:
                logs = logs - 1
                tic = 0
                while (tic < 5) and (fireCond == 1):
                    playFire()
                    if logs < 1:
                        getLogs = 1
                    if logs > 10:
                        getLogs = 0
                    if getLogs == 1:
                        playGetLogs()
                        logs = logs + 4
                    tic = tic + 1
                    fireCond = testforCond()
                    time.sleep(194)
                if fireCond == 1:
                    playFireiLog()
                    time.sleep(2100)
            playFireEnd()
            time.sleep()
        time.sleep(10)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def mainNew():
    while True:
        fireCond = testforCond()
        if fireCond == 1:
            playFireStartNew()
            time.sleep(2500)
            while fireCond == 1:
                playFireCont()
                time.sleep(4720)
                fireCond = testforCond()
        time.sleep(10)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()