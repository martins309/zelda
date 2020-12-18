# Weapons Setup
from character import Character
from weapons import Weapons
from weapons import Sword
from weapons import Axe
from weapons import Golden_Bow

# class shop applies to all weapons
def weapons_selection():
    return [Sword(), Axe(), Golden_Bow()]

def shop(gold, inventory):
    while True:
        print("Current Gold: {}".format(gold))
        print("Select your choice of weapon! (type exit to leave)")
        shop_total = len(weapons_selection())
        counter = 1
        while counter <= shop_total:
            print("{}. {}, {} gold".format(counter, weapons_selection()[counter-1], weapons_selection()[counter-1].price))
            counter += 1
        selection = input()
        try:
            selection = int(selection)
            if selection <= shop_total and selection > 0:
                if gold >= weapons_selection()[selection-1].price:
                    print("You bought the {} for {} gold".format(weapons_selection()[selection-1], weapons_selection()[selection-1].price))
                    inventory.append(weapons_selection()[selection-1])
                    gold -= weapons_selection()[selection-1].price
                else:
                    print("Not enough gold!")
            else:
                print("Invalid input %r" % selection)
        except:
            if selection == "exit":
                return gold, inventory
            else:
                print("Invalid input %r" % selection)
        


    
