import pytools
import time

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }

class globals:
    urlBase = 'http://api.openweathermap.org/data/2.5/weather?lat=44.8367770&lon=-63.5951100&appid=' + status.apiKey
    urlFast = 'http://gsweathermore.ddns.net:226/access.php?key=56c15c7d00df42d8815c7d00df42d8ab'
    urlSuperFast = 'http://gsweathermore.ddns.net:226/currentdata.json'
class grabber:
    def getBaseData(url):
        try:
            print(str(pytools.clock.getDateTime()) + ' ::: Getting Base Data...')
            # url: http://api.openweathermap.org/data/2.5/weather?lat=44.7659964&lon=-63.6850686&appid=<apiKey>
            data = pytools.net.getJsonAPI(url)
            # [windspeeds, windgusts, visibility, snow, weather, modifier]
            try:
                if data['weather'][0]['main'] == "Thunderstorm":
                    weather = 'thunder'
                elif data['weather'][0]['main'] == "Rain":
                    weather = 'rain'
                elif data['weather'][0]['main'] == "Drizzle":
                    weather = 'lightrain'
                elif data['weather'][0]['main'] == "Snow":
                    weather = 'snow'
                elif data['weather'][0]['main'] == "Mist":
                    weather = 'mist'
                elif data['weather'][0]['main'] == "Clouds":
                    weather = 'clouds'
                elif float(data['weather'][0]['id']) == 500.0:
                    weather = 'lightrain'
                else:
                    weather = 'clear'
            except:
                weather = 'clear'

            try:
                i = 0
                modifier = 0
                while i < len(data['weather']):
                    modifier = modifier + (float(data['weather'][i]['id']) % 100)
                    i = i + 1
            except:
                modifier = 0
            
            try:
                speed = float(data['wind']['speed'])
            except:
                speed = 0
            try:
                temp = float(data['main']['temp']) - 273
            except:
                temp = 0
            try:
                pressure = float(data['main']['pressure'])
            except:
                pressure = 0
            try:
                humidity = float(data['main']['humidity'])
            except:
                humidity = 0
            try:
                gusts = float(data['wind']['gust'])
            except:
                gusts = 0
            try:
                snow = float(data['snow']['1h'])
            except:
                try:
                    snow = float(data['snow']['3h'])
                except:
                    snow = 0
            array = [speed, gusts, float(data['visibility']), snow, weather, modifier, pressure, temp, humidity]
            print(array)
            return array
        except:
            return [0.0, 0.0, 15000, 0.0, 'clear', 0, 1000.0, 15.0, 50.0]

    def getFastData(url):
        try:
            print(str(pytools.clock.getDateTime()) + ' ::: Getting Fast Data...')
            # url: https://api.weather.com/v2/pws/observations/current?stationId=INOVASCO146&format=json&units=s&apiKey=<apiKey>
            data = pytools.net.getJsonAPI(url)['data']
            # [rainRate, rainTotal, pressure, temp, humidity, lightningDanger]
            rainRate = data['main']['observations'][0]['metric_si']['precipRate']
            rainTotal = data['main']['observations'][0]['metric_si']['precipTotal']
            pressure = data['main']['observations'][0]['metric_si']['pressure']
            temp = data['main']['observations'][0]['metric_si']['temp']
            humidity = data['main']['observations'][0]['humidity']
            lightning = data['lightning_danger']
            array = [float(rainRate) * 2, float(rainTotal) * 10, float(pressure), float(temp), float(humidity), int(lightning)]
            print(array)
            return array
        except:
            return False

    def getSuperFastData(url):
        data = pytools.net.getJsonAPI(url)
        try:
            rainRate = float(data['rainHour'])
        except:
            rainRate = 0.0
        try:
            windGusts = float(data['windPeak'])
        except:
            rainGusts = 0.0
        try:
            windSpeeds = float(data['windAvg'])
        except:
            windSpeeds = 0.0
        try:
            temp = float(data['temp'])
        except:
            temp = 0.0
        try:
            humidity = float(data['humidity'])
        except:
            humidity = 0.0
        try:
            pressure = float(data['rainHour'])
        except:
            pressure = 0.0
        return [temp, humidity, pressure, rainRate, windSpeeds, windGusts]
        

