from time import sleep

from lib.clear import clear

from utils.render_hud import render_hud
from utils.init_state import init_state
from utils.message import message
from utils.get_player_action import get_player_action

from data.weapons import weapons

from actions.equip_weapon import equip_weapon

def game_start(max_hp):
    clear()
    print(message("You awake cold and hungry. Everywhere you look is nothing but dark."))
    sleep(5)

    clear()
    print(message("How did you get here? The memories of it come in flashes and fits. Were you thrown down here or did you fall?"))
    sleep(5)

    clear()
    print(message("You struggle to your feet and try to get your bearings. Try to even remember your own name. What is your name?"))
    sleep(3)

    name = input("> ")
    uppercased_name = "{}{}".format(name[0].upper(), name[1:])

    state = init_state(uppercased_name, max_hp)

    clear()
    render_hud(state, max_hp)
    print(message("Of course! \"{} the {},\" that is what they used to call you.".format((state["player"]["name"]), state["player"]["title"])))
    sleep(5)

    clear()
    render_hud(state, max_hp)
    pick = get_player_action(
        "You have no shield, but you quickly realize you've got a weapon hanging by your side. Do you remember what it is?",
        ["Sword", "Axe", "Spear"],
    )

    chosen_weapon = weapons[str(pick + 2)]
    state = equip_weapon(state, chosen_weapon)

    return state