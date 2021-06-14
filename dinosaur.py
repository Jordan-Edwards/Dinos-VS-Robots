class Dinosaur:

    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
        self.energy = 100
        self.attack_power = attack_power
        self.attack_type = ('Gust', 'Hyperbeem', 'Thunder Bolt')

    #def attack(self, dinosaur):
     #   print('You Have Been Attacked!')
     #   robot.health -= self.attack_power
