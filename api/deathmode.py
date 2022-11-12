import pytools
import random
import time
import os
import math

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": [],
        "whisperIndex": 0,
        "hallowedWolfIndex": 0,
        "ghosts": {},
        "monsters": {},
        "death_wind": {}
    }

class globals:
    class deathWind:
       state = 0
       run = 0
       nextPlay = 0
    class monsters:
        state = 0
        run = 0
        nextPlay = 0
    class ghosts:
        state = 0
        run = 0
        nextPlay = 0

class utils:
    def dayTimesGrabber():
        dayTimes = pytools.IO.getList('daytimes.pyl')[1]
        if dayTimes == 1:
            dayTimes = [[2022, 5, 11, 3, 45, 15], [2022, 5, 11, 4, 34, 10], [2022, 5, 11, 5, 16, 33], [2022, 5, 11, 5, 48, 29], [2022, 5, 11, 13, 10, 47], [2022, 5, 11, 20, 33, 6], [2022, 5, 11, 21, 5, 2], [2022, 5, 11, 21, 47, 25], [2022, 5, 11, 22, 36, 20]]
        return dayTimes

class background:

    class whispers:
        def calc(dateArray, dayTimes):
            try:
                timef = dateArray
                timef[2] = dateArray[2] - 1
                start = pytools.clock.dateArrayToUTC(pytools.clock.getMidnight(timef))
                midnight = pytools.clock.dateArrayToUTC(pytools.clock.getMidnight(dateArray))
                current = pytools.clock.dateArrayToUTC(dateArray)
                x = 86400 + (current - start)
                g = 86400 - (86400 - (pytools.clock.dateArrayToUTC(dayTimes[5]) - midnight))
                while g > 86400:
                    g = g - 86400
                while x > 86400:
                    x = x - 86400
                
                e = 2.71828182846
                a = 10
                f = 0.000000004
                k = 120
                r = 0.0008
                j = 0.000000002
                n = a * (e ** (-f * ((x - 86000) ** 2)))
                l = k * (e ** ((-3) * r * ((x - g - 100) ** 1.12)))
                try:
                    pass
                    #l = math.fabs(float(l))
                except:
                    pass
                    #l = math.fabs(float(l.real))
                l = (2.5 * k) * (1 / ((2 * 3.14) ** 0.5) * (e ** (-1 * (((x - g - 100) ** 2) / (20 * k)))))
                s = 5 * (e ** (-j * ((x - g - 5400) ** 2)))
                m = 0.5 * a * (e ** (-2 * f * ((x - 86000 - 3600) ** 2)))
                d = 6 * a * (e ** (-150 * f * ((x - 86400) ** 2)))
                o = -1024 ** (x - 86400)
                h = 6 * a * (e ** (-15000 * f * ((x - 86400) ** 2)))
                if dateArray[1] == 10:
                    l = l / ((31 / dateArray[2]) ** 7)
                    d = d / ((31 / dateArray[2]) ** 16)
                    h = h / ((31 / dateArray[2]) ** 92)
                else:
                    l = l / 3
                    d = d / ((31 / 25) ** 16)
                    h = h / ((31 / 25) ** 92)
                out = n + l + s + m + d + o + h
                if out < 0:
                    out = 0
            except:
                out = 0
                
            print('Current whisper chance: ' + str(out))
            status.vars['whisperIndex'] = out
            return out

        def run(dateArray, dayTimes):
            whisperChance = background.whispers.calc(dateArray, dayTimes)
            if random.randint(0, 100) < whisperChance:
                ghSpeaker = 5
                while ghSpeaker == 5:
                    ghSpeaker = random.randint(0, 8)
                min = int(math.floor(25 + (whisperChance / 4)))
                max = int(math.floor(60 + (whisperChance / 2.5)))
                if min < 0:
                    min = 0
                if min > 100:
                    min = 100
                if max < 0:
                    max = 0
                if max > 100:
                    max = 100
                pytools.sound.main.playSound("whispering.mp3", ghSpeaker, random.randint(min, max), (random.random() / 3) + 0.6 + 0.15, 0, 0)
                
    def death_wind(dateArray, dayTimes):
        startf = dayTimes[5]
        startf[4] = startf[4] + 11
        if startf[4] > 60:
            startf[4] = startf[4] - 60
            startf[3] = startf[3] + 1
        endf = dayTimes[2]
        endf[4] = endf[4] - 11
        if endf[4] < 0:
            end[4] = endf[4] + 60
            end[3] = endf[3] - 1
        if dateArray[3] > 12:
            endf[2] = endf[2] + 1
            if endf[2] > pytools.clock.getMonthEnd(endf[1]):
                endf[1] = endf[1] + 1
                if endf[1] > 12:
                    endf[1] = 1
                    endf[0] = endf[0] + 1
        else:
            startf[2] = startf[2] - 1
            if startf[2] < 1:
                startf[1] = startf[1] - 1
                if startf[1] < 1:
                    startf[1] = 12
                    startf[0] = startf[0] - 1
        start = pytools.clock.dateArrayToUTC(startf)
        current = pytools.clock.dateArrayToUTC(dateArray)
        end = pytools.clock.dateArrayToUTC(endf)
        print(dateArray)
        print(startf, dateArray, endf)
        print([start, current, end])
        if (start < current) and (current < end):
            globals.deathWind.run = 1
            if globals.deathWind.state != 1:
                globals.deathWind.state = 1
                globals.deathWind.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 500
                pytools.sound.main.playSoundWindow("death_wind_fi.mp3;death_wind_fi.mp3", [10, 50], 1.0, 0.0, 0)
            if globals.deathWind.state == 1:
                if globals.deathWind.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                    globals.deathWind.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 194
                    pytools.sound.main.playSoundWindow("death_wind.mp3;death_wind.mp3", [10, 50], 1.0, 0.0, 0)
        status.vars["death_wind"]["nextPlay"] = globals.deathWind.nextPlay
        status.vars["death_wind"]["state"] = globals.deathWind.state

    def monsters(dateArray, dayTimes):
        dayTimes = utils.dayTimesGrabber()
        startf = dayTimes[5]
        startf[4] = startf[4] + 26
        if startf[4] > 60:
            startf[4] = startf[4] - 60
            startf[3] = startf[3] + 1
        endf = dayTimes[2]
        endf[4] = endf[4] - 26
        if endf[4] < 0:
            endf[4] = endf[4] + 60
            endf[3] = endf[3] - 1
        if dateArray[3] > 12:
            endf[2] = endf[2] + 1
            if endf[2] > pytools.clock.getMonthEnd(endf[1]):
                endf[1] = endf[1] + 1
                if endf[1] > 12:
                    endf[1] = 1
                    endf[0] = endf[0] + 1
        else:
            startf[2] = startf[2] - 1
            if startf[2] < 1:
                startf[1] = startf[1] - 1
                if startf[1] < 1:
                    startf[1] = 12
                    startf[0] = startf[0] - 1
        start = pytools.clock.dateArrayToUTC(startf)
        current = pytools.clock.dateArrayToUTC(dateArray)
        end = pytools.clock.dateArrayToUTC(endf)
        print("Monsters: " + str(start) + " ;;; " + str(current))
        midnight = pytools.clock.dateArrayToUTC(pytools.clock.getMidnight(dateArray))
        dis = midnight - start
        dayMod = ((((current - midnight) + 86400) / ((start - midnight) + 86400)) ** 16)
        if dayMod > 1:
            dayMod = 1
        wolfChance = ((20 * (2.71828182846 ** -(((((current - midnight) * 0.00016) * (dis / 10854)) ** 2)))) / 2) * dayMod
        if dateArray[1] == 10:
            wolfChance = wolfChance / ((31 / dateArray[2]) ** 4)
        if random.randrange(0, 100) < wolfChance:
            if os.path.isfile('.\\nomufflewn.derp') == True:
                pytools.sound.main.playSound('wolf_howl_' + str(random.randrange(0, 3)) + ".mp3", 4, 40, 1, 0, 0)
            else:
                pytools.sound.main.playSound('wolf_howl_' + str(random.randrange(0, 3)) + "_m.mp3", 2, 40, 1, 0, 0)
                pytools.sound.main.playSound('wolf_howl_' + str(random.randrange(0, 3)) + ".mp3", 3, 40, 1, 0, 0)
        status.vars['hallowedWolfIndex'] = wolfChance
        if (start < current) and (current < end):
            globals.monsters.run = 1
            if globals.monsters.state == 0:
                globals.monsters.state = 1
                globals.monsters.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 500
                pytools.sound.main.playSoundWindow("monsters_fi.mp3;monsters_fi.mp3", [20, 50], 1.0, 0.0, 0)
            if globals.monsters.state == 1:
                if globals.monsters.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                    globals.monsters.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 194
                    pytools.sound.main.playSoundWindow("monsters.mp3;monsters.mp3", [20, 50], 1.0, 0.0, 0)
        status.vars["monsters"]["nextPlay"] = globals.monsters.nextPlay
        status.vars["monsters"]["state"] = globals.monsters.state
    
    def ghosts(dateArray, dayTimes):
        startf = dayTimes[6]
        current = pytools.clock.dateArrayToUTC(dateArray)
        endf = dayTimes[1]
        if dateArray[3] > 12:
            endf[2] = endf[2] + 1
            if endf[2] > pytools.clock.getMonthEnd(endf[1]):
                endf[1] = endf[1] + 1
                if endf[1] > 12:
                    endf[1] = 1
                    endf[0] = endf[0] + 1
        else:
            startf[2] = startf[2] - 1
            if startf[2] < 1:
                startf[1] = startf[1] - 1
                if startf[1] < 1:
                    startf[1] = 12
                    startf[0] = startf[0] - 1
        end = pytools.clock.dateArrayToUTC(endf)
        start = pytools.clock.dateArrayToUTC(dayTimes[6])
        if (start < current) and (current < end):
            globals.ghosts.run = 1
            if globals.ghosts.state == 0:
                globals.ghosts.state = 1
                globals.ghosts.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 500
                pytools.sound.main.playSoundWindow("ghosts_fi.mp3;ghosts_fi.mp3", [20, 50], 1.0, 0.0, 0)
            if globals.ghosts.state == 1:
                if globals.ghosts.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                    globals.ghosts.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 194
                    pytools.sound.main.playSoundWindow("ghosts.mp3;ghosts.mp3", [20, 50], 1.0, 0.0, 0)
        status.vars["ghosts"]["nextPlay"] = globals.ghosts.nextPlay
        status.vars["ghosts"]["state"] = globals.ghosts.state
    
    def end():
        if globals.ghosts.run == 0:
            if globals.ghosts.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                if globals.ghosts.state == 1:
                    globals.ghosts.state = 0
                    pytools.sound.main.playSoundWindow("ghosts_fo.mp3;ghosts_fo.mp3", [20, 50], 1.0, 0.0, 0)
        if globals.monsters.run == 0:
            if globals.monsters.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                if globals.monsters.state == 1:
                    globals.monsters.state = 0
                    pytools.sound.main.playSoundWindow("monsters_fo.mp3;monsters_fo.mp3", [20, 50], 1.0, 0.0, 0)
        if globals.deathWind.run == 0:
            if globals.deathWind.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                if globals.deathWind.state == 1:
                        globals.deathWind.state = 0
                        pytools.sound.main.playSoundWindow("death_wind_fo.mp3;death_wind_fo.mp3", [20, 50], 1.0, 0.0, 0)
