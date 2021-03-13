import os
from system import isWindows
try:
    import win32api
    import win32gui
except:
    pass



iS_UNMUTED = bool(True)



def mute_unmute() :
    if isWindows() == 1 : 
        WM_APPCOMMAND = 0x319
        APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

        hwnd_active = win32gui.GetForegroundWindow()
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)

    else :
        if iS_UNMUTED :
            os.system("osascript -e 'set volume output muted true'")
            iS_UNMUTED = bool(False)
        else :
            os.system("osascript -e 'set volume output muted false'")
            iS_UNMUTED = bool(True)

