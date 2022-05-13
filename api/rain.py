import pytools
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

class sounds:
    def rain():
        pytools.sound.main.playSoundWindow("rain.mp3;rain_nm.mp3", [20, 30], 1.0, 0.0, 0)
        pytools.sound.main.playSound("lightrain_wall.mp3", 0, 50, 1.0, 0.0, 0)
        pytools.sound.main.playSound("lightrain_wall.mp3", 1, 50, 1.0, 0.0, 0)

    def lightRain():
        pytools.sound.main.playSoundWindow("lightrain.mp3;lightrain_nm.mp3", [50, 50], 1.0, 0.0, 0)
        pytools.sound.main.playSound("lightrain_wall.mp3", 0, 35, 1.0, 0.0, 0)
        pytools.sound.main.playSound("lightrain_wall.mp3", 1, 35, 1.0, 0.0, 0)
    
    def mist():
        pytools.sound.main.playSoundWindow("lightrain.mp3;mist_nm.mp3", [25, 50], 1.0, 0.0, 0)
    
def main():
    while True:
        dataList = utils.dataGrabber()
        if dataList[0][4] == "rain":
            sounds.rain()
        if dataList[0][4] == "lightrain":
            sounds.lightRain()
        if dataList[0][4] == "mist":
            sounds.mist()
        if dataList[0][4] == "thunder":
            sounds.rain()
        time.sleep(194)

def run():
    main()
            
        
