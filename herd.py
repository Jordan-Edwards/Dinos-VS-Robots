from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()


    def create_herd(self):

        robot1 = Dinosaur("Mothra", 10)
        robot2 = Dinosaur("Godzillia", 20)
        robot3 = Dinosaur("King Ghidorah", 30)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)