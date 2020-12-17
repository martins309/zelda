# Weapons Setup
from character import Character
from weapons import Weapons
from weapons import Sword
from weapons import Axe
from weapons import Golden_Bow

# class shop applies to all weapons
def weapons_selection():
    return Sword, Axe, Golden_Bow

def shop(gold, inventory):
    while True:
        print("Current Gold: {}".format(gold))
        print("Select your choice of weapon! (type exit to leave)")
        print("1. Sword, 10 gold")
        print("2. Axe, 20 gold")
        print("3. Golden Bow, 50 gold")
        selection = input()
        if selection == "1" and gold >= 10:
            print("You bought the Sword for 10 gold")
            inventory.append(Sword)
            gold -= 10
        elif selection == "2" and gold >= 20:
            print("You bought the Axe for 20 gold!")
            inventory.append(Axe)
            gold -= 20
        elif selection == "3" and gold >= 50:
            print("You bought the Golden Bow for 50 gold!")
            inventory.append(Golden_Bow)
            gold -= 50
        elif selection == "exit":
            return inventory, gold
        else:
            print("Invalid input %r" % selection)
        


    
