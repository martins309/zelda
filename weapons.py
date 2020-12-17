class Weapons:
    def __init__(self, power):
        self.power = power

class Sword(Weapons):
    def __init__(self):
        self.power = 4
    def __str__(self):
        return "Sword"

class Axe(Weapons):
    def __init__(self):
        self.power = 8
    def __str__(self):
        return "Axe"
    
class Golden_Bow(Weapons):
    def __init__(self):
        self.power = 6
    def __str__(self):
        return "Golden Bow"