import random

from .get_epithet import get_epithet
from .dungeon import generate_dungeon

def init_state(player_name, starting_hp):
    dungeon = generate_dungeon(45, 20)

    suitable_coords = []
    y = len(dungeon) - 2
    for x in range(len(dungeon[y])):
        if dungeon[y][x] is 0:
            suitable_coords.append((x, y))
    
    starting_coords = random.choice(suitable_coords)
            

    initial_state = {
        "combat": None,
        "victories": [],
        "player": {
            "hp": starting_hp,
            "name": player_name,
            "title": get_epithet(),
            "equipped_shield": {
                "max": 0,
                "remaining": 0,
            },
            "equipped_weapon": {
                "name": "Fists",
                "id": 1
            }
        },
        "victories": [],
        "inventory": [],
        "weapons": [],
        "dungeon": dungeon,
        "visited": [starting_coords],
        "coords": starting_coords,
    }
    return initial_state