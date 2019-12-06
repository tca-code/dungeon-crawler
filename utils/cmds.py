import sys
from lib.clear import clear

def exit():
    clear()
    print("Goodbye!")
    sys.exit()

CMDS = {
    "exit": exit
}

def run_cmd(cmd):
    if cmd[0] is ".":
        cmd_key = cmd[1:]
        CMDS[cmd_key]()
    return cmd