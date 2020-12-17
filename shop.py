# Weapons Setup
from character import Character
from classes import Warrior
from classes import Medic


def shop():
    pass
# Define each weapon and its attack damage
class Sword(Character):
    def __init__(self, weapon, status_effects = 10):
        self.weapon = "Sword"
        self.status_effects = status_effects
        return "A lightweight battle sword"
class Axe(Character):
    def __init__(self, weapon, status_effects = 8):
        self.weapon = "Axe"
        self.status_effects = status_effects
        return "A lightweight battle Axe"

class Golden_Bow(Character):
    def __init__(self, weapon, status_effects = 6):
        self.weapon = "Golden Bow"
        self.status_effects = status_effects
        return "A lightweight battle Axe"

def weapon_selections():
     while True:
        print("Select your choice of weapon!")
        print("1. Sword")
        print("2. Axe")
        print("Golden Bow")
        selection = input()
        if selection == "1":
            print("You chose the Sword!")
            return Sword(10)
        elif selection == "2":
            print("You chose the Axe!")
            return Axe(8)
        elif selection == "3":
            print("You chose the Golden Bow")
            return Golden_Bow(6)
        else:
            print("Invalid input %r" % selection)


        
