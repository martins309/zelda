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
from weapons import Weapons
from weapons import Sword
from weapons import Axe
from weapons import Golden_Bow
from selection import selection

def title_screen():
    print("###########################")
    print("#### Welcome to Merikh ####")
    print("###########################")
    print("###### By Team Yoshi ######")

def main():
    status = ''
    while status != "dead":
        try:
            print('What do you want to do?')
            select = selection(["Battle", "Shop", "Inventory"], 0)
            if select[1] == 'Battle':
                print('You go to battle!')
                status = battle(hero)
            elif select[1] == 'Shop':
                print('You go to the shop!')
                wgi = shop(hero.gold, hero.inventory, hero)
                hero.gold = wgi[0]
                hero.inventory = wgi[1]
            elif select[1] == 'Inventory':
                wgi = inventory(hero.equipped_weapon, hero.gold, hero.inventory, hero)
                hero.equipped_weapon = wgi[0]
                hero.gold = wgi[1]
                hero.inventory = wgi[2]
            else:
                print("Invalid input %r" % select[1])
        except:
            print("Invalid input")


title = title_screen()
end = False
hero = character_select() 
main()
