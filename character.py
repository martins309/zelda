import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.isalive = True

    def alive(self):
        if self.health < 1:
            self.isalive = False

    def print_status(self):
        print("The %s has %d health and %d power." % (self, self.health, self.power))

    def choose_direction(self, direction):
        while True:
            if direction == "W" or direction == 1:
                return "up"
            elif direction == "S" or direction == 2:
                return "down"
            elif direction == "A" or direction == 3:
                return "left"
            elif direction == "D" or direction == 4:
                return "right"
            else:
                print('Invalid input\n')
                direction = input("Choose a direction")

    def attack(self, opponent):
        attack_direction = self.choose_direction(input("Pick a direction to attack (use WASD)"))
        block_direction = opponent.choose_direction(random.randint(1, 4))
        if attack_direction == block_direction:
            print("The {} blocked the attack!")
        else:
            opponent.health -= self.power
            print("The %s does %d damage to the %s." % (self, self.power, opponent))
            opponent.alive()
            if opponent.isalive == False:
                print("The %s is dead." % opponent)