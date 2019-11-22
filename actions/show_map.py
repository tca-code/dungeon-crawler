from lib.color import Color

def show_map(dungeon, visited_squares = [], debug = False):
    d = ""
    wall = Color("#").cyan().render()
    door = Color("x").yellow().render()
    path = Color(".").dim().render()
    for y in range(len(dungeon)):
        for x in range(len(dungeon[y])):
            tile = dungeon[y][x]
            if debug:
                if tile is 1:
                    d += wall
                elif tile is 3:
                    d += door
                elif tile is 0:
                    d += path
            else:
                is_outer_wall = (
                    y is 0 or
                    x is 0 or
                    y is len(dungeon) - 1 or
                    x is len(dungeon[y]) - 1
                )
                if is_outer_wall:
                    d += wall
                    continue
                
                if (x, y) in visited_squares:
                    if tile is 1:
                        d += wall
                    elif tile is 3:
                        d += door
                    elif tile is 0:
                        d += path
                else:
                    d += "#"

        d += "\n"
    return d