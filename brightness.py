import os
from system import isWindows

def lower_brightness():
    if isWindows(): 
        os.system("nircmd.exe changebrightness -20")
    else :
        os.system("osascript -e 'tell application \"System Events\"' -e 'key code 145' -e ' end tell'")


def raise_brightness():
    if isWindows(): 
        os.system("nircmd.exe changebrightness 20")
    else :
        os.system("osascript -e 'tell application \"System Events\"' -e 'key code 144' -e ' end tell'")
