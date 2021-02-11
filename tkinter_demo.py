import tkinter
from tkinter import ttk


root = tkinter.Tk()  # création de la fenêtre
root.geometry("1000x500")

frame = tkinter.Frame(root, padx=20, pady=20, bg="#808080")
frame2 = tkinter.Frame(root, padx=20, pady=20, bg="#D3D3D3")

frame.grid()
frame2.grid()

button = tkinter.Button(frame, text="Cliquez ici")
button2 = ttk.Button(frame2, text="Ou cliquez ici")
button.grid()
button2.grid()


# root.update()  # met  à jour la fenêtre et l'affiche
root.mainloop()  # crée une boucle infini qui va répéter et mettre à jour la fenetre
