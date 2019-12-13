from time import sleep
import sys

from lib.clear import clear

from utils.render_hud import render_hud
from utils.cmds import run_cmd
from utils.message import message

from utils.square_exists import square_exists
from utils.dice import d
from data.monsters import get_random_monster
from actions.monster_attack import monster_attack
from actions.player_attack import player_attack

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

    def render_and_message(msg):
        clear()
        render_hud(state, MAX_HP)
        print(message(msg))

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
            monster = get_random_monster()
            
            render_and_message("A " + monster["name"].upper() + " has been provoked.")
            sleep(1.5)
            
            mon_dmg = monster_attack(state, monster)
            render_and_message("The " + monster["name"].upper() + " deals you " + str(mon_dmg) \
                + " damage. You have " + str(state["player"]["hp"]) + " HP remaining.")
            
            # Combat loop
            while True:
                cmd = input("Do you attack? (Y/n) ")

                if cmd.lower() is not "n":
                    dmg = player_attack(state["player"], monster)
                    render_and_message("You deal " + str(dmg) + " damange with your " + state["player"]["equipped_weapon"]["name"].upper()\
                        + " the " + monster["name"].upper() + " has " + str(monster["hp"]) + " HP remaining.")
                    sleep(1.5)

                    mon_dmg = monster_attack(state, monster)
                    render_and_message("The " + monster["name"].upper() + " deals you " + str(mon_dmg) \
                        + " damage. You have " + str(state["player"]["hp"]) + " HP remaining.")
                    sleep(1.5)
                else:
                    render_and_message("You attempt to flee but are thwarted")
                
                if state["player"]["hp"] <= 0:
                    render_and_message("The " + monster["name"].upper() + " dances over your lifeless body.")
                    sleep(2)
                    render_and_message("GAME OVER")
                    sleep(1)
                    sys.exit()
                
                if monster["hp"] <= 0:
                    render_and_message("You've defeated the " + monster["name"].upper() + ". You burn its corpse so it doesn't attract others.")
                    sleep(2)
                    state["combat"] = False
                    break

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
            render_and_message("Where you're trying to go is no place at all.")
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
            render_and_message("Looks like you hit a wall there bud. Maybe try a different direction.")
            print("> ")
            sleep(1)
            continue
        
        state["coords"] = next_square
        state["visited"].append(state["coords"])
        # TODO: check square
        if d(1, 20) > 10:
            state["combat"] = True
            render_and_message("There's something in the dark!")
        else:
            state["combat"] = False


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("Goodbye!")
