from character import Character
import random

class Goblin(Character):
    def __str__(self):
        return "Goblin"

class Zombie(Character):
    def __str__(self):
        return "Zombie"

    def alive(self):
        if self.health < -19:
                self.isalive = False

class Shadow(Character):
    def __str__(self):
        return "Shadow"
    
    def alive(self):
        modifier = random.randint(1, 10)
        if modifier == 10:
            if self.health < 1:
                self.isalive = False
        else:
            print('The shadow dodged the attack!')
            self.health = 1