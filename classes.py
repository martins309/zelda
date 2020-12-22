from character import Character
import random

class Warrior(Character):
    def __str__(self):
        return "Warrior"

class Medic(Character):
    def __str__(self):
        return "Medic"

    def alive(self):
        modifier = random.randint(1, 5)
        if modifier == 3:
            print('The Medic recovered 10 hp!')
            self.health += 10
        if self.health < 1:
            self.isalive = False

class Thief(Character):
    def steal(self, enemy, hero):
        modifier = enemy.gold * self.looting_modifier * random.randint(1, 3)
        if modifier ==  3 or modifier == 2:
            print("The thief just took your gold!")
        else:
            enemy.attack(hero, hero, enemy, enemy.bonus_damage_percent, enemy.bonus_damage_multiplier)
    
    def __str__(self):
        return "Thief"
        
class King(Character):
    def __str__(self):
        return "King"
    
class Dwarf(Character):
    def __str__(self):
        return "Dwarf"

class Brawler(Character):
    def __str__(self):
        return "Brawler"