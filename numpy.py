import numpy
import random

def is_moyenne():
    moyenne = sum(tableau_notes)/len(tableau_notes)
    print(moyenne)
    return str(moyenne)

notes = input("Entrez une note pour continuer ou -1 pour arreter: ")
tableau_notes = []

while 0<=int(notes)<=20:
    print(int(notes))
    tableau_notes.append(int(notes))
    notes = input("Entrez une note pour continuer ou -1 pour arreter: ")
    if int(notes) == -1:
        # print(is_moyenne())
        print(numpy.average(tableau_notes))



print(random.randint(0, 100))
