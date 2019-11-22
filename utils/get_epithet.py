import random
from lib.get_csv_contents import get_csv_contents

def get_epithet():
    return random.choice(get_csv_contents("data/epithets.csv"))