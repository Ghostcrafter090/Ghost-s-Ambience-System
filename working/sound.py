import sys
import time
import wave
import math
import os
import sounddevice as sd
import json

import pyaudio
from pydub.utils import get_player_name, make_chunks
from pydub import AudioSegment

class IO:
    def getJson(path, doPrint=True):
        error = 0
        try:
            file = open(path, "r")
            jsonData = json.loads(file.read())
            file.close()
        except:
            if doPrint:
                print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            jsonData = error
        return jsonData

class globals:
    speakers = {}

if os.path.exists(".\\soundOutputs.json"):
    globals.speakers = IO.getJson(".\\soundOutputs.json")
if os.path.exists("..\\soundOutputs.json"):
    globals.speakers = IO.getJson("..\\soundOutputs.json")

def run(seg, speed, index):
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(seg.sample_width),
                    channels=seg.channels,
                    output_device_index=index,
                    rate=int(seg.frame_rate * speed),
                    output=True)

    try:
        for chunk in make_chunks(seg, 500):
            stream.write(chunk._data)
    finally:
        stream.stop_stream()
        stream.close()

        p.terminate()

def play(path, volume, speed, speaker):
    speaker[0] = speaker[0].replace(".exe", "")
    
    if path.find(".mp3") != -1:
        wf = AudioSegment.from_mp3(path)
    else:
        wf = AudioSegment.from_wav(path)
    
    wf = wf + (10 * math.log(volume / 100, 10))
    
    try:
        index = globals.speakers[speaker[0]][2]
    except:
        for n in sd.query_devices():
            if globals.speakers[speaker[0]][0] == n["name"]:
                if globals.speakers[speaker[0]][1] == "MME":
                    if n["hostapi"] == 0:
                        index = n["index"]
                if globals.speakers[speaker[0]][1] == "WDM-KS":
                    if n["hostapi"] == 4:
                        index = n["index"]
        globals.speakers[speaker[0]].append(index)
    

    run(wf, speed, index)