from utils.dice import d

weapons = {
    "1": {
        "id": 1,
        "name": "Fists",
        "dmg": lambda: d(1, 4),
        "discoverable": False
    },
    "2": {
        "id": 2,
        "name": "Short Sword",
        "dmg": lambda: d(1, 4),
        "discoverable": False
    },
    "3": {
        "id": 3,
        "name": "Handaxe",
        "dmg": lambda: d(1, 4),
        "discoverable": False
    },
    "4": {
        "id": 4,
        "name": "Spear",
        "dmg": lambda: d(1, 6),
        "discoverable": False
    }
}