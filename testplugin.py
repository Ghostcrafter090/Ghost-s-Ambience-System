import pytools
import sys
import os

class plugin:
    test = False

def run():
    exec("""
import api.""" + sys.argv[2] + """
plugin.test = api.""" + sys.argv[2] + """
""")
    
    os.chdir(".\\working")

    plugin.test.run()

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