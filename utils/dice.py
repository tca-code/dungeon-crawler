from random import randint

def d(count, die):
    value = 0
    while count:
        value += randint(1, die)
        count -= 1
    return value