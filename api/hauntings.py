import pytools
import modules.floorplan as floorplan
import random
import math
import time
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
import modules.ghostAudio as audio
import speech_recognition as sr

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

# Definitions:
#
# Ghost communication, the ghost to communicate via reaction to loud sounds. Also deturmines the ghosts ability to create death calls over the phone. Also allows for ghost texts.
#
# Ghost Reactions, the ghost reacting to energy shifts in the form of loud noises. These are triggered based on volume levels of any room minus the volume level of the ambience system. 
# More energy means higher activity.

class type:
    echo = 0
    spirit = 1
    poltergeist = 2
    demon = 3
    
class speech:

    # initialize tokenizer and model from pretrained GPT2 model
    tokenizer = AutoTokenizer.from_pretrained("huggingartists/ghost")
    model = AutoModelWithLMHead.from_pretrained("huggingartists/ghost")
    
class tools:
    def getDayTimesUTC():
        dayTimes = pytools.IO.getList("daytimes.pyl")[1]
        try:
            while int(dayTimes) == dayTimes:
                dayTimes = pytools.IO.getList("daytimes.pyl")[1]
                time.sleep(1)
        except:
            pass
                
        dayTimesUTC = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        while i < len(dayTimes):
            dayTimesUTC[i + 1] = pytools.clock.dateArrayToUTC(dayTimes[i])
            i = i + 1
        dayTimesUTC[0] = pytools.clock.dateArrayToUTC(dayTimes[4]) - (86400 / 2)
        return dayTimesUTC
    
    def getMin(n):
        if n[0] < n[1]:
            return n[0]
        else:
            return n[1]

