from email.errors import NoBoundaryInMultipartDefect
from tempfile import TemporaryFile
import pytools
import time
import os
import termcolor
import sys
import threading
import ctypes
import msvcrt
import subprocess
import os
from sty import Style, RgbBg, RgbFg
from sty import fg, bg, ef, rs
import math
import random

import sounddevice as sd
import numpy as np
import pytools

from ctypes import wintypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)

SW_MAXIMIZE = 3

class globals:
    maxSize = False

kernel32.GetConsoleWindow.restype = wintypes.HWND
kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

os.system("color")

class tools:
    def max_window(lines=None):
        fd = os.open('CONOUT$', os.O_RDWR)
        try:
            hCon = msvcrt.get_osfhandle(fd)
            max_size = kernel32.GetLargestConsoleWindowSize(hCon)
            if max_size.X == 0 and max_size.Y == 0:
                raise ctypes.WinError(ctypes.get_last_error())
        finally:
            os.close(fd)
        globals.maxSize = max_size
        cols = 100
        hWnd = kernel32.GetConsoleWindow()
        if cols and hWnd:
            if lines is None:
                globals.maxY = max_size.Y
            else:
                globals.maxY = max_size.Y
            subprocess.check_call('mode.com con cols={} lines={}'.format(cols, globals.maxY))
            user32.ShowWindow(hWnd, SW_MAXIMIZE)
            
    printf = False
            
    def printColor(x, y, text, r, g, b, yellow=False):
        if x >= globals.maxSize.X:
            x = globals.maxSize.X - 1
        if y >= globals.maxSize.Y:
            y = globals.maxSize.Y - 1
        
        bg.orange = Style(RgbBg(r, g, b))
        fg.orange = Style(RgbFg(r, g, b))
        if yellow:
            try:
                if pixl.array[x][y] == 0:
                    # pytools.IO.console.printAt(x, y, termcolor.colored(text, color))
                    pytools.IO.console.printAt(x, y, fg.orange + bg.orange + text + bg.rs + fg.rs)
            except:
                pass
        else:
            pixl.array[x][y] = r + g + b

            pytools.IO.console.printAt(x, y, fg.orange + bg.orange + text + bg.rs + fg.rs)
class pixl:
    array = {}
        
