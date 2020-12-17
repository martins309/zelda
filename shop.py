# Weapons Setup
from character import Character
from classes import Warrior
from classes import Medic

# class shop applies to all weapons
def shop():
    sword = sword()
    axe = axe()
    bow = bow()
class weapons_selection():
    def __init__(weapons_selection, sword, axe, bow):

# Define each weapon and its attack damage
class sword(weapons_selection):
    def __init__(weapon_selection, status_effects = 8):
        weapon_selection.weapon = "Axe"
        weapon_selection.status_effects = status_effects
        return "A lightweight battle Axe"

    def __init__(weapon_selection, status_effects = 10):
        weapon_selection.weapon = "sword"
        weapon_selection.status_effects = status_effects
        return "A battle sword"
class Axe(weapons_selection):
    def __init__(weapon_selection, status_effects = 8):
        weapon_selection.weapon = "Axe"
        weapon_selection.status_effects = status_effects
        return "A lightweight battle Axe"

class Bow(weapons_selection):
    def __init__(self, weapon, status_effects = 6):
        weapon_selection.weapon = "Bow"
        weapon_selection.status_effects = status_effects
        return "A Golden Bow"


# Objects

class weapons_selection:
    def weapons_selection():
        def __init__(weapons_selection, sword, axe, bow):
            while True:
                print("Select your choice of weapon!")
                print("1. Sword")
                print("2. Axe")
                print("3.Golden Bow")
                selection = input()
            if selection == "1":
                print("You chose the Sword!")
                return Sword(10)
            elif selection == "2":
                print("You chose the Axe!")
                return Axe(8)
            elif selection == "3":
                print("You chose the Bow")
                return Bow(6)
           


    
