from dice import d

MONSTERS_EASY = [
    {
        "xp": 200,
        "name": "Giant Centipede",
        "armor": 0,
        "hp": 5,
        "dmg": lambda: d(1, 6),
        "weapon": "Bite"
    },
    {
        "xp": 200,
        "name": "Giant Centipede",
        "armor": 0,
        "hp": 7,
        "dmg": lambda: d(1, 6),
        "weapon": "Bite"
    },
    {
        "xp": 200,
        "name": "Dream Spider",
        "armor": 0,
        "hp": 5,
        "dmg": lambda: d(1, 3),
        "weapon": "Bite"
    },
]

MONSTERS_MED = [
    {
        "xp": 400,
        "name": "Hobgoblin Fighter",
        "armor": 3,
        "hp": 17,
        "dmg": lambda: d(1, 8) + 2,
        "weapon": "Longsword"
    },
    {
        "xp": 400,
        "name": "Golden-Clad Skeleton",
        "armor": 2,
        "hp": 8,
        "dmg": lambda: d(1, 6),
        "weapon": "Scimitar"
    },
    {
        "xp": 400,
        "name": "Wolf",
        "armor": 0,
        "hp": 13,
        "dmg": lambda: d(1, 6),
        "weapon": "Bite"
    },
]

MONSTERS_HARD = [
    {
        "xp": 800,
        "name": "Dragon",
        "armor": 5,
        "hp": 22,
        "dmg": lambda: d(1, 12),
        "weapon": "Bite"
    },
    {
        "xp": 800,
        "name": "Cave Troll",
        "armor": 0,
        "hp": 40,
        "dmg": lambda: d(1, 8) + 7,
        "weapon": "Pummel"
    },
]

DRAGON_KING = {
    "xp": 19200,
    "name": "Dragon King",
    "armor": 18,
    "hp": 189,
    "dmg": lambda: d(2, 12) + 15,
    "weapon": "NO SURVIVAL"
}