import pytools
import random
import time
import os

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

class globals:
    class deathWind:
       state = 0
       nextPlay = 0
    class monsters:
        state = 0
        nextPlay = 0
    class ghosts:
        state = 0
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
            timef = dateArray
            timef[2] = dateArray[2] - 1
            start = pytools.clock.dateArrayToUTC(pytools.clock.getMidnight(timef))
            midnight = pytools.clock.dateArrayToUTC(pytools.clock.getMidnight(dateArray))
            current = pytools.clock.dateArrayToUTC(dateArray)
            x = current - start
            g = midnight - pytools.clock.dateArrayToUTC(dayTimes[5])
            e = 2.71828182846
            a = 10
            f = 0.000000004
            k = 120
            r = 0.0008
            j = 0.000000002
            n = a * (e ** (-f * ((x - 86000) ** 2)))
            l = k * (e ** (-3 * r * ((x - g - 100) ** 1.12)))
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
            print('Current whisper chance: ' + str(out))
            return out

        def run(dateArray, dayTimes):
            if random.randint(0, 100) < background.whispers.calc(dateArray, dayTimes):
                pytools.sound.main.playSound("whispering.mp3", random.randint(0, 4), random.randint(50, 100), (random.random() / 3) + 0.6 + 0.15, 0, 0)

    def death_wind(dateArray, dayTimes):
        start = pytools.clock.dateArrayToUTC(pytools.clock.solveForDialation([0, 0, 0, 0, -11, 0], dayTimes[5]))
        current = pytools.clock.dateArrayToUTC(dateArray)
        if start < current:
            if globals.deathWind.state == 0:
                globals.deathWind.state = 1
                globals.deathWind.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 500
                pytools.sound.main.playSoundWindow("death_wind_fi.mp3;death_wind_fi.mp3", [10, 50], 1.0, 0.0, 0)
            if globals.deathWind.state == 1:
                if globals.deathWind.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                    globals.deathWind.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 194
                    pytools.sound.main.playSoundWindow("death_wind.mp3;death_wind.mp3", [10, 50], 1.0, 0.0, 0)
        else:
            if globals.deathWind.state == 1:
                globals.deathWind.state = 0
                pytools.sound.main.playSoundWindow("death_wind_fo.mp3;death_wind_fo.mp3", [10, 50], 1.0, 0.0, 0)

    def monsters(dateArray, dayTimes):
        start = pytools.clock.dateArrayToUTC(pytools.clock.solveForDialation([0, 0, 0, 0, -26, 0], dayTimes[5]))
        current = pytools.clock.dateArrayToUTC(dateArray)
        midnight = pytools.clock.dateArrayToUTC(pytools.clock.getMidnight(dateArray))
        dis = midnight - start
        wolfChance = 20 * (2.71828182846 ** -(((((current - midnight) * 0.00016) * (dis / 10854)) ** 2)))
        if dateArray[1] == 10:
            wolfChance = wolfChance / ((31 / dateArray[2]) ** 4)
        if random.randrange(0, 100) < wolfChance:
            if os.path.isfile('.\\nomufflewn.derp') == True:
                pytools.sound.main.playSound('wolf_howl_' + str(random.randrange(0, 3)) + ".mp3", 4, 40, 1, 0, 0)
            else:
                pytools.sound.main.playSound('wolf_howl_' + str(random.randrange(0, 3)) + "_m.mp3", 2, 40, 1, 0, 0)
                pytools.sound.main.playSound('wolf_howl_' + str(random.randrange(0, 3)) + ".mp3", 3, 40, 1, 0, 0)
        if start < current:
            if globals.monsters.state == 0:
                globals.monsters.state = 1
                globals.monsters.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 500
                pytools.sound.main.playSoundWindow("monsters_fi.mp3;monsters_fi.mp3", [10, 50], 1.0, 0.0, 0)
            if globals.monsters.state == 1:
                if globals.monsters.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                    globals.monsters.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 194
                    pytools.sound.main.playSoundWindow("monsters.mp3;monsters.mp3", [10, 50], 1.0, 0.0, 0)
        else:
            if globals.monsters.state == 1:
                globals.monsters.state = 0
                pytools.sound.main.playSoundWindow("monsters_fo.mp3;monsters_fo.mp3", [10, 50], 1.0, 0.0, 0)

    def ghosts(dateArray, dayTimes):
        start = pytools.clock.dateArrayToUTC(dayTimes[6])
        current = pytools.clock.dateArrayToUTC(dateArray)
        if start < current:
            if globals.ghosts.state == 0:
                globals.ghosts.state = 1
                globals.ghosts.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 500
                pytools.sound.main.playSoundWindow("ghosts_fi.mp3;ghosts_fi.mp3", [10, 50], 1.0, 0.0, 0)
            if globals.ghosts.state == 1:
                if globals.ghosts.nextPlay < pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                    globals.ghosts.nextPlay = pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()) + 194
                    pytools.sound.main.playSoundWindow("ghosts.mp3;ghosts.mp3", [10, 50], 1.0, 0.0, 0)
        else:
            if globals.ghosts.state == 1:
                globals.ghosts.state = 0
                pytools.sound.main.playSoundWindow("ghosts_fo.mp3;ghosts_fo.mp3", [10, 50], 1.0, 0.0, 0)

def main():
    while True:
        dateArray = pytools.clock.getDateTime()
        dayTimes = utils.dayTimesGrabber()
        dayOfWeek = pytools.clock.getDayOfWeek()
        wait = 600
        if dateArray[2] == 13:
            if dayOfWeek == 5:
                background.whispers.run(dateArray, dayTimes)
                wait = 1
                background.death_wind(dateArray, dayTimes)
                if 9 <= dateArray[1] <= 11:
                    background.monsters(dateArray, dayTimes)
        if dateArray[1] == 10:
            background.whispers.run(dateArray, dayTimes)
            wait = 1
            if dateArray[2] >= 29:
                background.death_wind(dateArray, dayTimes)
            if dateArray[2] >= 30:
                background.monsters(dateArray, dayTimes)
            if dateArray[2] == 31:
                background.ghosts(dateArray, dayTimes)
        time.sleep(wait)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()
            


