from weapon import Weapon


class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 100
        self.power_level = 150
        self.weapon = Weapon
        self.weapon_choice = ['Mecha-Fist', 'Plasma Rifle', 'BFG 9000']

    def attack(self, dinosaur):
        print('You Have Been Attacked!')
        dinosaur.health -= self.weapon.attack_power