class haunts:
    ghosts = {}
    
    def save(prop):
        ghostsf = pytools.IO.getJson("ghosts.json")
        ghostsf["list"].append(prop)
        pytools.IO.saveJson("ghosts.json", ghostsf)
    
    def register(properties):
        haunts.ghosts[properties["name"]] = ghost(properties)
        
    def remove(properties):
        haunts.ghosts.pop(properties["name"])
        
    def purgeGhosts():
        ghostsf = pytools.IO.getJson("ghosts.json")
        i = 0
        for n in ghostsf["list"]:
            try:
                if pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) > n["halfLife"]:
                    if random.random() < (5356800 / (pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) - n["halfLife"])):
                        print("A ghost has left: " + n["name"] + " of type " + str(n["type"]))
                        ghostsf["list"].pop(i)
                        haunts.remove(n)
            except:
                pass
            i = i + 1
        pytools.IO.saveJson("ghosts.json", ghostsf)
        
    def getGhosts():
        return pytools.IO.getJson("ghosts.json")["list"]
        
    def randomRegister():
        person = pytools.net.getJsonAPI("https://api.namefake.com/")
        dobf = person["birth_data"]
        dob = [int(dobf.split("-")[0]), int(dobf.split("-")[1]), int(dobf.split("-")[2]), int(math.floor(random.random() * 24)), int(math.floor(random.random() * 60)), int(math.floor(random.random() * 60))]
        dodMonth = int(math.floor(1 + (random.random() * 11)))
        dod = [int(dobf.split("-")[0]) + int(random.random() * 117), dodMonth, int(math.floor(pytools.clock.getMonthEnd(dodMonth) * random.random())), int(math.floor(random.random() * 24)), int(math.floor(random.random() * 60)), int(math.floor(random.random() * 60))]
        while pytools.clock.dateArrayToUTC(dod) > pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
            dodMonth = int(math.floor(1 + (random.random() * 11)))
            dod = [dob[0] + int(random.random() * random.random() * 117), dodMonth, int(math.floor(pytools.clock.getMonthEnd(dodMonth) * random.random())), int(math.floor(random.random() * 24)), int(math.floor(random.random() * 60)), int(math.floor(random.random() * 60))]
        name = person["name"]
        typf = int(math.floor(random.random() * 4))
        if typf == 0:
            acti = [random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10]
        elif typf == 1:
            acti = [random.random() * 5, random.random() * 6, random.random() * 7, random.random() * 8, random.random() * 9, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 9, random.random() * 8, random.random() * 7, random.random() * 6]
        elif typf == 2:
            acti = [random.random() * 10, random.random() * 9, random.random() * 5, random.random() * 2, random.random() * 1, random.random() * 2, random.random() * 3, random.random() * 4, random.random() * 5, random.random() * 6, random.random() * 7, random.random() * 8]
        elif typf == 3:
            acti = [random.random() * 10, random.random() * 6, random.random() * 2, random.random() * 1, random.random() * 0, random.random() * 0, random.random() * 0, random.random() * 0, random.random() * 0, random.random() * 2, random.random() * 7, random.random() * 10]
        else:
            acti = [random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10, random.random() * 10]
            typf = 0
        mem = []
        dobu = pytools.clock.dateArrayToUTC(dob)
        dodu = pytools.clock.dateArrayToUTC(dod)
        i = 0
        while i < (random.random() * 20):
            rndY = dob[0] + int(math.floor(((dod[0] - dob[0]) * random.random())))
            rndM = int(math.floor(1 + (random.random() * 11)))
            mem.append([[rndY, rndM, int(math.floor(pytools.clock.getMonthEnd(rndM) * random.random())), int(math.floor(random.random() * 24)), int(math.floor(random.random() * 60)), int(math.floor(random.random() * 60))], [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]])
            i = i + 1
        mem.append([dob, [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]])
        mem.append([dod, [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]])
        prop = {
            "name": name,
            "type": typf, 
            "details": {
                "activity": acti,
                "hatrid": random.random() * 10 * typf,
                "love": random.random() * 10 / (((random.random() * 0.5) + 0.5) * (typf + 1)),
                "voice": [((1.3 * random.random()) + 0.3), (random.random() * 10) + 4, random.random()],
                "memmories": mem,
                "completedMemmories": {}
            },
            "dateAdded": pytools.clock.getDateTime(),
            "halfLife": pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + (random.random() * 100 * 24 * 60 * 60)
        }
        haunts.save(prop)
        haunts.register(prop)
        print("A new ghost has arrived: " + prop["name"] + " of type " + str(prop["type"]))
    
    class handler:
        def handle(current=False):
            dateArray = pytools.clock.getDateTime()
            if current != False:
                dateArray = current
            startOfYear = pytools.clock.dateArrayToUTC([dateArray[0], 1, 1, 0, 0, 0])
            current = pytools.clock.dateArrayToUTC(dateArray) - startOfYear
            a = 100
            b = 26265600
            c = 3000000000000
            e = 2.71828182846
            f = 30931200
            g = 300000000000
            p = 3.14159265359
            h = 50
            j = 10 * math.sin((p / 1180290.0) * (-current - (dateArray[0] * 365.25 * 24 * 60 * 60) - (13 * 24 * 60 * 60)))
            k = 10 * math.sin((p / 302499) * (current + (dateArray[0] * 365.25 * 24 * 60 * 60) - 6))
            l = 0
            i = 1
            while i < 13:
                nf = pytools.clock.dateArrayToUTC([dateArray[0], i, 13, 12, 0, 0]) - startOfYear
                l = l + (10 * e ** (-(((current - nf) ** 2) / g)))
                i = i + 1
            hallowFactor = (a * e ** (-(((current - b) ** 2) / c))) + (h * e ** (-(((current - f) ** 2) / g))) + j + k + l
            pytools.IO.saveFile("hallowFactor.cx", str(hallowFactor))
            if hallowFactor < 6:
                hallowFactor = 12
            while len(haunts.getGhosts()) < (hallowFactor / 6):
                haunts.randomRegister()
            haunts.purgeGhosts()

