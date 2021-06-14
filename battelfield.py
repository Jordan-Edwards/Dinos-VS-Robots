from herd import Herd
from fleet import Fleet
import random

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()


    def welcome_message(self):
        print('Welcome to my devCodeCamp OOP Project')
        print('The Robots belong to a Fleet just as the Dinosaurs belong to the Herd.')
        #print(f'{self.herd.dinosaurs[0].type}')

    def pick_a_side(self):
        pick_a_side = int(input('Pick a Side!: (0) Robots; (1) Dinosaurs'))
        if pick_a_side == 0:
            print('You have picked Robots!')
        elif pick_a_side == 1:
            print('You have picked Dinosaurs!')
        else:
            print("Not an Option")

    def dinosaurs_options_opponent(self):
        i = 1
        for element in self.fleet.robots:
            print(f'{element.name} has {element.health} health.')
            i += 1

    def robots_options_opponent(self):
        i = 1
        for element in self.herd.dinosaurs:
            print(f'{element.type} has {element.health} health.')
            i += 1


    def flip_coin(self):
        first_turn = random.randint(0,1)
        if first_turn == 0:
            print('Robots go first!')
            first_turn == 0
        if first_turn == 1:
            print('Dinosaurs go first!')
            first_turn == 2

    def dinosaurs_turn(self):
        self.dinosaurs_options_opponent()
        self.herd.dinosaurs[0].attack_robots()

    def robots_turn(self):
        self.robots_options_opponent()
        self.herd.dinosaurs[0].attack_robots

        if first_turn == 0:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

                    self.robots_turn

                if self.herd.dinosaurs[0].health <= 0:
                    print(f'{self.herd.dinosaurs[0].type} has been Knocked Out!')
                    self.herd.dinosaurs.remove(self.heard.dinosaurs[0])

                elif self.fleet.robots[0].health <= 0:
                    print(f'{self.fleet.robots[0].health} has been Knocked Out!')
                    self.fleet.robots.remove(self.fleet.robots[0])

                if len(self.fleet.robots) == 0:
                    self.show_winners_dinosaurs()
                    return

                elif len(self.fleet.dinosaurs) == 0:
                    self.show_winners_robots()
                    return

                    self.dinosaurs_turn

                if self.herd.dinosaurs[0].health <= 0:
                    print(f'{self.herd.dinosaurs[0].type} has been Knocked Out!')
                    self.herd.dinosaurs[0].remove(self.herd.dinosaurs[0])

                elif self.fleet.robots[0].health <= 0:
                    print(f'{self.fleet.robots[0].name} has been Knocked Out!')
                    self.fleet.robots.remove(self.fleet.robots[0])

        elif first_turn == 1:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

                 self.dinosaurs_turn()

                if self.herd.dinosaurs[0].health <=0:
                    print(f'{self.herd.dinosaurs[0].type} has been Knocked Out!')
                    self.herd.dinosaurs.remove(self.herd.dinosaurs[0])

                elif self.fleet.robots[0].health <= 0:
                    print(f'{self.fleet.robots[0].name} has been Knocked Out!')
                    self.fleet.robots.remove(self.fleet.robots[0])

                if len(self.fleet.robots) == 0:
                    self.show_winners_dinosaurs()
                    return
                elif len(self.herd.dinosaurs) == 0:
                    self.show_winners_robots()
                    return

                self.robots_turn()

                if self.herd.dinosaurs[0].health <=0:
                    print(f'{self.herd.dinosaurs[0].type} has been Knocked Out!')
                    self.herd.dinosaurs.remove(self.herd.dinosaurs[0])

                elif self.fleet.robots[0].health <= 0:
                    print(f'{self.fleet.robots[0].name} has been Knocked Out!')
                    self.fleet.robots.remove(self.fleet.robots[0])

                if len(self.fleet.robots) == 0:
                    self.show_winners_dinosaurs()
                    return

                elif len(self.herd.dinosaurs) == 0:
                    self.show_winners_robots()
                    return


    def start_battle(self):
        self.welcome_message()

