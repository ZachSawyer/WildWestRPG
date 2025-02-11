import random

def dmg():
    return random.randint(1, 5)

def life():
    pass

def combat():
    damage = dmg()
    print(f"The enemy does {damage} to you!")