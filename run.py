from character import Character
from classes import Warrior
from classes import Medic
from enemies import Goblin
from enemies import Shadow
from enemies import Zombie
import random
from character_select import character_select
from enemy_select import enemy_select
from battle import battle
from shop import shop

def main():
    while battle != "dead":
        print(battle)
        print('Where would you like to go?')
        print('1. Battle')
        print('2. Shop')
        selection = input()
        if selection == '1':
            print('You go to battle!')
            battle()
        elif selection == '2':
            print('You go to the shop!')
            shop()
        else:
            print("Invalid input %r" % selection)

end = False
print('hi')
hero = character_select() 

main()
