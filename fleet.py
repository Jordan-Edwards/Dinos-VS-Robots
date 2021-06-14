from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        weapon1 = Weapon("Mecha-Fist", 25)
        weapon2 = Weapon("Plasma Rifle", 50)
        weapon3 = Weapon("BFG 9000", 75)

        robot1 = Robot("Mecha-Mothra", weapon1)
        robot2 = Robot("Mecha-Godzillia", weapon2)
        robot3 = Robot("Mecha-King Ghidorah", weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)