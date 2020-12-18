import random

class Character:
    def __init__(self, health, damage_modifier, default_weapon, default_gold):
        self.health = health
        self.damage_modifier = damage_modifier
        self.isalive = True
        self.weapon = default_weapon
        self.gold = default_gold
        self.inventory = ['a', 's', 'w', 'd']

    def alive(self):
        if self.health < 1:
            self.isalive = False

    def print_status(self):
        print("The {} has {} health and has a damage modifier of {}".format(self, self.health, self.damage_modifier))

    def choose_direction(self, direction):
        while True:
            if direction == "w" or direction == 1:
                return "up"
            elif direction == "s" or direction == 2:
                return "down"
            elif direction == "a" or direction == 3:
                return "left"
            elif direction == "d" or direction == 4:
                return "right"
            else:
                print('Invalid input\n')
                direction = input("Choose a direction")

    def attack(self, opponent, hero, enemy):
        if self == hero:
            attack_direction = self.choose_direction((input("Pick a direction to attack (use WASD)")).lower())
            block_direction = opponent.choose_direction(random.randint(1, 4))
        else:
            block_direction = self.choose_direction((input("Pick a direction to block (use WASD)")).lower())
            attack_direction = self.choose_direction(random.randint(1, 4))
        if attack_direction == block_direction:
            print("The {} blocked the attack!".format(opponent))
        else:
            opponent.health -= round(self.weapon.power * self.damage_modifier)
            print("The %s does %d damage to the %s." % (self, round(self.weapon.power * self.damage_modifier), opponent))
            opponent.alive()
            if opponent.isalive == False:
                print("The %s is dead." % opponent)