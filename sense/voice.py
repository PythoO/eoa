import sys
import subprocess


def speech(message):
    """
    This function takes a message as an argument and converts it to
    speech depending on the OS.
    """
    print(message)
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return subprocess.call([tts_engine, message])
    elif sys.platform.startswith('linux') or sys.platform == 'win32':
        tts_engine = 'espeak'
        speed = '-s170'
        return subprocess.call([tts_engine, speed, message])
