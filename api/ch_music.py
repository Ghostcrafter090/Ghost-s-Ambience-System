import pytools
import time
import random

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

def playMusic():
    mp3 = 'ch_music_' + str(random.randint(0, 2)) + ".mp3"
    pytools.sound.main.playSoundWindow(mp3, 50, 1.0, 0, 1)

def music(dateArray):
    if dateArray[3] > 9:
        if dateArray[3] < 16:
            if (11 < dateArray[3] < 12) == False:
                if (dateArray[4] < 10) == False:
                    if dateArray[4] < 40:
                        playMusic()

def main():
    while True:
        dateArray = pytools.clock.getDateTime()
        if dateArray[1] == 11:
            if dateArray[2] > 11:
                music()
        if dateArray[1] == 12:
            music()
        time.sleep(194)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()