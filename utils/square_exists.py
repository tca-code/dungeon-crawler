def square_exists(state, coords):
    (x, y) = coords
    dungeon = state["dungeon"]
    if x < 0 or y < 0:
        return False
    try:
        dungeon[y][x]
        return True
    except IndexError:
        return False
    