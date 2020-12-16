from character import Character
import random

class Warrior(Character):
    def __str__(self):
        return "Warrior"

    def attack(self, opponent):
        modifier = random.randint(1, 5)
        if modifier == 5:
            bonus_damage = 2
        else:
            bonus_damage = 1
        opponent.health -= self.power*bonus_damage
        print("The %s does %d damage to the %s." % (self, self.power*bonus_damage, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)

class Medic(Character):
    def __str__(self):
        return "Medic"
    
    def alive(self):
        modifier = random.randint(1, 5)
        if modifier == 5:
            print('The Medic recovered 2 hp!')
            self.health += 2
        if self.health < 1:
            self.isalive = False