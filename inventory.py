
from weapons import Weapons
from weapons import Sword

def inventory(equipped_weapon, gold, inventory):
    while True:
        print('Here is your current weapon: {}'.format(equipped_weapon))
        print('Here is your current gold: {}'.format(gold))
        print('Here is your inventory:')
        keys = list(inventory.keys())
        print(keys)
        print('What would you like to do? (type \'exit\' to exit)')
        print('1. change weapon')
        print('2. drop item')
        while True:
            user_input = input()
            if user_input == "1":
                wi = list(equip_weapon(equipped_weapon, inventory))
                equipped_weapon = wi[0]
                inventory = wi[1]
                return equipped_weapon, gold, inventory
            elif user_input == "2":
                wi = list(drop_item(equipped_weapon, inventory))
                equipped_weapon = wi[0]
                inventory = wi[1]
                return equipped_weapon, gold, inventory
            elif user_input == "exit":
                return equipped_weapon, gold, inventory
            else:
                print("Invalid input {}".format(user_input))


def equip_weapon(equipped_weapon, inventory):
    while True:
        equip = input('which weapon would you like to equip? (type exit to cancel)')
        print(equip)
        if equip in inventory:
            print('equipped the {}'.format(equip))
            keys = list(inventory.keys())
            equipped_weapon_index = keys.index(equip)
            equipped_weapon = keys[equipped_weapon_index]
            return equipped_weapon, inventory
        elif equip.lower() == 'exit':
            return equipped_weapon, inventory
        else:
            print('Item {} not in inventory, please try again'.format(equip))

def drop_item(equipped_weapon, inventory):
    while True:
        dropped_item = input('which item would you like to drop? (type exit to cancel)')
        if dropped_item in inventory:
            if dropped_item != equipped_weapon:
                print('dropped the {}'.format(dropped_item))
                inventory.pop(dropped_item)
                return equipped_weapon, inventory
            else:
                print("Cannot drop the currently equipped weapon!")
                return equipped_weapon, inventory
        elif dropped_item.lower() == 'exit':
            return equipped_weapon, inventory
        else:
            print('Item not in inventory, please try again')
