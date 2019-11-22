from .message import message
from lib import is_value

def __format_options(options):
    opt_arr = []

    for i in range(len(options)):
        opt_arr.append("{}) {}".format(str(i + 1), options[i]))

    return opt_arr

def __print_options(options):
    for opt in options:
        print(opt)

def get_player_action(info, options = []):
    print(message(info))
    print("\n")
    
    opts = __format_options(options)
    __print_options(opts)

    player_pick = input("\n> ")

    if is_value.number(player_pick):
        return int(player_pick) - 1

    for i in range(len(options)):
        option = options[i]
        if player_pick.lower() in option.lower():
            return i
    
    return None

