from tkinter import E
import pytools
import threading
import os
import sys
import traceback
import time

class threads:
    list = {}
    
    def launch(id):
        threads.list[id].start()
    
    def check(id):
        try:
            threads.list[id].join(timeout=0.5)
        except:
            pass
        try:
            if threads.list[id].is_alive():
                print(id)
                out = True
            else:
                out = False
        except:
            return False
        return out
    
class plugin:
    def __init__(self, pluginId, pluginObj, pluginString):
        self.obj = pluginObj
        self.id = pluginId
        self.fileData = pluginString
        
    def run(self):
        while True:
            try:
                if self.id != "old":
                    if self.id != "__pycache__":
                        self.obj.run()
                    else:
                        time.sleep(1000)
                else:
                    time.sleep(1000)
            except Exception as ex:
                try:
                    handlers.error.log(str(sys.exc_info()[0]), self.id, traceback.format_exc())
                    time.sleep(3)
                except:
                    print(str(pytools.clock.getDateTime()) + " ;;; log error.")
                    time.sleep(3)
    
    obj = False
    id = False
    fileData = ""

class plugins:
    list = {}
    
    def register(name, obj, strf):
        plugins.list[name] = plugin(name, obj, strf)
        
    def load(name):
        threads.list[name] = threading.Thread(target=plugins.list[name].run)
        
class handlers:
    class main:
        
        regObjTemp = {}
        
        def registerPlugins():
            os.system("mkdir .\\vars\\plugins")
            pluginsf = os.listdir(".\\api")
            keys = []
            for pluginf in pluginsf:
                print("Importing plugin " + pluginf + "...")
                if pluginf.find(".py") != -1:
                    exec("import api." + pluginf.split(".py")[0] + "\nhandlers.main.regObjTemp['" + pluginf.split(".py")[0] + "'] = api." + pluginf.split(".py")[0])
                    plugins.register(pluginf.split(".py")[0], handlers.main.regObjTemp[pluginf.split(".py")[0]], pytools.IO.getFile(".\\api\\" + pluginf))    
                    keys.append(pluginf.split(".py")[0])
            os.system("del .\\vars\\plugins\\*.cx /f /s /q")
            os.system("del .\\working\\*_errorlog.log")
            pytools.IO.saveFile(".\\vars\\pluginsList.pyn", keys)
        
        def loadPlugins():
            for pluginf in plugins.list:
                print("Loading plugin " + pluginf + "...")
                plugins.load(pluginf)
        
        def launchPlugins():
            os.chdir(".\\working")
            for threadf in threads.list:
                print("Launching plugin " + threadf + "...")
                threads.launch(threadf)
    
    class error:

        errorStatus = {}

        def log(error, pluginf, tracebackf):
            if os.path.isfile(pluginf + '_errorlog.log') == False:
                pytools.IO.saveFile(pluginf + '_errorlog.log', '')
            pytools.IO.saveFile("..\\vars\\plugins\\" + pluginf + "-error.cx", error)
            errorlog = "\n" + str(pytools.clock.getDateTime()) + ' ::: ' + pluginf + "; " + tracebackf
            pytools.IO.appendFile(pluginf + '_errorlog.log', errorlog)
            print("handlers.error.errorStatus['" + pluginf.split(".")[1] + "'] = " + pluginf.replace(".run()", "") + ".status.finishedLoop")
            exec("handlers.error.errorStatus['" + pluginf.split(".")[1] + "'] = " + pluginf.replace(".run()", "") + ".status.finishedLoop")
            pytools.IO.saveFile("..\\vars\\plugins\\" + pluginf + "-loopStatus.cx", str(handlers.error.errorStatus[pluginf.split(".")[1]]))

def soundsReporter():
    while True:
        window = "\n"
        clock = "\n"
        fireplace = "\n"
        outside = "\n"
        pluginf = "processreport"
        sounds = plugins.list[pluginf].obj.pytools.sound.main.activeSounds
        for n in sounds:
            if sounds[n][1][0] == "window":
                if window.find("\n"+ sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n") == -1:
                    window = window + sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n"
            elif sounds[n][1][0] == "clock":
                if clock.find("\n"+ sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n") == -1:
                    clock = clock + sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n"
            elif sounds[n][1][0] == "fireplace":
                if fireplace.find("\n"+ sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n") == -1:
                    fireplace = fireplace + sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n"
            elif sounds[n][1][0] == "outside":
                if outside.find("\n"+ sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n") == -1:
                    outside = outside + sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n"
            elif sounds[n][1][0] == "windown":
                if outside.find("\n"+ sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n") == -1:
                    outside = outside + sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n"
                if window.find("\n"+ sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n") == -1:
                    window = window + sounds[n][0].replace(".mp3", "").replace(".vbs", "").replace("_", " ").replace("active ghost.", "g_") + "\n"
            # except:
                # pass
        pytools.IO.saveJson("..\\vars\\sounds.json", {
            "clock": clock,
            "fireplace": fireplace,
            "window": window,
            "outside": outside
        })
        time.sleep(1)
       
def run():
    os.system("del .\\vars\\pluginVarsJson\\*.json /f /q")
    handlers.main.registerPlugins()
    handlers.main.loadPlugins()
    handlers.main.launchPlugins()
    
    soundsReport = threading.Thread(target=soundsReporter)
    soundsReport.start()
    
    while True:
        try:
            i = 0
            for pluginf in plugins.list:
                try:
                    compat = False
                    for n in sys.argv:
                        if n.split("=")[0] == "--apiKey":
                            pytools.IO.saveFile(".\\access.key", n.split("=")[1])
                    pytools.IO.saveJson('..\\vars\\\\pluginVarsJson\\' + pluginf + '_keys.json', plugins.list[pluginf].obj.status.vars)
                except:
                    print(traceback.format_exc())
                i = i + 1
            pytools.IO.saveFile("..\\systemLoop.json", "{\"lastLoop\":" + str(pytools.clock.getDateTime()) + "}")
            
            for n in os.listdir("..\\api"):
                if n != "old":
                    if n != "__pycache__":
                        try:
                            pytools.dummyf(plugins.list[n.split(".py")[0]])
                        except:
                            try:
                                error = 0
                                out = True
                                while error < 100:
                                    try:
                                        vars = pytools.IO.getJson("..\\vars\\pluginVarsJson\\" + n.split(".py")[0] + "_keys.json")
                                        if (pytools.clock.dateArrayToUTC(vars["lastLoop"]) + 60) > pytools.clock.dateArrayToUTC(pytools.clock.getDateTime()):
                                            out = False
                                    except:
                                        error = error + 1
                                if out:
                                    handlers.error.log("Handler for plugin " + n.split(".py")[0] + " has exited unexpectedly.", n.split(".py")[0], "\nAttempting to relaunch thread...")
                                    exec("import api." + n.split(".py")[0] + "\nhandlers.main.regObjTemp['" + n.split(".py")[0] + "'] = api." + n.split(".py")[0])
                                    plugins.register(n.split(".py")[0], handlers.main.regObjTemp[n.split(".py")[0]], pytools.IO.getFile(".\\api\\" + n.split(".py")[0] + ".py"))
                                    plugins.load(n.split(".py")[0])
                                    threads.launch(n.split(".py")[0])
                            except:
                                pass
        
        except:
            pass
        try:
            time.sleep(1)
        except:
            pass

try:
    for n in sys.argv:
        if n == "--run":
            run()
except:
    pytools.IO.saveFile("..\\crashlog.log", traceback.format_exc())
    
run()