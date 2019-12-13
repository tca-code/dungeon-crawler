import os
import re

def get_console_width():
    if os.name == "nt":
        regexr = r"Lines: (\s)* (\d*)"
        output = os.popen("MODE", "r").read()
        match = re.split(regexr, output)
        return int(match[2])
    else:
        coords = os.popen("stty size", "r").read().split()
        return int(coords[1])