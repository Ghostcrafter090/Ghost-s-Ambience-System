from datetime import datetime
import os
import time
import pytools
import threading

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

class globals:
    isChime = False
    isGong = False

def getDate():
    sequence = str(datetime.now()).replace(" ", "-").replace(":", "-").replace(".", "-")
    list = sequence.split("-")
    return list

class mech:
    def chimePR():
        print(str(datetime.now()) + " ;; Playing whirr prep sound...")
        os.system('cmd.exe /c start /d ".\\sound\\clock" /b "" ..\..\clock.exe whirr_prep.vbs')
        time.sleep(60)

    def windCL():
        print(str(datetime.now()) + " ;; Playing christmas chime...")
        os.system('cmd.exe /c start /wait /b /d ".\\sound\\clock" "" ..\..\clock.exe winding_clock.vbs')
        time.sleep(60)
        
class whirr:
    def standard():
        globals.isChime = True
        while globals.isChime:
            pytools.sound.main.playSound("whirr_cont.mp3", 0, 50, 1.0, 0.0, 0, clock=False)
            time.sleep(1)
        pytools.sound.main.playSound("whirr_ed.mp3", 0, 50, 1.0, 0.0, 0, clock=False)
            
    def gong():
        globals.isGong = True
        while globals.isGong:
            pytools.sound.main.playSound("gong_whirr_cont.mp3", 0, 50, 1.0, 0.0, 0, clock=False)
            time.sleep(1)
        pytools.sound.main.playSound("gong_whirr_ed.mp3", 0, 50, 1.0, 0.0, 0, clock=False)
            
    

class chime:
    def chimeFH():
        print(str(datetime.now()) + " ;; Starting whirr effect...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe whirr_st.vbs')
        time.sleep(3)
        gongWhirr = threading.Thread(target=whirr.standard)
        gongWhirr.start()
        print(str(datetime.now()) + " ;; Playing hour chime...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe hcs.vbs')
        file = open(".\\clocks\\default\\hcs_config.txt", "r")
        hcst = int(file.read()) - 2
        file.close()
        print(str(datetime.now()) + " ;; Waiting for " + str(hcst) + " seconds...")
        time.sleep(hcst)
        print(str(datetime.now()) + " ;; Chime sequence finished.")
        globals.isChime = False
        
    def chimeQH():
        print(str(datetime.now()) + " ;; Starting whirr effect...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe whirr_st.vbs')
        time.sleep(3)
        gongWhirr = threading.Thread(target=whirr.standard)
        gongWhirr.start()
        print(str(datetime.now()) + " ;; Playing quarter hour chime...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe qhcs.vbs')
        file = open(".\\clocks\\default\\qhcs_config.txt", "r")
        hcst = int(file.read()) - 2
        file.close()
        print(str(datetime.now()) + " ;; Waiting for " + str(hcst) + " seconds...")
        time.sleep(hcst)
        print(str(datetime.now()) + " ;; Chime sequence finished.")
        globals.isChime = False
        
    def chimeHH():
        print(str(datetime.now()) + " ;; Starting whirr effect...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe whirr_st.vbs')
        time.sleep(3)
        gongWhirr = threading.Thread(target=whirr.standard)
        gongWhirr.start()
        print(str(datetime.now()) + " ;; Playing half hour chime...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe hhcs.vbs')
        file = open(".\\clocks\\default\\hhcs_config.txt", "r")
        hcst = int(file.read()) - 2
        file.close()
        print(str(datetime.now()) + " ;; Waiting for " + str(hcst) + " seconds...")
        time.sleep(hcst)
        print(str(datetime.now()) + " ;; Chime sequence finished.")
        globals.isChime = False
        
    def chimeTH():
        print(str(datetime.now()) + " ;; Starting whirr effect...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe whirr_st.vbs')
        time.sleep(3)
        gongWhirr = threading.Thread(target=whirr.standard)
        gongWhirr.start()
        print(str(datetime.now()) + " ;; Playing third quarter hour chime...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe tqhcs.vbs')
        file = open(".\\clocks\\default\\tqhcs_config.txt", "r")
        hcst = int(file.read()) - 2
        file.close()
        print(str(datetime.now()) + " ;; Waiting for " + str(hcst) + " seconds...")
        time.sleep(hcst)
        print(str(datetime.now()) + " ;; Chime sequence finished.")
        globals.isChime = False
        
    def chimeHN():
        print(str(datetime.now()) + " ;; Starting gong whirr effect...")
        os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe gong_whirr_st.vbs')
        time.sleep(3)
        gongWhirr = threading.Thread(target=whirr.gong)
        gongWhirr.start()
        hour = int(getDate()[3])
        if hour > 12:
            hour = hour - 12
        if hour < 1:
            hour = 12
        hourn = hour
        file = open(".\\clocks\\default\\gong_config.txt", "r")
        hcst = int(file.read())
        file.close()
        while hour > 0:
            print(str(datetime.now()) + " ;; Playing gong number " + str(hourn - hour) + "...")
            os.system('cmd.exe /c start /b /d ".\\sound\\clock" "" ..\..\clock.exe gong.vbs')
            print(str(datetime.now()) + " ;; Waiting for " + str(hcst) + " seconds...")
            time.sleep(hcst)
            hour = hour - 1
        print(str(datetime.now()) + " ;; Chime sequence finished.")
        globals.isGong = False
        
    def chimeCH():
        print(str(datetime.now()) + " ;; Playing christmas chime...")
        pytools.sound.main.playSound("cotb.mp3", 0, 10, 1.0, 0.0, 1, clock=False)

def main():
    chime.chimeFH()
    chime.chimeHN()
    time.sleep(60)
    while 1 == 1:
        if os.path.exists(".\\remember.derp") == False:
            if int(getDate()[3]) == 19:
                if int(getDate()[4]) == 8:
                    mech.windCL()
            if int((getDate()[4])) == 58:
                mech.chimePR()
            if int((getDate()[4])) == 13:
                mech.chimePR()
            if int((getDate()[4])) == 28:
                mech.chimePR()
            if int((getDate()[4])) == 43:
                mech.chimePR()
            if int((getDate()[4])) == 0:
                chime.chimeFH()
                print(getDate())
                if int(getDate()[1]) == 12:
                    if int(getDate()[3]) == 12:
                        chime.chimeCH()
                chime.chimeHN()
                time.sleep(60)
            if int((getDate()[4])) == 15:
                chime.chimeQH()
                time.sleep(60)
            if int((getDate()[4])) == 30:
                chime.chimeHH()
                time.sleep(60)
            if int((getDate()[4])) == 45:
                chime.chimeTH()
                time.sleep(60)
        time.sleep(10)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True

def run():
    main()