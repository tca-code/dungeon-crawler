from data.weapons import weapons

def player_attack(player, monster):
    player_weapon = weapons[str(player["equipped_weapon"]["id"])]
    dmg = player_weapon["dmg"]()
    monster["hp"] -= dmg
    return dmg
