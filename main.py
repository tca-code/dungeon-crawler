from lib.clear import clear

from utils.render_hud import render_hud
from utils.cmds import run_cmd

from game_start import game_start

MAX_HP = 24

'''
1. Move
2. Check space
    0. If space was visited, do nothing
    1. If item, pick up
    2. If weapon, pick up
    3. If monster, enter combat
    4. If exit, win
3. Take Action
    1. Use item in inventory
    2. Fight
'''

def main():
    state = game_start(MAX_HP)
    turns = 0

    while True:
        clear()
        render_hud(state, MAX_HP)

        if turns is 0:
            pass
        
        if state["combat"] is not None:
            # continue combat
            pass
        else:
            
        
        cmd = run_cmd(input("> "))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("Goodbye!")
