
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
        print("La moyenne est: " + is_moyenne())

# correction

notes = []
note = input('Note: ')
note = int(note)
while note != -1:   # while 20 >= note >= 0
    notes.append(note)
    note = input('Note: ')

print(sum(notes) / len(notes))
