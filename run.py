from character import Character
from classes import Warrior
from classes import Medic
from enemies import Goblin
from enemies import Shadow
from enemies import Zombie
from inventory import inventory
import random
from character_select import character_select
from battle import battle
from shop import shop



def main():
    status = ''
    while status != "dead":
        print('What do you want to do?')
        print('1. Battle')
        print('2. Shop')
        print('3. inventory')
        selection = input()
        if selection == '1':
            print('You go to battle!')
            status = battle(hero)
        elif selection == '2':
            print('You go to the shop!')
            shop()
        elif selection == '3':
            wgi = inventory(hero.weapon, hero.gold, hero.inventory)
            hero.weapon = wgi[0]
            hero.gold = wgi[1]
            hero.inventory = wgi[2]
        else:
            print("Invalid input %r" % selection)



end = False

hero = character_select() 
main()
