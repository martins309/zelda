from character import Character
from classes import Warrior
from classes import Medic


def character_select():
    while True:
        print('Choose your character:')
        print('1. Warrior')
        print('2. Medic')
        selection = input()
        if selection == '1':
            print('You chose the Warrior class!')
            return Warrior(10, 5)
        elif selection == '2':
            print('You chose the Medic class!')
            return Medic(8, 4)
        else:
            print("Invalid input %r" % selection)