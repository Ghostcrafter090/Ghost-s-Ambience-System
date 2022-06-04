import pytools
import os
import threading
import time
import sys

class globals:
    class thread:
        list = [[], 0]
        def initializeArray(n):
            i = 0
            while i < n:
                globals.thread.list[0].append('print("system fucky!")')
                i = i + 1
            return 0
        current = ''

class plugin:
    def register(pluginn):
        if globals.thread.list[0] == []:
            globals.thread.initializeArray(200)
        n = pluginn + '.run()'
        globals.thread.list[0][globals.thread.list[1]] = threading.Thread(target=plugin.run, args=n)
        # globals.thread.list[0][globals.thread.list[1]].join()
        globals.thread.list[1] = globals.thread.list[1] + 1
        if globals.thread.list[1] > len(globals.thread.list[0]):
            globals.thread.list[1] = 0

    def activate():
        i = 0
        while i < globals.thread.list[1]:
            globals.thread.list[0][i].start()
            i = i + 1

    def run(*args):
        string = ""
        for x in args:
            string += x
        print(str(string))
        while True:
            error = 'File Closed Unexpectedly!'
            # print('try:\n    ' + string + '\nexcept Exception as e:\n    error = e')
            execString = 'try:\n    ' + string.replace('main.plugin.', 'plugin.') + '\nexcept Exception as e:\n    error = e\n    print(error)\n    handlers.error.log(str(error), \'' + string + '\')'
            exec(execString)
            handlers.error.log(error, string)

class handlers:
    class launcher:
        def getImports():
            list = os.listdir('.\\api\\')
            i = 0
            outlist = []
            while i < len(list):
                if list[i].find(".py") != -1:
                    outlist.append(list[i].replace('.py', ''))
                i = i + 1
            return outlist

        def importPlugins(list):
            i = 0
            global plugin
            script = ""
            while i < len(list):
                script = script + "import api." + list[i] + "\nplugin." + list[i] + " = api." + list[i] + "\n" + "api." + list[i] + ".status.apiKey = '" + sys.argv[1] + "'\n"
                os.system("mkdir .\\vars\\plugins")
                i = i + 1
            out = exec(script)
            return out

        def launch():
            imports = handlers.launcher.getImports()
            handlers.launcher.importPlugins(imports)
            i = 0
            pluginList = ";"
            while i < len(imports):
                pluginList = pluginList + 'plugin.' + str(imports[i]) + ";"
                plugin.register('plugin.' + str(imports[i]))
                i = i + 1
            os.system("del .\\vars\\plugins\\*.cx /f /s /q")
            os.system("del .\\working\\*_errorlog.log")
            pytools.IO.saveFile(".\\vars\\pluginsList.pyn", pluginList)
            os.chdir('.\\working')
            plugin.activate()
            while True:
                i = 0
                while i < len(imports):
                    try:
                        exec("for key in plugin." + imports[i] + ".status.vars:\n    if str(plugin." + str(imports[i]) + ".status.vars['lastLoop']).find('Time: ') == -1:\n        plugin." + str(imports[i]) + ".status.vars['lastLoop'] = 'Time: ' + str(plugin." + str(imports[i]) + ".status.vars['lastLoop'])\n    pytools.IO.saveJson('..\\\\vars\\\\pluginVars\\\\' + imports[i] + '-' + key + '.cx', plugin." + str(imports[i]) + ".status.vars[key])")
                    except:
                        pass
                    i = i + 1
                time.sleep(3)
            return 0

    class error:

        errorStatus = {}

        def log(error, pluginf):
            if os.path.isfile(pluginf + '_errorlog.log') == False:
                pytools.IO.saveFile(pluginf + '_errorlog.log', '')
            # errorlog = pytools.IO.getFile(plugin + '_errorlog.log')
            pytools.IO.saveFile("..\\vars\\plugins\\" + pluginf + "-error.cx", error)
            errorlog = "\n" + str(pytools.clock.getDateTime()) + ' ::: ' + pluginf + "; " + error
            pytools.IO.appendFile(pluginf + '_errorlog.log', errorlog)
            print("handlers.error.errorStatus['" + pluginf.split(".")[1] + "'] = " + pluginf.replace(".run()", "") + ".status.finishedLoop")
            exec("handlers.error.errorStatus['" + pluginf.split(".")[1] + "'] = " + pluginf.replace(".run()", "") + ".status.finishedLoop")
            pytools.IO.saveFile("..\\vars\\plugins\\" + pluginf + "-loopStatus.cx", str(handlers.error.errorStatus[pluginf.split(".")[1]]))
            time.sleep(3)

handlers.launcher.launch()