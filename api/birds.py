import pytools
import random
import math
import os
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }
    
birds = pytools.IO.getJson("birds.json")
birdTimes = pytools.IO.getJson("birdDays.json")

class tools:
    def getActivity(weights, dayTimesUTC):
        utc = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime())
        curr = 0
        while curr < (len(dayTimesUTC) - 1):
            if dayTimesUTC[curr] <= utc < dayTimesUTC[curr + 1]:
                break
            curr = curr + 1
        try:
            percent = (utc - dayTimesUTC[curr]) / dayTimesUTC[curr + 1]
        except:
            percent = (utc - dayTimesUTC[curr]) / (dayTimesUTC[0] + 86400)
        # print((weights[curr + 1] * (1 - percent)))
        return (weights[curr] * (1 - percent)) + (weights[curr + 1] * percent)
    
    def isWater(bird):
        n = ["goose", "duck", "mallard", "bufflehead", "merganser", "grouse", "gull"]
        i = 0
        while i < len(n):
            if bird.find(n[i]) != -1:
                return (random.random() * random.random() * random.random() * random.random() * random.random())
            i = i + 1
        return 1
    
    def isRaven(bird):
        if bird.find("raven") != -1:
            return random.random() * random.random()
        else:
            return 1
        
    def isCrow(bird):
        if bird.find("crow") != -1:
            return random.random() * random.random()
        else:
            return 1
        
    def isHunter(bird):
        n = ["hawk", "eagle", "owl", "osprey", "heron", "woodpecker", "grouse"]
        for f in n:
            if bird.find(f) != -1:
                return (random.random() * random.random())
        return 1
            
    def gullInc(bird, dataArray):
        if bird.find("gull") != -1:
            if dataArray[0][3] > 0:
                return (random.random() * dataArray[0][3]) + 1
            else:
                return 1
        else:
            return 1
        
    def tempDiff(bird, dataArray):
        i = 0
        f = 0
        r = 0
        dateArray = pytools.clock.getDateTime()
        hourTime = dateArray[3] + (((dateArray[4] * 60) + dateArray[5]) / 3600)
        while i < len(bird["activity"]):
            if r < bird["activity"][i]:
                r = bird["activity"][i]
                f = i
            i = i + 1
        monthPeak = 365 * (f / 12)
        tempDial = 4 * math.sin((2 * 3.14 * ((1 / 24) * hourTime)) - 21)
        currentPeak = (3 + math.fabs(dataArray[0][7] - (tempDial + ((-16 * math.sin(2 * 3.14 * ((1 / 365) * monthPeak))) + 7))))
        if currentPeak < 0.01:
            currentPeak = 0.01
        out = random.random() / (currentPeak / 3)
        if out > 3:
            out = 3
        if out < 1:
            out = 1
        return out

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
    
def main():
    birds = pytools.IO.getJson("birds.json")
    birdTimes = pytools.IO.getJson("birdDays.json")
    dayTimes = pytools.IO.getList("daytimes.pyl")[1]
    dayTimesUTC = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while i < len(dayTimes):
        dayTimesUTC[i + 1] = pytools.clock.dateArrayToUTC(dayTimes[i])
        i = i + 1
    dataArray = utils.dataGrabber()
    while True:
        if pytools.clock.getDateTime()[5] == 0:
            dayTimes = pytools.IO.getList("daytimes.pyl")[1]
            dayTimesUTC = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            i = 0
            while i < len(dayTimes):
                dayTimesUTC[i + 1] = pytools.clock.dateArrayToUTC(dayTimes[i])
                i = i + 1
            dataArray = utils.dataGrabber()
        dayTimesUTC[0] = pytools.clock.dateArrayToUTC(dayTimes[4]) - (86400 / 2)
        for bird in birds:
            ytc = (12 * pytools.clock.getYearUTC()) / 31536000
            monthActivity = ((1 - (ytc - math.floor(ytc))) * birds[bird]["activity"][int(math.floor(ytc))] + (((ytc - math.floor(ytc))) * birds[bird]["activity"][int(math.floor(ytc + 1))]))
            dayActivity = tools.getActivity(birdTimes[bird], dayTimesUTC)
            activity = (((monthActivity * dayActivity) / 100) ** (2 - (1 - tools.isHunter(bird)))) * tools.isWater(bird) * tools.isRaven(bird) * tools.isHunter(bird) * random.random() * tools.gullInc(bird, dataArray) * tools.tempDiff(birds[bird], dataArray)
            # print("Bird " + bird + " activity is registering at " + str(int(math.floor(activity * 100))) + "%" + " " + str(monthActivity) + " " + str(dayActivity))
            if random.random() < activity:
                if utils.testWindow():
                    pytools.sound.main.playSound(birds[bird]["sounds"][int(math.floor(random.random() * len(birds[bird]["sounds"])))], 6, (((activity * 2) * 10)) * random.random() * tools.isWater(bird) * tools.tempDiff(birds[bird], dataArray) * tools.isRaven(bird) * tools.isCrow(bird), 1, 0, 0)
                else:
                    pytools.sound.main.playSound(birds[bird]["sounds"][int(math.floor(random.random() * len(birds[bird]["sounds"])))], 2, (((activity * 2) * 10)) * random.random() * tools.isWater(bird) * tools.isRaven(bird) * tools.tempDiff(birds[bird], dataArray) * tools.isCrow(bird), 1, 0, 0)
                    pytools.sound.main.playSound(birds[bird]["sounds"][int(math.floor(random.random() * len(birds[bird]["sounds"])))], 3, (((activity * 2) / 8) * 10) * random.random() * tools.isWater(bird) * tools.isRaven(bird) * tools.tempDiff(birds[bird], dataArray) * tools.isCrow(bird), 1, 0, 0)
            time.sleep(0.1)
def run():
    main()