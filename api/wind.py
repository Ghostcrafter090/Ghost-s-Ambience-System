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
    def lightChimneyWind():
        pytools.sound.main.playSound("light_chimney_wind.mp3", 1, 10, 1.0, 0.0, 0)
    
    def lightWind():
        pytools.sound.main.playSound("light_wind.mp3", 0, 10, 1.0, 0.0, 0)
        pytools.sound.main.playSound("light_wind.mp3", 1, 10, 1.0, 0.0, 0)
        pytools.sound.main.playSoundWindow("light_wind.mp3;light_wind_nm.mp3", [20, 50], 1.0, 0.0, 0)
    
    def wind():
        pytools.sound.main.playSoundWindow("wind.mp3;wind_nm.mp3", [10, 50], 1.0, 0.0, 0)
    
    def chimneyWind():
        pytools.sound.main.playSound("chimney_wind.mp3", 1, 10, 1.0, 0.0, 0)

    def hurricaneWind():
        pytools.sound.main.playSound("hurricane_wail.mp3", 0, 10, 1.0, 0.0, 0)
        pytools.sound.main.playSound("hurricane_wail.mp3", 1, 10, 1.0, 0.0, 0)
        pytools.sound.main.playSoundWindow("hurricane_wail.mp3;hurricane_wail_nm.mp3", [10, 50], 1.0, 0.0, 0)

def main():
    while True:
        dataList = utils.dataGrabber()
        if (dataList[0][1] > 13) or (dataList[0][0] > 11):
            sounds.lightChimneyWind()
        if (dataList[0][1] > 15) or (dataList[0][0] > 9):
            sounds.lightWind()
        if (dataList[0][1] > 19) or (dataList[0][0] > 17):
            sounds.wind()
        if (dataList[0][1] > 27) or (dataList[0][0] > 23):
            sounds.chimneyWind()
        if (dataList[0][1] > 30) or (dataList[0][0] > 30):
            sounds.hurricaneWind()
        time.sleep(194)

def run():
    main()
    
    

