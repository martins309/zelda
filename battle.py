from character import Character
from classes import Warrior
from classes import Medic
from enemies import Goblin
from enemies import Shadow
from enemies import Zombie
from enemy_select import enemy_select

import random

def battle(hero):
    enemy = enemy_select()
    print(enemy.isalive)
    while enemy.isalive == True and hero.isalive == True:
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(enemy)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
        if enemy.isalive == True:
            enemy.attack(hero)
        
        if hero.alive == False:
            return "dead"

        print()
        