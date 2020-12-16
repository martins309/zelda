from character import Character
from enemies import Goblin
from enemies import Shadow
from enemies import Zombie


def enemy_select():
    while True:
        print('Choose your foe:')
        print('1. Goblin')
        print('2. Shadow')
        print('3. Zombie')
        selection = input()
        if selection == '1':
            print('You chose the Goblin enemy!')
            return Goblin(6, 2)
        elif selection == '2':
            print('You chose the Shadow enemy!')
            return Shadow(1, 1)
        elif selection == '3':
            print('You chose the Zombie enemy!')
            return Zombie(5, 2)
        else:
            print("Invalid input %r" % selection)