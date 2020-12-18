from character import Character
from enemies import Goblin
from enemies import Shadow
from enemies import Zombie
from weapons import Weapons
from weapons import Sword
from weapons import Fist
from enemies import Ogre 
from enemies import Gigant 
from enemies import Dragon
from weapons import Club
from weapons import Flail
from weapons import FireBreath


def enemy_select():
    while True:
        print('Choose your foe:')
        print('1. Goblin')
        print('2. Shadow')
        print('3. Zombie')
        print('4. Ogre')
        print('5. Gigant')
        print('6. Dragon')
        selection = input()
        if selection == '1':
            print('You chose the Goblin enemy!')
            return Goblin(6, 1, Sword(), 5)
        elif selection == '2':
            print('You chose the Shadow enemy!')
            return Shadow(1, 1, Fist(), 1)
        elif selection == '3':
            print('You chose the Zombie enemy!')
            return Zombie(5, 1, Fist(), 1)
        elif selection == '4':
            print('You chose the Ogre enemy!')
            return Ogre (10, 7, Club(), 7)
        elif selection == '5':
            print('you chose the Gigant enemy!')
            return Gigant (20, 10, Flail(), 30)
        elif selection == '6':
            print('you chose the Dragon enemy!')
            return Dragon (50, 20, FireBreath(), 50)
        else:
            print("Invalid input %r" % selection)