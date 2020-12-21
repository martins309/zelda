# Weapons Setup
from character import Character
from weapons import Weapons
from weapons import Sword
from weapons import Axe
from weapons import Golden_Bow
from orbs import Orbs
from orbs import Diamond_orb
from orbs import Golden_orb
from orbs import Silver_orb
from orbs import Bronze_orb

# class shop applies to all weapons
def stock():
    return [Sword(), Axe(), Golden_Bow(), Diamond_orb(), Golden_orb(), Silver_orb(), Bronze_orb()]

def stock_names():
    return ["Sword", "Axe", "Golden Bow", "Diamond_orb", "Golden_orb", "Silver_orb", "Bronze_orb"]



def shop(gold, inventory):
    while True:
        print("Current Gold: {}".format(gold))
        print('Current Inventory:')
        keys = list(inventory.keys())
        print(keys)
        print("Select your choice of item! (type exit to leave)")
        shop_total = len(stock())
        counter = 1
        while counter <= shop_total:
            print("{}. {}, {} gold".format(counter, stock_names()[counter-1], stock()[counter-1].price))
            counter += 1
        selection = input()
        try:
            selection = int(selection)
            if selection <= shop_total and selection > 0:
                if gold >= stock()[selection-1].price:
                    print("You bought the {} for {} gold".format(stock_names()[selection-1], stock()[selection-1].price))
                    inventory[stock_names()[selection-1]] = stock()[selection-1]
                    gold -= stock()[selection-1].price
                    while True:
                        user_input = input("Would you like to buy anything else? (Y/N)").upper()
                        if user_input == 'Y':
                            pass
                        elif user_input == 'N':
                            return gold, inventory
                        else:
                            print("Invalid input %r" % user_input)
                else:
                    print("Not enough gold!")
            else:
                print("Invalid input %r" % selection)
        except:
            if selection == "exit":
                return gold, inventory
            else:
                print("Invalid input %r" % selection)




        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        

        


    
