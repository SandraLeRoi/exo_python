import random


class Dice:
    def __init__(self, nb_faces=6):
        self.__nb_faces = nb_faces
        self.value = random.randint(1, self.__nb_faces)

    def reroll(self):
        self.value = random.randint(1, self.__nb_faces)
        self.display()

    def display(self):
        print("Valeur: %s" % self.value)

    def nb_faces(self):
        return self.__nb_faces


class DiceHundred(Dice):
    def __init__(self):
        super().__init__(100)


# dice = Dice()
# dice.display()
# dice.reroll()
# dice.reroll()
# dice.reroll()
# dice.reroll()

class Game:
    def __init__(self):
        self.dices = []
        self.dices.append(Dice())


my_game = Game()