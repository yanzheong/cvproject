import os
from system import isWindows

def lower_volume() :
    if isWindows() == 1 : 
        os.system("nircmd.exe changesysvolume 3000")
    else :
        os.system("osascript -e 'set volume output volume -10'")

def raise_volume() :
    if isWindows() == 1 : 
        os.system("nircmd.exe changesysvolume -3000")
    else :
        os.system("osascript -e 'set volume output volume +10'")