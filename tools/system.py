import os
import ctypes
import subprocess


def shutdown_pc():
    os.system("shutdown /s /t 5")
    return "Shutting down your computer."


def restart_pc():
    os.system("shutdown /r /t 5")
    return "Restarting your computer."


def sleep_pc():
    ctypes.windll.powrprof.SetSuspendState(False, True, False)
    return "Putting computer to sleep."


def lock_pc():
    ctypes.windll.user32.LockWorkStation()
    return "Locking your computer."


def sign_out():
    os.system("shutdown /l")
    return "Signing out."


def volume_up():
    try:
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        from ctypes import POINTER, cast
        from comtypes import CLSCTX_ALL

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        volume = cast(interface, POINTER(IAudioEndpointVolume))

        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)

        return "Volume increased."

    except:
        return "Unable to increase volume."


def volume_down():
    try:
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        from ctypes import POINTER, cast
        from comtypes import CLSCTX_ALL

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        volume = cast(interface, POINTER(IAudioEndpointVolume))

        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)

        return "Volume decreased."

    except:
        return "Unable to decrease volume."


def mute_volume():
    try:
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        from ctypes import POINTER, cast
        from comtypes import CLSCTX_ALL

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        volume = cast(interface, POINTER(IAudioEndpointVolume))

        volume.SetMute(1, None)

        return "Volume muted."

    except:
        return "Unable to mute volume."