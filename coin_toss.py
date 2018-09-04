from random import random

def flip_coin():
    r = random()
    return "Heads" if r > 0.5 else "Tails"

print(flip_coin())
    