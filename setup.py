import os

importArray = [
    ['win32api', "py -m pip install pywin32"],
    ['win32con', "py -m pip install pywin32"],
    ['win32gui', "py -m pip install pywin32"],
    'psutil',
    ['smtplib', 'py -m pip install secure-smtplib'],
    ['PIL', 'py -m pip install PILLOW'],
    'requests',
    'datetime',
    'bs4',
    ['threading', 'py -m pip install thread6'],
    'suntime',
    ['zipfile', 'py -m pip install zipfile36 & py -m pip install zipfile38'],
    ['shutil', 'py -m pip install pytest-shutil'],
    ['pickle', 'py -m pip install pickle-mixin'],
]

class check:
    cond = False

i = 0
install = True
while (i < len(importArray)) and (install):
    # exec("try:\n    import " + importArray[i] + "\n    check.cond = True\nexcept:\n    check.cond = False")
    if check.cond == False:
        out = input("Permission to install " + str(importArray[i]) + " (Y/n)? ")
        if out == "Y":
            if str(importArray[i])[0] == "[":
                os.system(importArray[i][1])
            else:
                os.system("py -m pip install " + importArray[i])
        else:
            install = False
    i = i + 1

if (install):
    print("Components Installed! Downloading and unpacking assets...")
    os.system("py .\\unpack.py")
else:
    print("Error. Not all components installed.\nIf you wish to run Ghost's Ambience System,\nplease rerun this script and respond with 'Y' for all responses.")
    exit()