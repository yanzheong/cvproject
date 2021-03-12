from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

class Volume:

    def lower_volume()
        # Get default audio device using PyCAW
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Get current volume 
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
        # NOTE: -6.0 dB = half volume !

    def raise_volume()
        # Get default audio device using PyCAW
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Get current volume 
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb + 6.0, None)
        # NOTE: -6.0 dB = half volume !