from lib.color import Color
from lib.dot_prop import get
from lib.get_console_width import get_console_width

def __render_player_name(player_name, player_title):
    return Color("{} the {}".format(player_name, player_title)).yellow().render()

def __render_hp(max_health, remaining_health):
    return __render_stat(
        "Health", 
        "{}/{}".format(str(remaining_health), str(max_health)),
    )

def __render_shield(max_shield, remaining_shield):
    return __render_stat(
        "Shield", 
        "{}/{}".format(str(remaining_shield), str(max_shield)),
    )

def __render_weapon(weapon_name):
    label = Color("Weapon").yellow().render()
    weapon_colored = Color(weapon_name).green().render()
    return "{}: {}".format(label, weapon_colored)

def __render_stat(stat_name, stat_value):
    stat_name_colored = Color(stat_name).yellow().render()
    stat_value_colored = Color(stat_value).white().render()
    return "{}: {}".format(stat_name_colored, stat_value_colored)

def render_hud(state, max_health):
    console_width = get_console_width()
    player_state = state["player"]

    hp = __render_hp(max_health, get(player_state, "hp"))
    weapon = __render_weapon(get(player_state, "equipped_weapon.name"))
    shield = __render_shield(
        get(player_state, "equipped_shield.max"),
        get(player_state, "equipped_shield.remaining"),
    )
    player_name = __render_player_name(
        get(player_state, "name"),
        get(player_state, "title"),
    )

    stats_line = "{} {} {}".format(hp, weapon, shield)
    line_len = (len(stats_line) + len(player_name)) - 10 * 7
    padding_space = console_width - line_len
    
    bottom_line = ""

    for i in range(console_width):
        bottom_line += "-"

    print(bottom_line)
    if padding_space > -1:
        padding = ""
        for i in range(padding_space - 4):
            padding += " "
        print("  {}{}{}  ".format(player_name, padding, stats_line))
    else:
        print(player_name)
        print(stats_line)
    print(bottom_line)