class ghost:
    def __init__(self, information):
        self.prop = information
        
    # Spirit:
    # Standard ghost type, commincative, non-reactive, acts on own accord. Good or bad.
    # 
    # Poltergeist:
    # Non communicative, highly reactive. Poltergeists can be generated during long periods of high energy.
    # 
    # Echo:
    # Non communicative, non reactive, acts on own accord.
    #
    # Demon:
    # Highly communicative, highly reactive, acts on own accord.
    
    
    prop = {
        "name": "null", # The Ghosts Name.
        "type": type.echo, # The Ghost's type: (spirit, echo, poltergeist, demon)
        "details": {
            "activity": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "hatrid": 0,
            "love": 0,
            "memmories": [
                # [[0, 0, 0, 0, 0, 0], [0, 0]]
            ],
            "completedMemmories": {}
        }
    }
    
    sM = 1000
    
    speechModifier = 1000
    
    mood = 0 # deturmine's the ghosts mood. Negatives are periods of hate, positives are periods of love.
    activity = 0 # How active the ghost is at this current point in time. (Controlled by either activity or energy).
    
    activeMemmory = False
    
    tempMemmorys = [
        # [[0, 0, 0, 0, 0, 0], [0, 0]]
    ]
    
    x = 20
    y = 20
    rotation = 0
    
    def move(self, x, y, r=False, d=1):
        # while self.rotation != r:
        #     self.rotation = self.rotation + 1
        #     if self.rotation > 359:
        #         self.rotation = 0
        if r == False:
            dial = self.getRot(x, y)
            wall = floorplan.map.vectorSearch(0, self.x, self.y, dial)
            self.x = self.x + dial[0]
            self.y = self.y + dial[1]
            if (0 > self.x) or (self.x > floorplan.level[0][1][0]):
                self.x = random.random() * floorplan.level[0][1][0]
            if (0 > self.y) or (self.y > floorplan.level[0][1][1]):
                self.y = random.random() * floorplan.level[0][1][1]
            # print("Moved ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " to position " + str(self.x) + "," + str(self.y))
            if (wall[0] - 5) < self.x < (wall[0] + 5):
                if ((wall[1] - 5) < self.y < (wall[1] + 5)):
                    self.x = self.x - dial[0]
                    self.y = self.y - dial[1]
                    self.wallAnger = self.wallAnger + math.fabs((self.mood / 100))
                    # print("Ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " bounced into wall at position " + str(self.x) + "," + str(self.y) + ". It's wall anger is now: " + str(self.wallAnger))
                    return False
            return True
        else:
            self.rotation = r
            wall = floorplan.map.rotSearch(0, self.x, self.y, self.rotation)
            dial = floorplan.coord.dialation.get(1 * d, self.rotation)
            self.x = self.x + dial[0]
            self.y = self.y + dial[1]
            if (0 > self.x) or (self.x > floorplan.level[0][1][0]):
                self.x = random.random() * floorplan.level[0][1][0]
            if (0 > self.y) or (self.y > floorplan.level[0][1][1]):
                self.y = random.random() * floorplan.level[0][1][1]
            # print("Moved ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " to position " + str(self.x) + "," + str(self.y))
            if (wall[0] - 5) < self.x < (wall[0] + 5):
                if ((wall[1] - 5) < self.y < (wall[1] + 5)):
                    self.x = self.x - dial[0]
                    self.y = self.y - dial[1]
                    self.wallAnger = self.wallAnger + math.fabs((self.mood / 100))
                    # print("Ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " bounced into wall at position " + str(self.x) + "," + str(self.y) + ". It's wall anger is now: " + str(self.wallAnger))
                    return False
            return True
        
    def getRot(self, x, y):
        a = x - self.x
        b = y - self.y
        while (((a > 1) or (a < -1)) and ((b > 1) or (b < -1))):
            rrand = random.random()
            a = a / (1 + rrand)
            b = b / (1 + rrand)
        return [a, b]

    def getActivity(self, weights):
        dayTimesUTC = tools.getDayTimesUTC()
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
    
    def memmoryTrigger(self):
        dateArray = pytools.clock.getDateTime()
        for n in self.prop["details"]["memmories"]:
            if pytools.clock.dateArrayToUTC(dateArray) > pytools.clock.dateArrayToUTC([dateArray[0], dateArray[1], dateArray[2], n[0][3], n[0][4], n[0][5]]):
                try:
                    if self.prop["details"]["completedMemmories"][str(n)] == True:
                        pass
                except:
                    if self.activeMemmory == False:
                        print("Memmory " + str(n) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been triggered.")
                        self.activeMemmory = n
    
    spm = 0
    
    def speak(self, words, type):
        inputs = speech.tokenizer.encode(words.split(";")[0], return_tensors='pt')
        outputs = speech.model.generate(inputs, max_length=(10 + int(random.random() * 20)), do_sample=True)
        text = speech.tokenizer.decode(outputs[0], skip_special_tokens=True)
        speechf = "null"
        try:
            try:
                speechf = text.split("\n")[1:math.floor(int((((len(text.split("\n")) - 1) * random.random()) + 1)))]
                audio.speak(speechf, self.prop["name"].replace(" ", ".").replace(".", "_"), type, self.mood, self.prop["details"]["voice"], self.activity, [self.x, self.y], 0)
            except:
                speechf = text.split("\n")[0]
                audio.speak(speechf, self.prop["name"].replace(" ", ".").replace(".", "_"), type, self.mood, self.prop["details"]["voice"], self.activity, [self.x, self.y], 0)
        except:
            pass
        print("Ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has spoken. It has said: " + speechf)
    
    def getSpm(self):
        try:
            self.spm = ((1000 * self.spm) + int(pytools.IO.getFile("speechPerMinute.cx"))) / 1001
        except:
            pass
        return 1 + self.spm
    
    wallAnger = 1
    
    lastDay = -1
    
    class ai:
        def echo(selff, dateArray):
            self = selff
            self.activity = self.getActivity(self.prop["details"]["activity"])
            self.mood = ((self.mood * 3) + (((2 * random.random()) - 1)) / 4) + (0.1 * random.random() * self.prop["details"]["hatrid"]) + (0.1 * random.random() * self.prop["details"]["love"]) 
            if self.wallAnger > 200:
                if self.activeMemmory != False:
                    self.prop["details"]["completedMemmories"][str(self.activeMemmory)] = True
                    print("Memmory " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been terminated out of anger.")
                    self.activeMemmory = False
            if dateArray[2] != self.lastDay:
                self.prop["details"]["completedMemmories"] = {}
                self.lastDay = dateArray[2]
            if self.mood > 100:
                self.mood = 100
            if self.mood < -100:
                self.mood = -100
            self.memmoryTrigger()
            if self.activeMemmory != False:
                wall = self.move(self.activeMemmory[1][0], self.activeMemmory[1][1])
                if wall == False:
                    # self.wallAnger = self.wallAnger + math.fabs((self.mood / 100))
                    self.move(0, 0, (random.random() * 2) - 1, self.wallAnger * tools.getMin(self.getRot(self.activeMemmory[1][0], self.activeMemmory[1][1])))
                    self.mood = self.mood - (5 / (self.prop["details"]["hatrid"] - self.prop["details"]["love"]))
                else:
                    self.wallAnger = self.wallAnger - math.fabs((self.mood / 400))
                    if self.wallAnger < 1:
                        self.wallAnger = 1
                if ((self.x - 5) < self.activeMemmory[1][0] < (self.x + 5)) or (self.wallAnger > 200):
                    if ((self.y - 5) < self.activeMemmory[1][1] < (self.y + 5)) or (self.wallAnger > 200):
                        self.prop["details"]["completedMemmories"][str(self.activeMemmory)] = True
                        print("Memmory " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been completed.")
                        self.activeMemmory = False
            else:
                if self.mood > 0:
                    self.rotation = ((self.rotation * 10) + ((random.random() * 2) - 1)) / 11
                    self.move(0, 0, self.rotation, self.activity * random.random())
                else:
                    self.rotation = ((self.rotation * 10) + ((random.random() * 2) - 1)) / 11
                    self.move(0, 0, self.rotation, (self.activity * (-1 * self.mood)) * random.random())
        
        def spirit(selff, dateArray):
            self = selff
            self.activity = self.getActivity(self.prop["details"]["activity"]) * self.getSpm()
            self.mood = ((self.mood * 3) + (((4 * random.random()) - 1)) / 4) + (0.1 * random.random() * self.prop["details"]["hatrid"]) + (0.1 * random.random() * self.prop["details"]["love"]) 
            if self.wallAnger > 200:
                if self.activeMemmory != False:
                    self.prop["details"]["completedMemmories"][str(self.activeMemmory)] = True
                    print("Memmory " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been terminated out of anger.")
                    self.activeMemmory = False
            if dateArray[2] != self.lastDay:
                self.prop["details"]["completedMemmories"] = {}
                self.lastDay = dateArray[2]
            if self.mood > 100:
                self.mood = 100
            if self.mood < -100:
                self.mood = -100
            if self.activity > 10:
                self.activity = 10
            self.memmoryTrigger()
            if self.activeMemmory != False:
                wall = self.move(self.activeMemmory[1][0], self.activeMemmory[1][1])
                if wall == False:
                    # self.wallAnger = self.wallAnger + math.fabs((self.mood / 100))
                    self.move(self.activeMemmory[1][0], self.activeMemmory[1][1], (random.random() * 2) - 1, self.wallAnger * tools.getMin(self.getRot(self.activeMemmory[1][0], self.activeMemmory[1][1])))
                    self.mood = self.mood - (5 / (self.prop["details"]["hatrid"] - self.prop["details"]["love"]))
                else:
                    self.wallAnger = self.wallAnger - math.fabs((self.mood / 400))
                    if self.wallAnger < 1:
                        self.wallAnger = 1
                if ((self.x - 5) < self.activeMemmory[1][0] < (self.x + 5)) or (self.wallAnger > 200):
                    if ((self.y - 5) < self.activeMemmory[1][1] < (self.y + 5)) or (self.wallAnger > 200):
                        self.prop["details"]["completedMemmories"][str(self.activeMemmory)] = True
                        print("Memmory " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been completed.")
                        self.activeMemmory = False
            else:
                if self.mood > 0:
                    n = random.random() < (0.1 / ((10 - self.activity) + 1))
                    if (self.activeMemmory == False) and n:
                        transcript = pytools.IO.getFile("transcript.cxl").split("\n")
                        try:
                            indexf = int(math.floor(random.random() * len(transcript)))
                            self.activeMemmory = [pytools.clock.getDateTime(), pytools.IO.getJson("mics.json")[transcript[indexf].split(";")[1]]]
                        except:
                            pass
                        print("Ghost communication response " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been triggered.")
                    if self.activeMemmory == False:
                        n = random.random() * random.random() < ((0.1 / (10 - self.activity)) * random.random() * random.random() * random.random())
                        if n:
                            self.activeMemmory = [pytools.clock.getDateTime(), [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]]
                    self.move(self.x, self.y, (random.random() * 2) - 1, (self.activity / 10))
                    n = random.random() < (((0.1 / ((10 - self.activity) + 1)) / self.speechModifier))
                    if (self.activeMemmory == False) and n:
                        try:
                            transcript = pytools.IO.getFile("transcript.cxl").split("\n")
                            indexf = int(math.floor(random.random() * len(transcript)))
                            self.speak(transcript[indexf], self.prop["type"])
                            print(str(n) + " spirit-0")
                        except:
                            pass
                else:
                    if self.activeMemmory == False:
                        n = random.random() * random.random() < ((0.1 / ((10 - self.activity) + 1)) * random.random() * random.random() * random.random())
                        if n:
                            self.activeMemmory = [pytools.clock.getDateTime(), [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]]
                    self.rotation = ((self.rotation * 10) + ((random.random() * 2) - 1)) / 11
                    self.move(self.x, self.y, self.rotation, 2 * ((self.activity / 10) * (-1 * (self.mood / 100))))
                    
        def poltergeist(selff, dateArray):
            self = selff
            self.activity = self.getActivity(self.prop["details"]["activity"]) * self.getSpm()
            self.mood = ((self.mood * 3) + (((8 * random.random()) - 1)) / 4) + (0.1 * random.random() * self.prop["details"]["hatrid"]) + (0.1 * random.random() * self.prop["details"]["love"]) 
            if self.wallAnger > 200:
                if self.activeMemmory != False:
                    self.prop["details"]["completedMemmories"][str(self.activeMemmory)] = True
                    print("Memmory " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been terminated out of anger.")
                    self.activeMemmory = False
            if dateArray[2] != self.lastDay:
                self.prop["details"]["completedMemmories"] = {}
                self.lastDay = dateArray[2]
            if self.mood > 100:
                self.mood = 100
            if self.mood < -100:
                self.mood = -100
            if self.activity > 10:
                self.activity = 10
            self.memmoryTrigger()
            if self.activeMemmory != False:
                wall = self.move(self.activeMemmory[1][0], self.activeMemmory[1][1])
                if wall == False:
                    # self.wallAnger = self.wallAnger + math.fabs((self.mood / 100))
                    self.move(self.activeMemmory[1][0], self.activeMemmory[1][1], (random.random() * 2) - 1, self.wallAnger * tools.getMin(self.getRot(self.activeMemmory[1][0], self.activeMemmory[1][1])))
                    self.mood = self.mood - (5 / (self.prop["details"]["hatrid"] - self.prop["details"]["love"]))
                else:
                    self.wallAnger = self.wallAnger - math.fabs((self.mood / 400))
                    if self.wallAnger < 1:
                        self.wallAnger = 1
                if ((self.x - 5) < self.activeMemmory[1][0] < (self.x + 5)) or (self.wallAnger > 200):
                    if ((self.y - 5) < self.activeMemmory[1][1] < (self.y + 5)) or (self.wallAnger > 200):
                        self.prop["details"]["completedMemmories"][str(self.activeMemmory)] = True
                        print("Memmory " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been completed.")
                        self.activeMemmory = False
            else:
                if self.mood < 0:
                    n = random.random() < (0.1 / ((10 - self.activity) + 1))
                    if n:
                        soundEvents = pytools.IO.getJson("soundEvents.json")
                        try:
                            h = True
                            for n in soundEvents:
                                if h:
                                    if (pytools.clock.dateArrayToUTC(soundEvents[n]) + 30) > pytools.clock.dateArrayToUTC(dateArray):
                                        self.activeMemmory = [pytools.clock.getDateTime(), pytools.IO.getJson("mics.json")[sr.Microphone.get_pyaudio().PyAudio().get_device_info_by_index(int(n))["name"]]]
                                        self.mood = self.mood - 3
                                        h = False
                        except:
                            pass
                        print("Ghost reaction response " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been triggered.")
                    if self.activeMemmory == False:
                        n = random.random() * random.random() < ((0.1 / (10 - self.activity)) * random.random() * random.random() * random.random())
                        if n:
                            self.activeMemmory = [pytools.clock.getDateTime(), [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]]
                    self.move(self.x, self.y, (random.random() * 2) - 1, (self.activity / 10))
                    n = random.random() < (((0.1 / ((10 - self.activity) + 1)) / self.speechModifier))
                    if n:
                        try:
                            ghostWords = pytools.IO.getJson("ghost_pg_words.json")
                            words = ghostWords["words"][int(math.floor(random.random() * len(ghostWords["words"])))]
                            sentence = words.replace(",").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                            k = 0
                            while (sentence == "") and (k < 100):
                                sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                k = k + 1
                            self.speak(sentence, self.prop["type"])
                            print(str(n) + " pg-0")
                        except:
                            pass
                else:
                    if self.activeMemmory == False:
                        n = random.random() * random.random() < ((0.1 / ((10 - self.activity) + 1)) * random.random() * random.random() * random.random())
                        if n:
                            self.activeMemmory = [pytools.clock.getDateTime(), [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]]
                        n = ((0.5 + (0.5 * (1 - math.fabs((self.mood / 100))))) * (random.random())) < (((0.1 / ((10 - self.activity) + 1)) * random.random() * random.random() * random.random()) / self.speechModifier)
                        if n:
                            self.activeMemmory = [pytools.clock.getDateTime(), [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]]
                            try:
                                ghostWords = pytools.IO.getJson("ghost_pg_words.json")
                                words = ghostWords["words"][int(math.floor(random.random() * len(ghostWords["words"])))]
                                sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                k = 0
                                while (sentence == "") and (k < 100):
                                    sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                    k = k + 1
                                self.speak(sentence, self.prop["type"])
                                print(str(n) + " pg-1")
                            except:
                                pass
                        n = random.random() < (0.1 / ((10 - self.activity) + 1))
                        soundEvents = pytools.IO.getJson("soundEvents.json")
                        k = False
                        try:
                            h = True
                            for n in soundEvents:
                                if h:
                                    if (pytools.clock.dateArrayToUTC(soundEvents[n]) + 30) > pytools.clock.dateArrayToUTC(dateArray):
                                        self.activeMemmory = [pytools.clock.getDateTime(), pytools.IO.getJson("mics.json")[sr.Microphone.get_pyaudio().PyAudio().get_device_info_by_index(int(n))["name"]]]
                                        k = True
                                        self.mood = self.mood - 3
                                        h = False
                        except:
                            pass
                        if k:
                            print("Ghost reaction response " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been triggered.")
                        if (self.activeMemmory == False) and n:
                            soundEvents = pytools.IO.getJson("soundEvents.json")
                            try:
                                h = True
                                for n in soundEvents:
                                    if h:
                                        if (pytools.clock.dateArrayToUTC(soundEvents[n]) + 30) > pytools.clock.dateArrayToUTC(dateArray):
                                            if self.mood < -20:
                                                self.activeMemmory = [pytools.clock.getDateTime(), pytools.IO.getJson("mics.json")[n]]
                                            try:
                                                ghostWords = pytools.IO.getJson("ghost_pg_words.json")
                                                transcript = pytools.IO.getFile("transcript.cxl").split("\n")
                                                indexf = int(math.floor(random.random() * len(transcript)))
                                                words = ghostWords["words"][int(math.floor(random.random() * len(ghostWords["words"])))]
                                                sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                                k = 0
                                                while (sentence == "") and (k < 100):
                                                    sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                                    k = k + 1
                                                self.speak(sentence + ". " + transcript[indexf], self.prop["type"])
                                                print(str(n) + " pg-2")
                                            except:
                                                pass
                                            self.mood = self.mood - 3
                                            h = False
                            except:
                                pass
                    self.rotation = ((self.rotation * 10) + ((random.random() * 2) - 1)) / 11
                    self.move(self.x, self.y, self.rotation, 2 * ((self.activity / 10) * (-1 * (self.mood / 100))))
        
        def demon(selff, dateArray):
            self = selff
            self.activity = self.getActivity(self.prop["details"]["activity"]) * self.getSpm()
            self.mood = ((self.mood * 3) + (((16 * random.random()) - 1)) / 4) + (0.1 * random.random() * self.prop["details"]["hatrid"]) + (0.1 * random.random() * self.prop["details"]["love"]) 
            if self.wallAnger > 200:
                if self.activeMemmory != False:
                    self.prop["details"]["completedMemmories"][str(self.activeMemmory)] = True
                    print("Memmory " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been terminated out of anger.")
                    self.activeMemmory = False
            if dateArray[2] != self.lastDay:
                self.prop["details"]["completedMemmories"] = {}
                self.lastDay = dateArray[2]
            if self.mood > 100:
                self.mood = 100
            if self.mood < -100:
                self.mood = -100
            if self.activity > 10:
                self.activity = 10
            self.memmoryTrigger()
            if self.activeMemmory != False:
                wall = self.move(self.activeMemmory[1][0], self.activeMemmory[1][1])
                if wall == False:
                    # self.wallAnger = self.wallAnger + math.fabs((self.mood / 100))
                    self.move(self.activeMemmory[1][0], self.activeMemmory[1][1], (random.random() * 2) - 1, self.wallAnger * tools.getMin(self.getRot(self.activeMemmory[1][0], self.activeMemmory[1][1])))
                    self.mood = self.mood - (5 / (self.prop["details"]["hatrid"] - self.prop["details"]["love"]))
                else:
                    self.wallAnger = self.wallAnger - math.fabs((self.mood / 400))
                    if self.wallAnger < 1:
                        self.wallAnger = 1
                if ((self.x - 5) < self.activeMemmory[1][0] < (self.x + 5)) or (self.wallAnger > 200):
                    if ((self.y - 5) < self.activeMemmory[1][1] < (self.y + 5)) or (self.wallAnger > 200):
                        self.prop["details"]["completedMemmories"][str(self.activeMemmory)] = True
                        print("Memmory " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been completed.")
                        self.activeMemmory = False
            else:
                if self.mood < 0:
                    n = random.random() < (0.1 / ((10 - self.activity) + 1))
                    if n:
                        soundEvents = pytools.IO.getJson("soundEvents.json")
                        try:
                            h = True
                            for n in soundEvents:
                                if h:
                                    if (pytools.clock.dateArrayToUTC(soundEvents[n]) + 30) > pytools.clock.dateArrayToUTC(dateArray):
                                        self.activeMemmory = [pytools.clock.getDateTime(), pytools.IO.getJson("mics.json")[sr.Microphone.get_pyaudio().PyAudio().get_device_info_by_index(int(n))["name"]]]
                                        self.mood = self.mood - 8
                                        h = False
                        except:
                            pass
                        if self.activeMemmory != False:
                            print("Ghost reaction response " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been triggered.")
                    n = random.random() < (0.1 / ((10 - self.activity) + 1))
                    if (self.activeMemmory == False) and n:
                        transcript = pytools.IO.getFile("transcript.cxl").split("\n")
                        try:
                            indexf = int(math.floor(random.random() * len(transcript)))
                            self.activeMemmory = [pytools.clock.getDateTime(), pytools.IO.getJson("mics.json")[transcript[indexf].split(";")[1]]]
                        except:
                            pass
                        print("Ghost communication response " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been triggered.")
                    if self.activeMemmory == False:
                        n = random.random() * random.random() < ((0.1 / (10 - self.activity)) * random.random() * random.random() * random.random())
                        if n:
                            self.activeMemmory = [pytools.clock.getDateTime(), [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]]
                    self.move(self.x, self.y, (random.random() * 2) - 1, (self.activity / 10))
                    n = random.random() < ((0.1 / ((10 - self.activity) + 1)) / self.speechModifier)
                    if n:
                        try:
                                ghostWords = pytools.IO.getJson("ghost_dm_words.json")
                                transcript = pytools.IO.getFile("transcript.cxl").split("\n")
                                indexf = int(math.floor(random.random() * len(transcript)))
                                words = ghostWords["words"][int(math.floor(random.random() * len(ghostWords["words"])))]
                                sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                k = 0
                                while (sentence == "") and (k < 100):
                                    sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                    k = k + 1
                                self.speak(sentence + ". " + transcript[indexf], self.prop["type"])
                                print(str(n) + " demon-0")
                        except:
                            pass
                else:
                    if self.activeMemmory == False:
                        n = random.random() * random.random() < (((0.1 / ((10 - self.activity) + 1)) * random.random() * random.random() * random.random()))
                        if n:
                            self.activeMemmory = [pytools.clock.getDateTime(), [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]]
                        n = ((0.5 + (0.5 * (1 - math.fabs((self.mood / 100))))) * (random.random())) < (((0.1 / ((10 - self.activity) + 1)) * random.random() * random.random() * random.random()) / self.speechModifier)
                        if n:
                            self.activeMemmory = [pytools.clock.getDateTime(), [floorplan.level[0][1][0] * random.random(), floorplan.level[0][1][1] * random.random()]]
                            try:
                                ghostWords = pytools.IO.getJson("ghost_dm_words.json")
                                transcript = pytools.IO.getFile("transcript.cxl").split("\n")
                                indexf = int(math.floor(random.random() * len(transcript)))
                                words = ghostWords["words"][int(math.floor(random.random() * len(ghostWords["words"])))]
                                sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                k = 0
                                while (sentence == "") and (k < 100):
                                    sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                    k = k + 1
                                self.speak(sentence + ". " + transcript[indexf], self.prop["type"])
                                print(str(n) + " demon-1")
                            except:
                                pass
                        soundEvents = pytools.IO.getJson("soundEvents.json")
                        k = False
                        try:
                            h = True
                            for n in soundEvents:
                                if h:
                                    if (pytools.clock.dateArrayToUTC(soundEvents[n]) + 30) > pytools.clock.dateArrayToUTC(dateArray):
                                        self.activeMemmory = [pytools.clock.getDateTime(), pytools.IO.getJson("mics.json")[sr.Microphone.get_pyaudio().PyAudio().get_device_info_by_index(int(n))["name"]]]
                                        self.mood = self.mood - 3
                                        h = False
                                        k = True
                        except:
                            pass
                        if k:
                            print("Ghost reaction response " + str(self.activeMemmory) + " for ghost " + self.prop["name"] + " of type " + str(self.prop["type"]) + " has been triggered.")
                        if (self.activeMemmory == False) and n:
                            soundEvents = pytools.IO.getJson("soundEvents.json")
                            try:
                                h = True
                                for n in soundEvents:
                                    if h:
                                        if (pytools.clock.dateArrayToUTC(soundEvents[n]) + 30) > pytools.clock.dateArrayToUTC(dateArray):
                                            if self.mood < -20:
                                                self.activeMemmory = [pytools.clock.getDateTime(), pytools.IO.getJson("mics.json")[n]]
                                            try:
                                                ghostWords = pytools.IO.getJson("ghost_dm_words.json")
                                                transcript = pytools.IO.getFile("transcript.cxl").split("\n")
                                                indexf = int(math.floor(random.random() * len(transcript)))
                                                words = ghostWords["words"][int(math.floor(random.random() * len(ghostWords["words"])))]
                                                sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                                k = 0
                                                while (sentence == "") and (k < 100):
                                                    sentence = words.replace(",", ".").split(".")[int(math.floor(random.random() * len(words.replace(",", ".").split("."))))]
                                                    k = k + 1
                                                self.speak(sentence + ". " + transcript[indexf], self.prop["type"])
                                                print(str(n) + " demon-2")
                                            except:
                                                pass
                                            self.mood = self.mood - 8
                                            h = False
                            except:
                                pass
                    self.rotation = ((self.rotation * 10) + ((random.random() * 2) - 1)) / 11
                    self.move(self.x, self.y, self.rotation, 2 * ((self.activity / 10) * (-1 * (self.mood / 100))))
    
    def tic(self):
        dateArray = pytools.clock.getDateTime()
        self.speechModifier = self.sM / (self.activity + 1)
        if self.prop["type"] == type.echo:
            self.ai.echo(self, dateArray)
        if self.prop["type"] == type.spirit:
            self.ai.spirit(self, dateArray)
        if self.prop["type"] == type.poltergeist:
            self.ai.poltergeist(self, dateArray)
        if self.prop["type"] == type.demon:
            self.ai.demon(self, dateArray)
            
            
def main():
    floorplan.loadLevel(0)
    ghostsf = pytools.IO.getJson("ghosts.json")
    for n in ghostsf["list"]:
        if n["type"] != 4:
            haunts.register(n)
    while True:
        haunts.handler.handle()
        for n in haunts.ghosts:
            haunts.ghosts[n].tic()
        time.sleep(0.1)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True
            
def run():
    main()