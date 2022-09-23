import pytools
import sys
import os

class plugin:
    test = False
    
class globals:
    apiKey = ""

def run():
    exec("""
import api.""" + sys.argv[2] + """
plugin.test = api.""" + sys.argv[2] + """
""")
    
    os.chdir(".\\working")
    
    plugin.test.status.apiKey = globals.apiKey

    plugin.test.run()
    
for n in sys.argv:
    if n.split("=") == "--apiKey":
        globals.apiKey = n.split("=")[1]

runf = False
try:
    if sys.argv[1] == "--run":
        if sys.argv[2]:
            runf = True
except:
    print("Invalid syntax.")
    print("To test plugin: py testplugin.py --run <plugin_name>")
    
if runf:
    run()