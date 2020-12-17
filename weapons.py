class Weapons:
    def __init__(self, power):
        self.power = power

class Sword(Weapons):
    def __init__(self):
        self.power = 6

    def __str__(self):
        return "Sword"
    
    