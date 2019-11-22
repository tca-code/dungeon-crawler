from lib.clear import clear

from utils.render_hud import render_hud
from utils.cmds import run_cmd

from game_start import game_start

MAX_HP = 24

def main():
    state = game_start(MAX_HP)
    turns = 0

    while True:
        '''
        Anatomy of a Turn (Loop)
        1. Clear the screen
        2. Re-render the heads up display (HUD)
        3. Check to see if we're in combat, if we are, complete the combat
        4. If not in combat, let the user know what directions are available
           and ask them what they want to do.
        5. Check the new "square" to see if there's loot or a monster there
        6. If there's loot, pick it up. If it's a monster, enter combat.
        '''
        clear()
        render_hud(state, MAX_HP)
        
        if state["combat"]:
            # TODO: write combat code
            pass

        # TODO: let the player know which directions are available
        cmd = run_cmd(input("> "))

        # TODO: move the player based on their "cmd"


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("Goodbye!")
