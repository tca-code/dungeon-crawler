from time import sleep
import sys

from lib.clear import clear

from utils.render_hud import render_hud
from utils.cmds import run_cmd
from utils.message import message
from utils.square_exists import square_exists

from game_start import game_start

args = sys.argv[1:]

MAX_HP = 24
DIRECTIONS = [
    "up",
    "down",
    "left",
    "right"
]
SPEED_UP_TEXT = "--fast" in args

def main():
    state = game_start(MAX_HP, SPEED_UP_TEXT)
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

        print(message("Which direction do you go?"))
        print(state["coords"])
        cmd = run_cmd(input("> "))

        # Step 2: Error Handling
        if cmd.lower() not in DIRECTIONS:
            clear()
            render_hud(state, MAX_HP)
            print(message("Hmm... that doesn't sound like any direction I've heard of before"))
            print("> ")
            sleep(1)
            continue
        
        # Step 1: Update state
        if cmd.lower() == "up":
            (x, y) = state["coords"]
            next_square = (x, y - 1)
        elif cmd.lower() == "down":
            (x, y) = state["coords"]
            next_square = (x, y + 1)
        elif cmd.lower() == "left":
            (x, y) = state["coords"]
            next_square = (x - 1, y)
        elif cmd.lower() == "right":
            (x, y) = state["coords"]
            next_square = (x + 1, y)
        
        # Step 3: Check if square exists
        if not square_exists(state, next_square):
            clear()
            render_hud(state, MAX_HP)
            print(message("Where you're trying to go is no place at all."))
            print("> ")
            sleep(1)
            continue

        (x, y) = next_square

        # Step 4: Find the exit
        if state["dungeon"][y][x] == 3:
            # TODO: make the victory more enjoyable
            print(message("You did it! you made it out alive!"))
            break

        # Step 5: collision logics
        if state["dungeon"][y][x] == 1:
            clear()
            render_hud(state, MAX_HP)
            print(message("Looks like you hit a wall there bud. Maybe try a different direction."))
            print("> ")
            sleep(1)
            continue
        
        state["coords"] = next_square
        state["visited"].append(state["coords"])
        # TODO: check square


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("Goodbye!")
