import random

def dmg():
    return random.randint(1, 5)

def life():
    pass

def combat():
    damage = dmg()
    dmg_desc = None

    if damage < 3:
        dmg_desc = "Weak!"
    else:
        dmg_desc = "Strong!"

    print(f"The enemy does {damage} to you! {dmg_desc}")
