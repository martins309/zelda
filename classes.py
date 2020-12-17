from character import Character
import random

class Warrior(Character):
    def __str__(self):
        return "Warrior"

    def attack(self, opponent):
        modifier = random.randint(1, 5)
        if modifier == 5:
            bonus_damage = 3
        else:
            bonus_damage = 2
        opponent.health -= self.power*bonus_damage
        print("The %s does %d damage to the %s." % (self, self.power*bonus_damage, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)


    
    def alive(self):
        modifier = random.randint(1, 4)
        if modifier == 4:
            print('The Warrior recovered 6 hp!')
            self.health += 3
        if self.health < 1:
            self.isalive = False




class Medic(Character):
    def __str__(self):
        return "Medic"

    def attack(self, opponent):
        modifier = random.randint(1, 7)
        if modifier == 7:
            bonus_damage = 2
        else:
            bonus_damage = 1
        opponent.health -= self.power*bonus_damage
        print("The %s does %d damage to the %s." % (self, self.power*bonus_damage, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)
    
    def alive(self):
        modifier = random.randint(1, 5)
        if modifier == 5:
            print('The Medic recovered 2 hp!')
            self.health += 2
        if self.health < 1:
            self.isalive = False


class Thief(Character):
    def __str__(self):
        return "Thief"

    def attack(self, opponent):
        modifier = random.randint(1, 6)
        if modifier == 6:
            bonus_damage = 3
        else:
            bonus_damage = 1
        opponent.health -= self.power*bonus_damage
        print("The %s does %d damage to the %s." % (self, self.power*bonus_damage, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)


    def alive(self):
        modifier = random.randinit(1, 7) 
        if modifier == 6 or modifier == 7: 
            print('The Thief recovered 5 hp') 
            self.health += 1
        if self.health < 1:
            self.health = False 


class King(Character):
    def __str__(self):
        return "King"

#this is for bonus damage. 
    def attack(self, opponent):
        modifier = random.randint(1, 3)
        if modifier == 2 or modifier == 3:
            bonus_damage = 10
        else:
            bonus_damage = 7
        opponent.health -= self.power*bonus_damage
        print("The %s does %d damage to the %s." % (self, self.power*bonus_damage, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)

    def alive(self):
        modifier = random.randinit(1,3)
        if modifier == 1 or modifier == 2 or modifier == 3: 
            print('The King has recovered 10 hp!')
            self.health += 5 
        if self.health < 1: 
            self. health = False 


class Dwarf(Character):
    def __str__(self):
        return "Dwarf"

    def attack(self, opponent):
        modifier = random.randint(1, 4)
        if modifier == 2 or modifier == 4:
            bonus_damage = 5
        else:
            bonus_damage = 3
        opponent.health -= self.power*bonus_damage
        print("The %s does %d damage to the %s." % (self, self.power*bonus_damage, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)
    
    def alive(self):
        modifier = random.randinit(1, 4)
        if modifier == 4: 
            print('The Dward has recovered 4 hp!')
            self.health += 3
        if self.health < 1: 
            self. health = False 