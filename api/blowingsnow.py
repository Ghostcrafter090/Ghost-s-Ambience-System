import pytools
import random
import os
import time

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

class utils:
    def dataGrabber():
        out = pytools.IO.getList('.\\dataList.pyl')[1]
        if out == 1:
            out = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        return out
    
    def testWindow():
        out = False
        if os.path.exists(".\\nomufflewn.derp") == True:
            out = True
        return out

def audio(dataList, depth):
    volume = (((2500 / 30) * dataList[0][1]) / 100) + 25 + depth
    if dataList[0][4].find("snow") != -1:
        volume = volume * 2
    if utils.testWindow():
        print("Blowing snow with window open...")
        pytools.sound.main.playSound('snowwindow.mp3', 6, volume, 1, 0, 0)
    else:
        print("Blowing snow with window closed...")
        pytools.sound.main.playSound('snowonwindow.mp3', 2, volume, 1, 0, 0)
        pytools.sound.main.playSound('snowwindow.mp3', 3, volume, 1, 0, 0)

def main():
    while True:
        data = pytools.net.getTextAPI('https://www.snow-forecast.com/resorts/Ski-Martock/6day/bot')
        depth = float(data.split("Fresh snowfall depth:")[1].split(" ")[1])
        try:
            dataList = utils.dataGrabber()
        except:
            dataList = [[3.49, 7.79, 10000.0, 0, 'clouds', 4.0, 1027.0, 7.360000000000014, 99.0], [0, 0, 1027.0, 7.360000000000014, 99.0], 'set temp=280\n    set tempc=7\n    set windspeed=3\n    set windgust=7\n    set pressure=1027\n    set humidity=99\n    set weather=clouds\n    set modifier=4', 7]
        if dataList[0][7] < 5:
            chance = (5 - (dataList[0][7])) * (5 - (dataList[0][7])) * (5 - (dataList[0][7])) * (5 - (dataList[0][7])) * (float(depth) + 1)
        else:
            chance = 0
        print("Blowing Snow Chance: " + str(chance))
        if dataList[0][4].find("snow") != -1:
            audio(dataList, depth)
        if (random.random() * 32768) <= chance:
            audio(dataList, depth)
        time.sleep(194)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()
