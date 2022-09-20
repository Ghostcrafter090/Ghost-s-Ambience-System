import pytools
import os
import sys
import time

def main():
    pytools.IO.saveFile(".\\working\\server.derp", "derp")
    if os.path.exists(".\\serverCommands.json") == False:
        pytools.IO.saveJson(".\\serverCommands.json", {
            "commands": [],
            "execute": 0
        })
    print("Server started.")
    while True:
        try:
            commands = pytools.IO.getJson(".\\serverCommands.json")
            if commands["execute"] == 1:
                for command in commands["commands"]:
                    print("running command: " + command)
                    os.system("start /min "" py console.py " + command + " --server > server_output.cxl")
                commands["execute"] = 0
                pytools.IO.saveJson(".\\serverCommands.json", commands)
        except:
            pass
        time.sleep(1)
        
try:
    for n in sys.argv:
        if n == "--run":
            main()
except:
    pass