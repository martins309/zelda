from character import Character
import random



    
class Goblin(Character):
    def __str__(self):
        return "Goblin"

class Zombie(Character):
    def __str__(self):
            return "Zombie"

    def alive(self):
        if self.health < -50:
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

class Ogre(Character):
    def __str__(self):
        return "Ogre"
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
            modifier = random.randint(1, 7)
            if modifier == 7:
                serious_damage = 7
            else:
                serious_damage = 5
            opponent.health -= round(self.weapon.power * self.damage_modifier) + serious_damage
            print("The %s does %d damage to the %s." % (self, round(self.weapon.power * self.damage_modifier) + serious_damage, opponent))
            opponent.alive()
            if opponent.isalive == False:
                print("The %s is dead." % opponent)

          

    
class Gigant(Character):
    def __str__(self):
        return "Gigant"
    
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
            modifier = random.randint(1, 7)
            if modifier == 7:
                serious_damage = 7
            else:
                serious_damage = 5
            opponent.health -= round(self.weapon.power * self.damage_modifier) + serious_damage
            opponent.health -= round(self.weapon.power * self.damage_modifier)
            print("The %s does %d damage to the %s." % (self, round(self.weapon.power * self.damage_modifier), opponent))
            opponent.alive()
            if opponent.isalive == False:
                print("The %s is dead." % opponent) 

        
    
class Dragon(Character):
    def __str__(self):
        return "Dragon"
    
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
            modifier = random.randint(1, 7)
            if modifier == 7:
                serious_damage = 7
            else:
                serious_damage = 5
            opponent.health -= round(self.weapon.power * self.damage_modifier) + serious_damage
            opponent.health -= round(self.weapon.power * self.damage_modifier)
            print("The %s does %d damage to the %s." % (self, round(self.weapon.power * self.damage_modifier), opponent))
            opponent.alive()
            if opponent.isalive == False:
                print("The %s is dead." % opponent)
        modifier = random.randint(1, 3)
        if modifier == 2 or modifier == 3:
            serious_damage = 10
        else:
            serious_damage = 9
        opponent.health -= self.power*serious_damage
        print("The %s does %d damage to the %s." % (self, self.power*serious_damage, opponent))
        
    
    
    