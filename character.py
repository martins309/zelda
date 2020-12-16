class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.isalive = True

    def attack(self, opponent):
        opponent.health -= self.power
        print("The %s does %d damage to the %s." % (self, self.power, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)

    def alive(self):
        if self.health < 1:
            self.isalive = False

    def print_status(self):
        print("The %s has %d health and %d power." % (self, self.health, self.power))