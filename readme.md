GHOSTS ADAPTIVE AMBIENCE SYSTEM (Python Version)
---------------------------------------------------------------------------

To install, run setup.py, this will install the required python libraries if they don't exist already, and it will then pull the system assets from my website and unpack them.

If you've ran setup in this enviroment before, and just need to unpack the assets, run unpack.py

The "assets" I speak of are audio files. These are used for ambience generation.

*Running The System*
----------------------

To Run the ambience system, you will first need an API Key from Open Weather Map. 
https://openweathermap.org/api

Once obtained, there are 2 ways of launching the ambience system (the easiest at least). I will first outline the user client method.


User Client Method
------------------

Launch the file "console.py" in a command prompt window using python with the following command line switches:
```cmd
py console.py --run
```

Once ran, an information panel should appear looking something like this:

![alt text](https://github.com/Ghostcrafter090/Ghost-s-Ambience-System/blob/master/images/console_offline.png?raw=true)