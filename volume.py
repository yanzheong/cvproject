import os
from system import isWindows

def lower_volume():
    if isWindows(): 
        os.system("nircmd.exe changesysvolume 3000")
    else :
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 6.25) --100%'")

def raise_volume():
    if isWindows(): 
        os.system("nircmd.exe changesysvolume -3000")
    else :
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 6.25) --100%'")
