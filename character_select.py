from character import Character
from classes import Warrior
from classes import Medic
from classes import Thief
from classes import Dwarf
from classes import King
from weapons import Weapons
from weapons import Sword
def character_select():
    while True:
        print('Choose your character:')
        print('1. Warrior')
        print('2. Medic')
        print('3. Thief')
        print('4. Dwarf')
        print('5. King')
        selection = input()
        if selection == '1':
            print('You chose the Warrior class!')
            return Warrior(10, 5, Sword, 10)
        
        elif selection == '2':
            print('You chose the Medic class!')
            return Medic(8, 4, Sword, 20)
        
        elif selection == '3':
            print('You chose the Thief!')
            return Thief(6, 4, Sword, 50)

        elif selection == '4':
            print('You chose the Dwarf!')
            return Dwarf(7, 7, Sword, 40)
        
        elif selection == '5':
            print('You chose the King!!')
            return King(20, 15, Sword, 1000)
        else:
            print("Invalid input %r" % selection)