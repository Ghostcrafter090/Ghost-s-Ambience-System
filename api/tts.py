import speech_recognition as sr
import pyttsx3
import pytools
import threading
import time
import importlib

class status:
    apiKey = ""
    finishedLoop = False
    vars = {
        "lastLoop": []
    }
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

mics = {}

pytools.IO.saveFile("transcript.cxl", "")
     
# Loop infinitely for user to
# speak

class globals:
    speech = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    speeches = 0
 
class micInstance:
    def __init__(self, micf, namef):
        self.mic = micf
        self.name = namef
        
    mic = 0
    name = ""
    
    def getText(self, mic):
        while(1):   
        
            # Exception handling to handle
            # exceptions at the runtime
            try:
                
                # use the microphone as source for input.
                with sr.Microphone(device_index=mic) as source2:
                    
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    
                    #listens for the user's input
                    try:
                        audio2 = r.listen(source2, timeout=1, phrase_time_limit=5)
                        
                        # Using google to recognize audio
                        MyText = r.recognize_google(audio2)
                        MyText = MyText.lower()
                    
                        return MyText
                    except:
                        return False
                    
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                return False
                
            except sr.UnknownValueError:
                print("unknown error occured")
                return False

    def micRun(self):
        while True:
            text = micInstance.getText(self, self.mic)
            print(text)
            n = True
            try:
                file = pytools.IO.getFile("transcript.cxl").split("\n")
                if len(file) > 10:
                    file = file[1:]
                    file.append(text + ";" + str(self.name))
                    n = False
                filef = ""
                for r in file:
                    filef = filef + r + "\n"
                pytools.IO.saveFile("transcript.cxl", filef.replace("\n\n", "\n"))
            except:
                n = True
            if n:
                if text:
                    pytools.IO.appendFile("transcript.cxl", text + ";" + str(self.name) + "\n")
        
micHandlers = []

def runMic(*args):
    string = ""
    for x in args:
        string += x
        print(int(micHandlers[int(x)][0][0]))
    n = micInstance(int(micHandlers[int(x)][0][0]), micHandlers[int(x)][0][1])
    print(x)
    n.micRun()
        
def run():
    mics = pytools.IO.getJson("mics.json")
    i = 0
    n = 0
    f = 0
    while n < sr.Microphone.get_pyaudio().PyAudio().get_device_count():
        for key in mics:
            if key == sr.Microphone.get_pyaudio().PyAudio().get_device_info_by_index(n)["name"]:
                if sr.Microphone.get_pyaudio().PyAudio().get_device_info_by_index(n)["hostApi"] == 2:
                    micHandlers.append(["", ""])
                    micHandlers[f][0] = [n, sr.Microphone.get_pyaudio().PyAudio().get_device_info_by_index(n)["name"]]
                    micHandlers[f][1] = threading.Thread(target=runMic, args=str(f))
                    f = f + 1
        n = n + 1
    for n in micHandlers:
        n[1].start()
        print("penis")
    while True:
        pytools.IO.saveFile("speechPerMinute.cx", "0")
        dateArray = pytools.clock.getDateTime()
        if dateArray[4] % 5:
            globals.speech[i] = globals.speeches
            pytools.IO.saveFile("speechPerMinute.cx", str(globals.speeches))
            globals.speeches = 0
            i = i + 1
            if i > 9:
                i = 0
            status.vars['lastLoop'] = pytools.clock.getDateTime()
            status.finishedLoop = True
