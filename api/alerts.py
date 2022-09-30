import pytools
import gtts
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

class globals:
    textsf = [""]

def main():
    while True:
        dateArray = pytools.clock.getDateTime()
        try:
            dayTimes = pytools.IO.getList("dayTimes.pyl")[1]
        except:
            dayTimes = [[2022, 10, 21, 6, 0, 22], [2022, 10, 21, 6, 34, 14], [2022, 10, 21, 7, 8, 19], [2022, 10, 21, 7, 36, 33], [2022, 10, 21, 12, 59, 1], [2022, 10, 21, 18, 21, 28], [2022, 10, 21, 18, 49, 43], [2022, 10, 21, 19, 23, 47], [2022, 10, 21, 19, 57, 39]]
        try:
            texts = pytools.net.getTextAPI("https://www.weather.gc.ca/warnings/report_e.html?ns1").split(" Access city")[1].split("Weather shortcuts")[0].split("\n")
        except:
            texts = globals.textsf
        out = True
        for n in texts:
            if n.find("No Alerts in effect") != -1:
                out = False
        if out:
            if globals.textsf != texts:
                if (pytools.clock.dateArrayToUTC(dayTimes[3]) < pytools.clock.dateArrayToUTC(dateArray) < pytools.clock.dateArrayToUTC(dayTimes[5])):
                    pytools.sound.main.playSoundWindow("alert_incoming.mp3;alert_incoming.mp3", 25, 1.0, 0.0, 1)
                else:
                    pytools.sound.main.playSoundWindow("alert_incoming_night.mp3;alert_incoming_night.mp3", 10, 1.0, 0.0, 1)
                for n in texts:
                    try:
                        gtts.gTTS(text=n, lang="en", slow=False).save(".\\sound\\assets\\alerts.mp3")
                        if (pytools.clock.dateArrayToUTC(dayTimes[3]) < pytools.clock.dateArrayToUTC(dateArray) < pytools.clock.dateArrayToUTC(dayTimes[5])):
                            pytools.sound.main.playSoundWindow("alerts.mp3;alerts.mp3", 25, 1.0, 0.0, 1)
                        else:
                            pytools.sound.main.playSoundWindow("alerts.mp3;alerts.mp3", 15, 1.0, 0.0, 1)
                    except:
                        pass
                if (pytools.clock.dateArrayToUTC(dayTimes[3]) < pytools.clock.dateArrayToUTC(dateArray) < pytools.clock.dateArrayToUTC(dayTimes[5])):
                    pytools.sound.main.playSoundWindow("alert_end.mp3;alert_end.mp3", 25, 1.0, 0.0, 1)
                else:
                    pytools.sound.main.playSoundWindow("alert_end_night.mp3;alert_end_night.mp3", 10, 1.0, 0.0, 1)
                globals.textsf = texts
            if (dateArray[3] % 6) == 0:
                if (dateArray[4] % 60) == 0:
                    if (pytools.clock.dateArrayToUTC(dayTimes[3]) < pytools.clock.dateArrayToUTC(dateArray) < pytools.clock.dateArrayToUTC(dayTimes[5])):
                        pytools.sound.main.playSoundWindow("alert_reproduce.mp3;alert_reproduce.mp3", 25, 1.0, 0.0, 1)
                    else:
                        pytools.sound.main.playSoundWindow("alert_reproduce_night.mp3;alert_reproduce_night.mp3", 10, 1.0, 0.0, 1)
                    for n in texts:
                        try:
                            gtts.gTTS(text=n, lang="en", slow=False).save(".\\sound\\assets\\alerts.mp3")
                            if (pytools.clock.dateArrayToUTC(dayTimes[3]) < pytools.clock.dateArrayToUTC(dateArray) < pytools.clock.dateArrayToUTC(dayTimes[5])):
                                pytools.sound.main.playSoundWindow("alerts.mp3;alerts.mp3", 25, 1.0, 0.0, 1)
                            else:
                                pytools.sound.main.playSoundWindow("alerts.mp3;alerts.mp3", 15, 1.0, 0.0, 1)
                        except:
                            pass
                    if (pytools.clock.dateArrayToUTC(dayTimes[3]) < pytools.clock.dateArrayToUTC(dateArray) < pytools.clock.dateArrayToUTC(dayTimes[5])):
                        pytools.sound.main.playSoundWindow("alert_end.mp3;alert_end.mp3", 25, 1.0, 0.0, 1)
                    else:
                        pytools.sound.main.playSoundWindow("alert_end_night.mp3;alert_end_night.mp3", 10, 1.0, 0.0, 1)
        time.sleep(10)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True
    
def run():
    main()