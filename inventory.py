
from weapons import Weapons
from weapons import Sword

def inventory(weapon, gold, inventory):
    while True:
        print('Here is your current weapon: {}'.format(weapon))
        print('Here is your current gold: {}'.format(gold))
        print('Here is your inventory:')
        print(inventory)

        print('What would you like to do?')
        print('1. change weapon')
        print('2. drop item')
        user_input = input()
        if user_input == "1":
            #wgi stands from weapon gold inventory
            wgi = equip_weapon(weapon, inventory)
            weapon = wgi[0]
            inventory = wgi[1]
            return weapon, gold, inventory
        elif user_input == "2":
            inventory = drop_item(inventory)
            return weapon, gold, inventory

def equip_weapon(weapon, inventory):
    while True:
        equip = input('which weapon would you like to equip? (type exit to cancel)')
        if equip in inventory:
            print('equipped the {}'.format(equip))
            store = weapon
            weapon = inventory.pop(inventory.index(equip))
            inventory.append(store)
            return weapon, inventory
        elif equip.lower() == 'exit':
            break
        else:
            print('Item not in inventory, please try again')

def drop_item(inventory):
    while True:
        dropped_item = input('which item would you like to drop? (type exit to cancel)')
        if dropped_item in inventory:
            print('dropped the {}'.format(dropped_item))
            inventory.pop(inventory.index(dropped_item))
            return inventory
        elif dropped_item.lower() == 'exit':
            break
        else:
            print('Item not in inventory, please try again')