def main():
    while True:
        dateArray = pytools.clock.getDateTime()
        dayTimes = utils.dayTimesGrabber()
        dayOfWeek = pytools.clock.getDayOfWeek()
        globals.deathWind.run = 0
        globals.monsters.run = 0
        globals.ghosts.run = 0
        wait = 600
        if dateArray[2] == 13:
            if dayOfWeek == 5:
                if dateArray[3] > 11:
                    background.whispers.run(dateArray, dayTimes)
                    wait = 1
                    dateArray = pytools.clock.getDateTime()
                    background.death_wind(dateArray, dayTimes)
                    if 9 <= dateArray[1] <= 11:
                        background.monsters(dateArray, dayTimes)
                        dateArray = pytools.clock.getDateTime()
                    elif dateArray[3] > 22:
                        background.monsters(dateArray, dayTimes)
                        dateArray = pytools.clock.getDateTime()
        elif dateArray[2] == 14:
            if dayOfWeek == 6:
                if dateArray[3] < 12:
                    background.whispers.run(dateArray, dayTimes)
                    wait = 1
                    dateArray = pytools.clock.getDateTime()
                    background.death_wind(dateArray, dayTimes)
                    if 9 <= dateArray[1] <= 11:
                        background.monsters(dateArray, dayTimes)
                        dateArray = pytools.clock.getDateTime()
        if ((dateArray[1] == 10) and (((dateArray[2] == 1) and (dateArray[3] > 12)) or (dateArray[2] > 1))) or ((dateArray[1] == 11) and (dateArray[2] == 1) and (dateArray[3] < 12)):
            background.whispers.run(dateArray, dayTimes)
            wait = 1
            dateArray = pytools.clock.getDateTime()
            if (dateArray[2] >= 29) or ((dateArray[1] == 11) and (dateArray[2] <= 1)):
                background.death_wind(dateArray, dayTimes)
                dateArray = pytools.clock.getDateTime()
            if (dateArray[2] >= 30) or ((dateArray[1] == 11) and (dateArray[2] <= 1)):
                background.monsters(dateArray, dayTimes)
                dateArray = pytools.clock.getDateTime()
            if (dateArray[2] == 31) or ((dateArray[1] == 11) and (dateArray[2] <= 1)):
                background.ghosts(dateArray, dayTimes)
                dateArray = pytools.clock.getDateTime()
        background.end()
        time.sleep(wait)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()
            


