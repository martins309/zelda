class Weapons:
    def __init__(self, power, price):
        self.power = power

class Fist(Weapons):
    def __init__(self):
        self.power = 1
        self.price = 0
    def __str__(self):
        return "Fist"

class Sword(Weapons):
    def __init__(self):
        self.power = 4
        self.price = 10
    def __str__(self):
        return "Sword"

class Axe(Weapons):
    def __init__(self):
        self.power = 8
        self.price = 20
    def __str__(self):
        return "Axe"
    
class Golden_Bow(Weapons):
    def __init__(self):
        self.power = 6
        self.price = 50
    def __str__(self):
        return "Golden Bow"

class Club(Weapons):
    def __init(self):
        self.power = 7
        self.price = 12
    def __str__(self):
        return "Club"

class Flail(Weapons):
    def __init__(self):
        self.power = 30
        self.price = 30
    def __str__(self):
        return "Flail"

class FireBreath(Weapons):
    def __init__(self):
        self.power = 50
        self.price = 50
    def __str__(self):
        return "FireBreath"