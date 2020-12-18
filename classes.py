from character import Character
import random

class Warrior(Character):
    def __str__(self):
        return "Warrior"

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
            modifier = random.randint(1, 5)
            if modifier == 5:
                bonus_damage = 2
            else:
                bonus_damage = 1
            opponent.health -= round(self.weapon.power * self.damage_modifier * bonus_damage)
            print("The %s does %d damage to the %s." % (self, round(self.weapon.power * self.damage_modifier * bonus_damage), opponent))
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


class Thief(Character):
    def __str__(self):
        return "Thief"


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
        opponent.health -= self.damage_modifier*bonus_damage
        print("The %s does %d damage to the %s." % (self, self.damage_modifier*bonus_damage, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)


class Dwarf(Character):
    def __str__(self):
        return "Dwarf"
