import pytools
import os
import threading
import time

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
                script = script + "import api." + list[i] + "\nplugin." + list[i] + " = api." + list[i] + "\n"
                os.system("mkdir .\\vars\\plugins")
                i = i + 1
            out = exec(script)
            return out

        def launch():
            imports = handlers.launcher.getImports()
            handlers.launcher.importPlugins(imports)
            i = 0
            while i < len(imports):
                plugin.register('plugin.' + str(imports[i]))
                i = i + 1
            os.chdir('.\\working')
            plugin.activate()
            while True:
                i = 0
                while i < len(imports):
                    try:
                        exec("for key in plugin." + imports[i] + ".status.vars:\n    pytools.IO.saveJson('..\\\\vars\\\\plugins\\\\' + imports[i] + '-' + key + '.cx', plugin." + str(imports[i]) + ".status.vars[key])")
                    except:
                        pass
                    i = i + 1
                time.sleep(3)
            return 0

    class error:
        def log(error, plugin):
            if os.path.isfile(plugin + '_errorlog.log') == False:
                pytools.IO.saveFile(plugin + '_errorlog.log', '')
            # errorlog = pytools.IO.getFile(plugin + '_errorlog.log')
            errorlog = "\n" + str(pytools.clock.getDateTime()) + ' ::: ' + plugin + "; " + error
            pytools.IO.appendFile(plugin + '_errorlog.log', errorlog)

handlers.launcher.launch()