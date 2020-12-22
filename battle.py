from character import Character
from classes import Warrior
from classes import Medic
from enemies import Goblin
from enemies import Shadow
from enemies import Zombie
from enemy_select import enemy_select
from orbs import Orbs
from orbs import Diamond_orb
from orbs import Golden_orb
from orbs import Silver_orb
from orbs import Bronze_orb

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
        print("3. use an item")
        print("4. flee")
        user_input = input()
        if user_input == "1":
            hero.attack(enemy, hero, enemy, hero.bonus_damage_percent, hero.bonus_damage_multiplier)
        elif user_input == "2":
            pass
        elif user_input == "3":
            hero.use_item()
        elif user_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.isalive == True:
            enemy.attack(hero, hero, enemy, enemy.bonus_damage_percent, enemy.bonus_damage_multiplier)
        if enemy.isalive == False:
            hero.pillage(enemy)

        if hero.isalive == False:
            print("Game Over")
            return "dead"
        else:
            pass

        print()
        