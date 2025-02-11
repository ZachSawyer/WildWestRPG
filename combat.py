import random

def dmg():
    return random.randint(1, 5)

def life():
    pass

def combat():
    damage = dmg()
    dmg_desc = None

    if damage < 3:
        dmg_desc = "weak"
    else:
        dmg_desc = "crushing"

    print(f"The enemy deals {dmg_desc} {damage} damage to you!")
