from copy import deepcopy
import random
import math
from lib.dot_prop import get

def generate_dungeon(map_height, map_width):
    base_level = [[0
        for y in range(map_height)]
            for x in range(map_width)]
    
    level_with_exit = __place_exit(__wall_off_dungeon(base_level))

    obstacle_count = math.ceil((map_height * map_width) * 0.05)
    return __place_obstacles(level_with_exit, obstacle_count)


def __wall_off_dungeon(dungeon):
    new_dungeon = deepcopy(dungeon)
    for y in range(len(dungeon)):
        for x in range(len(dungeon[y])):
            if x is 0:
                new_dungeon[y][x] = 1
            elif y is 0:
                new_dungeon[y][x] = 1
            elif y is len(dungeon) - 1:
                new_dungeon[y][x] = 1
            elif x is len(dungeon[y]) - 1:
                new_dungeon[y][x] = 1
    return new_dungeon

def __place_exit(dungeon):
    new_dungeon = deepcopy(dungeon)
    exit_x_location = random.randint(1, len(dungeon[0]) - 2)
    new_dungeon[1][exit_x_location] = 3
    return new_dungeon

def __place_obstacles(dungeon, obstacle_count):
    new_dungeon = deepcopy(dungeon)
    coords = []
    
    for y in range(len(dungeon)):
        for x in range(len(dungeon[y])):
            if dungeon[y][x] is 0:
                coords.append((x, y))
    
    choices = random.choices(population=coords, k=obstacle_count)
    
    for (x, y) in choices:
        new_dungeon[y][x] = 1
    
    return new_dungeon

