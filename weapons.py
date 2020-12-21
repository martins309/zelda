class Weapons:
    def __init__(self, power, price):
        self.power = power
        self.price = price

class Fist(Weapons):
    def __init__(self):
        self.power = 1
        self.price = 0

class Knife(Weapons):
    def __init__(self):
        self.power = 3
        self.price = 7

class Sword(Weapons):
    def __init__(self):
        self.power = 4
        self.price = 10

class Axe(Weapons):
    def __init__(self):
        self.power = 8
        self.price = 20
    
class Golden_Bow(Weapons):
    def __init__(self):
        self.power = 6
        self.price = 50

class Club(Weapons):
    def __init__(self):
        self.power = 2
        self.price = 5

class Flail(Weapons):
    def __init__(self):
        self.power = 10
        self.price = 100

class FireBreath(Weapons):
    def __init__(self):
        self.power = 1
        self.price = 0