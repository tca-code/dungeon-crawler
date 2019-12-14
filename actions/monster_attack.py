def monster_attack(state, monster):
    monster_atk = monster["dmg"]()
    player_shield = state["player"]["equipped_shield"]["remaining"]
    dmg = monster_atk - player_shield
    state["player"]["hp"] -= dmg
    return dmg
    