class bulk:
    def getData(oldBool: bool, oldData, bypass):
        dateArray = pytools.clock.getDateTime()
        if bypass:
            baseData = grabber.getBaseData(globals.urlBase)
            baseDataf = [baseData[0], baseData[1]]
            fastData = grabber.getFastData(globals.urlFast)
            superData = grabber.getSuperFastData(globals.urlSuperFast)
            dateNewBase = dateArray[4]
            dateNewFast = dateArray[4]
            dateNewSuper = dateArray[5]
        else:
            baseData = oldData[0]
            baseDataf = oldData[7]
            fastData = oldData[1]
            superData = oldData[2]
            dateNewBase = oldData[4]
            dateNewFast = oldData[5]
            dateNewSuper = oldData[6]
            if (dateArray[4] % 15) == 0:
                if oldData[4] != dateArray[4]:
                    dateNewBase = dateArray[4]
                    baseData = grabber.getBaseData(globals.urlBase)
                    baseDataf[0] = baseData[0]
                    baseDataf[1] = baseData[1]
            if (dateArray[4] % 1) == 0:
                if oldData[5] != dateArray[4]:
                    dateNewFast = dateArray[4]
                    fastData = grabber.getFastData(globals.urlFast)
            if (dateArray[5] % 20) == 0:
                if oldData[6] != dateArray[5]:
                    dateNewSuper = dateArray[5]
                    superData = grabber.getSuperFastData(globals.urlSuperFast)
        try:
            baseData[6] = superData[2]
            baseData[7] = superData[0]
            baseData[8] = superData[1]
            if baseDataf[0] < superData[4]:
                baseData[0] = superData[4]
            if baseDataf[1] < superData[5]:
                baseData[1] = superData[5]
            if fastData == False:
                fastData = [0, 0, baseData[6], baseData[7], baseData[8], 0]      
        except:
            pass

        outString = """set temp=""" + str(superData[0] + 273).split('.')[0] + """
    set tempc=""" + str(superData[0]).split('.')[0] + """
    set windspeed=""" + str(baseData[0]).split('.')[0] + """
    set windgust=""" + str(baseData[1]).split('.')[0] + """
    set pressure=""" + str(superData[2]).split('.')[0] + """
    set humidity=""" + str(superData[1]).split('.')[0] + """
    set weather=""" + str(baseData[4]).split('.')[0] + """
    set modifier=""" + str(baseData[5]).split('.')[0]
        dispString = """Temperature (C)      : """ + str(superData[0]) + """C
Wind Speeds (m/s)    : """ + str(baseData[0]) + """m/s
Wind Gusts  (m/s)    : """ + str(baseData[1]) + """m/s
Pressure    (hPa)    : """ + str(superData[2]) + """hPa
Humidity    (%)      : """ + str(superData[1]) + """%
Condition   (type)   : """ + str(baseData[4]) + """
Date        (YY-M-D) : """ + str(dateArray[0]) + "-" + str(dateArray[1]) + "-" + str(dateArray[2]) + """
Time        (hh:mm)  : """ + str(dateArray[3]) + ":" + str(dateArray[4])
        pytools.IO.saveFile("..\\vars\\dispstring.cx", dispString)
        pytools.IO.saveJson("..\\vars\\data.json", {
            "data": [baseData, fastData, outString, dateNewBase, dateNewFast],
            "dateArray": dateArray
        })
        if oldBool == 1:
            pytools.IO.saveFile('cond.cmd', outString)
        return [baseData, fastData, superData, outString, dateNewBase, dateNewFast, dateNewSuper, baseDataf]

def main():
    data = bulk.getData(1, [], True)
    while True:
        data = bulk.getData(1, data, False)
        print(str(pytools.clock.getDateTime()) + ' ::: ' + str(data))
        time.sleep(0.5)
        if (pytools.clock.getDateTime()[5] % 20) == 0:
            pytools.IO.saveList("dataList.pyl", data)
        status.vars['lastLoop'] = pytools.clock.getDateTime()
        status.finishedLoop = True


def run():
    main()