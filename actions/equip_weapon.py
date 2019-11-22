from copy import deepcopy

def equip_weapon(state, weapon):
    new_state = deepcopy(state)

    weapon_data = {
        "dmg": weapon["dmg"],
        "name": weapon["name"],
        "id": weapon["id"]
    }

    new_state["weapons"].append(weapon_data)
    new_state["player"]["equipped_weapon"] = weapon_data

    return new_state