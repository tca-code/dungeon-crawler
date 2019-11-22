import os

def get_console_width():
    coords = os.popen("stty size", "r").read().split()
    return int(coords[1])