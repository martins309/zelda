from character import Character
from classes import Warrior
from classes import Medic
from classes import Thief
from classes import Dwarf
from classes import Brawler
from classes import King
from weapons import Weapons
from weapons import Fist
from weapons import Knife
from weapons import Sword
from weapons import Axe
from weapons import Golden_Bow
from weapons import Club
from weapons import Flail

def character_select():
    while True:
        print('Choose your character:')
        print('1. Warrior')
        print('2. Medic')
        print('3. Thief')
        print('4. Dwarf')
        print('5. Brawler')
        selection = input()

        # arguments for classes: (health, damage modifier, default weapon name, 
        # default weapon object, bonus damage percent, bonus damage multiplier,
        # starting gold, looting modifier)

        if selection == '1':
            print('You chose the Warrior class!')
            return Warrior(50, 1.5, "Sword", Sword(), 20, 2, 10, 1)
        
        elif selection == '2':
            print('You chose the Medic class!')
            return Medic(40, 1.0, "Sword", Sword(), 5, 2, 1)
        
        elif selection == '3':
            print('You chose the Thief!')
            return Thief(30, 2, "Knife", Knife(), 10, 2.5, 50, 2)

        elif selection == '4':
            print('You chose the Dwarf!')
            return Dwarf(30, 2, "Axe", Axe(), 25, 2.5, 1.5)

        elif selection == '5':
            print('You chose the Brawler!')
            return Brawler(100, 5, "Fist", Fist(), 50, 2.5, 0, .25)

        elif selection == '6':
            print('You chose the King!!')
            return King(100, 2, "Golden Bow", Golden_Bow(), 50, 2, 1000, 10)

        else:
            print("Invalid input %r" % selection)