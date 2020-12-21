class Orbs: 
    def __init__(self, health, price):
        self.health = health 
        self.price = price

class Golden_orb(Orbs):
    def __init__(self):
        self.health = 7
        self.price = 10

class Silver_orb(Orbs):
    def __init__(self):
        self.health = 5
        self.price = 7

class Bronze_orb(Orbs):
    def __init__(self):
        self.health = 3
        self.price = 5

class Diamond_orb(Orbs):
    def __init__(self):
        self.health = 10
        self.price = 20




