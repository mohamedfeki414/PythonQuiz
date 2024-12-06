import tkinter as tk

# Fonction appelée lorsqu'un bouton est cliqué
def bouton_clique(num_bouton):
    texte.config(text=f'Bouton {num_bouton} cliqué en premier!')

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Bouton Cliqué en Premier")

# Création des boutons
bouton1 = tk.Button(fenetre, text="Bouton 1", command=lambda: bouton_clique(1))
bouton1.pack(pady=20)

bouton2 = tk.Button(fenetre, text="Bouton 2", command=lambda: bouton_clique(2))
bouton2.pack(pady=20)

# Création du texte pour afficher le résultat
texte = tk.Label(fenetre, text="")
texte.pack()

# Lancement de la boucle principale
fenetre.mainloop()
