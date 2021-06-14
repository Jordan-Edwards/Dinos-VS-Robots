from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()


    def create_herd(self):

        dino1 = Dinosaur("Mothra", 25)
        dino2 = Dinosaur("Godzillia", 50)
        dino3 = Dinosaur("King Ghidorah", 75)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)