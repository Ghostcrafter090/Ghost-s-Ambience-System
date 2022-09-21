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
        texts = pytools.net.getTextAPI("https://www.weather.gc.ca/warnings/report_e.html?ns1").split(" Access city")[1].split("Weather shortcuts")[0].split("\n")
        out = True
        for n in texts:
            if n.find("No Alerts in effect") != -1:
                out = False
        if out:
            if globals.textsf != texts:
                pytools.sound.main.playSoundWindow("alert_incoming.mp3;alert_incoming.mp3", 50, 1.0, 0.0, 1)
                for n in texts:
                    try:
                        gtts.gTTS(text=n, lang="en", slow=False).save(".\\sound\\assets\\alerts.mp3")
                        pytools.sound.main.playSoundWindow("alerts.mp3;alerts.mp3", 50, 1.0, 0.0, 1)
                    except:
                        pass
                pytools.sound.main.playSoundWindow("alert_incoming.mp3;alert_end.mp3", 50, 1.0, 0.0, 1)
                globals.textsf = texts
            if (dateArray[3] % 4) == 0:
                if (dateArray[4] % 60) == 0:
                    pytools.sound.main.playSoundWindow("alert_reproduce.mp3;alert_reproduce.mp3", 50, 1.0, 0.0, 1)
                    for n in texts:
                        try:
                            gtts.gTTS(text=n, lang="en", slow=False).save(".\\sound\\assets\\alerts.mp3")
                            pytools.sound.main.playSoundWindow("alerts.mp3;alerts.mp3", 50, 1.0, 0.0, 1)
                        except:
                            pass
                    pytools.sound.main.playSoundWindow("alert_incoming.mp3;alert_end.mp3", 50, 1.0, 0.0, 1)
        time.sleep(10)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True
    
def run():
    main()