import random


class De:
    def __init__(self, face=6):
        self.faces = face
        self.__valeur = random.randint(1, int(face))

    def lancer_de(self):
        self.__valeur = random.randint(1, int(self.faces))
        print("Valeur du lancer: " + str(self.__valeur))

    def display_face(self):
        print("Valeur: " + str(self.__valeur))


nb_face = input("Combien de face voulez-vous pour votre dé ? : ")
de = De(int(nb_face))
de.display_face()
lancer = input("Voulez-vous relancer le dé (y) ? ")
while lancer == "y":
    de.lancer_de()
    lancer = input("Voulez-vous relancer le dé (y) ? ")

