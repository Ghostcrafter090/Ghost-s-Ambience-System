import pytools
import time

class status:
    apiKey = ""
    vars = {
        "lastLoop": []
    }

class tools:
    def returnDateArray(string):
        staArray = pytools.clock.utcFormatToArray(string)
        diaArray = pytools.clock.getTimeDialation()
        return pytools.clock.solveForDialation(diaArray, staArray)

def main():
    while True:
        data = pytools.net.getJsonAPI('https://api.sunrise-sunset.org/json?lat=44.847075&lng=-63.604849&formatted=0')
        sunrise = tools.returnDateArray(data['results']['sunrise'])
        sunset = tools.returnDateArray(data['results']['sunset'])
        cts = tools.returnDateArray(data['results']['civil_twilight_begin'])
        cte = tools.returnDateArray(data['results']['civil_twilight_end'])
        nts = tools.returnDateArray(data['results']['nautical_twilight_begin'])
        nte = tools.returnDateArray(data['results']['nautical_twilight_end'])
        ats = tools.returnDateArray(data['results']['astronomical_twilight_begin'])
        ate = tools.returnDateArray(data['results']['astronomical_twilight_end'])
        solarNoon = tools.returnDateArray(data['results']['solar_noon'])
        pytools.IO.saveList("daytimes.pyl", [ats, nts, cts, sunrise, solarNoon, sunset, cte, nte, ate])
        string = """
set csth=""" + str(cts[3]) + """
set cstm=""" + str(cts[4]) + """
set ceth=""" + str(cte[3]) + """
set cetm=""" + str(cte[4]) + """
set cesth=""" + str(sunset[3]) + """
set cestm=""" + str(sunset[4]) + """
set nsth=""" + str(nts[3]) + """
set nstm=""" + str(nts[4]) + """
set neth=""" + str(nte[3]) + """
set netm=""" + str(nte[4]) + """
set asth=""" + str(ats[3]) + """
set astm=""" + str(ats[4]) + """
set aeth=""" + str(ate[3]) + """
set aetm=""" + str(ate[4])
        pytools.IO.saveFile("daytimes.cmd", string)
        time.sleep(600)
        status.vars['lastLoop'] = pytools.clock.getDateTime()

def run():
    main()