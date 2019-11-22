from lib.dot_prop import get

'''
1. Return a dict with up, down, left, right
2. Each option should have either a bool or a string
    1. If you can proceed in that direction, it will return True
    2. If not, return a descriptor of the obstacle
'''

def get_available_directions(state):
    current_location = get(state, "coords")
    dungeon = get(state, "dungeon")
    