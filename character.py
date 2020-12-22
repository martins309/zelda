import random
from weapons import Weapons
from weapons import Weapons
from weapons import Fist
from weapons import Knife
from weapons import Sword
from weapons import Axe
from weapons import Golden_Bow
from weapons import Club
from weapons import Flail
from orbs import Orbs
from orbs import Diamond_orb
from orbs import Golden_orb
from orbs import Silver_orb
from orbs import Bronze_orb


class Character:
    def __init__(self, health, damage_modifier, default_weapon_name, default_weapon, bonus_damage_percent = 0, bonus_damage_multiplier = 1, default_gold = 0, looting_modifier = 1):
        self.health = health
        self.damage_modifier = damage_modifier
        self.isalive = True
        self.weapon = default_weapon
        self.gold = default_gold
        self.looting_modifier = looting_modifier
        self.inventory = {
            default_weapon_name: [default_weapon],
            "Fist": [Fist()]
            }
        self.equipped_weapon = default_weapon_name
        self.bonus_damage_percent = bonus_damage_percent
        self.bonus_damage_multiplier = bonus_damage_multiplier

    def alive(self):
        if self.health < 1:
            self.isalive = False

    def print_status(self):
        print("The {} has {} health and has a damage modifier of {}".format(self, self.health, self.damage_modifier))

    def choose_direction(self, direction):
        while True:
            print(direction)
            if direction == "w" or direction == 1:
                return "up"
            elif direction == "s" or direction == 2:
                return "down"
            elif direction == "a" or direction == 3:
                return "left"
            elif direction == "d" or direction == 4:
                return "right"
            else:
                print("Invalid input")
                direction = input("Choose a direction")

    def attack(self, opponent, hero, enemy, bonus_damage_percent, bonus_damage_multiplier):
        if self == hero:
            attack_direction = self.choose_direction(input("Pick a direction to attack (use WASD)").lower())
            block_direction = self.choose_direction(random.randint(1, 4))
        else:
            block_direction = self.choose_direction(input("Pick a direction to block (use WASD)").lower())
            attack_direction = self.choose_direction(random.randint(1, 4))
        if attack_direction == block_direction:
            print("The {} blocked the attack!".format(opponent))
        else:
            random_percent = random.randint(1, 100)
            if random_percent <= bonus_damage_percent:
                bdamage = float(bonus_damage_multiplier)
            else:
                bdamage = 1
            opponent.health -= round(self.inventory[self.equipped_weapon][0].power * self.damage_modifier * bdamage)
            print("The {} does {} damage to the {} with the {}.".format(self, round(self.inventory[self.equipped_weapon][0].power * self.damage_modifier * bdamage), opponent, self.equipped_weapon))
            opponent.alive()
            if opponent.isalive == False:
                print("The %s is dead." % opponent)

    def use_item(self):
        print("Current inventory:")
        keys = list(self.inventory.keys())
        print(keys)
        while True:
            input1 = input("Which item would you like to use? (type 'exit' to cancel)")
            if input1 in self.inventory:
                if issubclass(type(self.inventory[input1]), Weapons):
                    while True:
                        input2 = input("Would you like to change your weapon to {} (Y/N)".format(input1)).upper()
                        if input2 == "Y":
                            print('equipped the {}'.format(input1))
                            keys = list(self.inventory.keys())
                            equipped_weapon_index = keys.index(input1)
                            self.equipped_weapon = keys[equipped_weapon_index]
                            break
                        elif input2 == "N":
                            break
                        else:
                            print("Invalid input %r" % input2)
                    break
                elif issubclass(type(self.inventory[input1]), Orbs):
                    print("used the {} to heal {} health".format(input1, self.inventory[input1].health))
                    self.health += self.inventory[input1].health
                    self.inventory.pop(input1)[0]
                    if len(self.inventory[input1]) == 0:
                        del self.inventory[input1]
                    break
                else:
                    pass
            elif input1 == "exit":
                break
            else:
                print("Invalid input %r" % input1)

    def pillage(self, enemy):
        self.gold += enemy.gold * self.looting_modifier
        print("The {} looted {} gold from the corpse of the {}".format(self, enemy.gold * self.looting_modifier, enemy))