import time
import sys
import os
import pytools

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }
    
def getTemp():
    temp = pytools.IO.getList("dataList.pyl")[1][0][7] + 273
    return temp
    
def playMatch():
    print("Lighting fireplace...")
    pytools.sound.main.playSound('match_light.mp3', 5, 50, 1, 0, 0)
    pytools.sound.main.playSound('match.wav', 1, 10, 1, 0, 1)
    # os.system('cmd.exe /c start /b /d ".\\lighting\\fire" "" ..\\..\\light.exe match_light.vbs & start /b /wait "" /d ".\\sound\\fire" ..\\..\\fireplace.exe match.vbs ')

def playFire():
    print("Playing standard fire effect...")
    pytools.sound.main.playSound('fire.wav', 1, 10, 1, 0, 0)
    pytools.sound.main.playSound('fire.wav', 5, 100, 1, -100, 0)   
    # os.system('cmd.exe /c start /b  "" /d ".\\sound\\fire" ..\\..\\fireplace.exe fire.vbs & start /b /d ".\\lighting\\fire" "" ..\\..\\light.exe fire_light.vbs')
    
def playFireStart():
    print("Playing standard fire_starting effect...")
    pytools.sound.main.playSound('fire_start.wav', 1, 10, 1, 0, 0)
    pytools.sound.main.playSound('fire_start.wav', 5, 100, 1, -100, 0)
    # os.system('cmd.exe /c start /b  "" /d ".\\sound\\fire" ..\\..\\fireplace.exe fire_start.vbs & start /b /d ".\\lighting\\fire" "" ..\\..\\light.exe fire_start_light.vbs')
    
def playFireEnd():
    print("Playing standard fire_ending effect...")
    pytools.sound.main.playSound('fire_end.wav', 1, 10, 1, 0, 0)
    pytools.sound.main.playSound('fire_end.wav', 5, 100, 1, -100, 0)
    # os.system('cmd.exe /c start /b  "" /d ".\\sound\\fire" ..\\..\\fireplace.exe fire_end.vbs & start /b /wait /d ".\\lighting\\fire" "" ..\\..\\light.exe fire_end_light.vbs')
    
def playFireiLog():
    print("Playing standard fire_ilog effect...")
    pytools.sound.main.playSound('fire_ilog.mp3', 1, 10, 1, 0, 0)
    pytools.sound.main.playSound('fire_ilog.mp3', 5, 100, 1, -100, 0)
    # os.system('cmd.exe /c start /b  "" /d ".\\sound\\fire" ..\\..\\fireplace.exe fire_ilog.vbs & start /b /d ".\\lighting\\fire" "" ..\\..\\light.exe fire_ilog_light.vbs')

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

def run():
    main()