class main:
    class visi:
        pix = {}
        
        def update(indata, outdata, frames, time, status):
            vol = float(np.linalg.norm(indata)*10)
            i = 0
            
            typef = {
                0: "red",
                1: "yellow"
            }
            
            while i < random.random():
                randX = int(math.floor(random.random() * globals.maxSize.X))
                if random.random() < 0.5:
                    main.visi.pix["red"][randX] = main.visi.pix["red"][randX] + vol
                    if main.visi.pix["red"][randX] > 120:
                        main.visi.pix["red"][randX] = 120
                else:
                    main.visi.pix["yellow"][randX] = main.visi.pix["yellow"][randX] + vol
                    if main.visi.pix["yellow"][randX] > 300:
                        main.visi.pix["yellow"][randX] = 300
                i = i + 0.1
            
        def register():
            main.visi.pix["yellow"] = {}
            main.visi.pix["red"] = {}
            
            typef = {
                0: "red",
                1: "yellow"
            }
            
            n = 0
            i = 0
            while i < globals.maxSize.X:
                n = 1
                main.visi.pix[typef[n]][i] = 0
                n = 0
                main.visi.pix[typef[n]][i] = 0
                k = 0
                while k < globals.maxSize.Y:
                    try:
                        pixl.array[i][k] = 0
                    except:
                        pixl.array[i] = {}
                        pixl.array[i][k] = 0
                    k = k + 1
                i = i + 1
                
                    
        
    def sounds():
        # sd.default.device[1] = 23
        while True:
            with sd.Stream(callback=main.visi.update):
                sd.sleep(1000)
    
    class man:
        def __init__(self, range):
            self.range = range
            
        range = [0, 1]
            
        def manager(self):
            while True:
                for n in main.visi.pix["red"]:
                    if self.range[0] < n < self.range[1]:
                        nr = int(main.visi.pix["red"][n]) + 1
                        ng = 1
                        nb = 1
                        if nr > 100:
                            ng = nr - 100
                            nr = 100
                        if ng > 100:
                            nb = ng - 100
                            ng = 100
                        if nb > 100:
                            nb = 100
                        flicker =  0.7 + (0.3 * random.random())
                        y = int(math.floor(((((nr + ng + nb) / 300) * globals.maxSize.Y) * 0.3)))
                        j = 0
                        while j < y:
                            nrh = nr + ng + nb - ((j / globals.maxSize.Y) * 300)
                            ngh = 1
                            nbh = 1
                            if nrh > 100:
                                ngh = nrh - 100
                                nrh = 100
                            if ngh > 100:
                                nbh = ngh - 100
                                ngh = 100
                            if nbh > 100:
                                nbh = 100
                            tools.printColor(n, globals.maxSize.Y - (j + 1), "X", int(math.floor(((nrh / 100) * flicker) * 255 * (1 - (j / y)))), int(math.floor(((ngh / 100) * flicker) * 255 * (1 - (j / y)))), int(math.floor(((nbh / 100) * flicker) * 255 * (1 - (j / y)))))
                            j = j + 1
                        try:
                            pass
                        except:
                            pass
                        main.visi.pix["red"][n] = main.visi.pix["red"][n] - 0.1
                        if main.visi.pix["red"][n] < 0:
                            main.visi.pix["red"][n] = 0
                for n in main.visi.pix["yellow"]:
                    if self.range[0] < n < self.range[1]:
                        if main.visi.pix["yellow"][n] + 50 <= 50:
                            nr = 1
                        else:
                            nr = int(main.visi.pix["yellow"][n] + 50)
                            y = int(math.floor((((((nr + ng + nb)) / 300) * globals.maxSize.Y))))
                        ng = 1
                        nb = 1
                        if nr > 100:
                            ng = nr - 100
                            nr = 100
                        if ng > 100:
                            nb = ng - 100
                            ng = 100
                        if nb > 100:
                            nb = 100
                        flicker =  0.7 + (0.3 * random.random())
                        j = 0
                        while j < y:
                            nrh = nr + ng + nb - ((j / globals.maxSize.Y) * 300)
                            ngh = 1
                            nbh = 1
                            if nrh > 100:
                                ngh = nrh - 100
                                nrh = 100
                            if ngh > 100:
                                nbh = ngh - 100
                                ngh = 100
                            if nbh > 100:
                                nbh = 100
                            tools.printColor(n, globals.maxSize.Y - (j + 1), "X", int(math.floor(((nrh / 100) * flicker) * 255 * (1 - (j / y)))), int(math.floor(((ngh / 100) * flicker) * 255 * (1 - (j / y)))), int(math.floor(((nbh / 100) * flicker) * 255 * (1 - (j / y)))), True)
                            j = j + 1
                        try:
                            k = 0
                            while k < 11:
                                tools.printColor(n, globals.maxSize.Y - (y + k), " ", 0, 0, 0, True)
                                k = k + 1
                        except:
                            pass
                        main.visi.pix["yellow"][n] = main.visi.pix["yellow"][n] - 10
                        if main.visi.pix["yellow"][n] < 0:
                            main.visi.pix["yellow"][n] = 0
    
def run():
    tools.max_window()
    main.visi.register()
    mains = []
    r = globals.maxSize.X
    i = 0
    while i < globals.maxSize.X:
        mains.append(threading.Thread(target=main.man([i, i + r]).manager))
        i = i + r
    thread1 = threading.Thread(target=main.sounds)
    for n in mains:
        n.start()
    thread1.start()
    
try:
    # if sys.argv[1] == "--run":
    if True:
        run()
except:
    pass