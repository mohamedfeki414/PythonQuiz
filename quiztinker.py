import tkinter as tk
import random
import time

# Liste des questions et des réponses
questions = ["What is the largest continent by land area?",
             "Which river is the longest in the world?",
             "Which country has the most natural lakes?",
             "Which famous artist is known for the painting 'Starry Night'?",
             "The Louvre Museum is located in which city?",
             "In which sport would you perform a slam dunk?",
             "Which country has won the most FIFA World Cups?",
             "What is the top prize awarded in the Olympic Games?",
             "Who wrote the play 'Romeo and Juliet'?",
             "Who painted the Mona Lisa?"]

answers = [["Africa", "Asia", "Europe", "South America"],
           ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
           ["Canada", "United States", "India", "Russia"],
           ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí"],
           ["Rome", "London", "Paris", "Madrid"],
           ["Tennis", "Football", "Basketball", "Volleyball"],
           ["Brazil", "Germany", "Italy", "Argentina"],
           ["Bronze Medal", "Silver Medal", "Gold Medal", "Platinum Medal"],
           ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
           ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"]]

correct_answer = ["Asia", "Nile River", "Canada", "Vincent van Gogh", "Paris", "Basketball", "Brazil", "Gold Medal", "William Shakespeare", "Leonardo da Vinci"]

selected_indices = random.sample(range(len(questions)), len(questions))

score = 0
current_question = 0
time_limit = 20  # Temps limite pour chaque question en secondes

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Quiz avec Temps Limité")

# Fonction qui met à jour la question et les options
def afficher_question():
    global current_question, time_left
    if current_question < len(questions):
        question = questions[selected_indices[current_question]]
        options = answers[selected_indices[current_question]]
        # Mettre à jour la question et les options
        question_label.config(text=question)
        for i in range(4):
            boutons_reponse[i].config(text=options[i], command=lambda i=i: verifier_reponse(i))
        
        # Réinitialiser le temps restant et démarrer le compte à rebours
        time_left = time_limit
        countdown()
    else:
        # Afficher le score final à la fin du quiz
        question_label.config(text=f"Quiz terminé! Votre score est : {score}")
        for bouton in boutons_reponse:
            bouton.config(state=tk.DISABLED)

# Fonction qui gère le compte à rebours
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Temps restant : {time_left} secondes")
        fenetre.after(1000, countdown)  # Appel récursif toutes les secondes
    else:
        # Si le temps est écoulé, passer à la question suivante
        verifier_reponse(None)

# Fonction appelée lorsque l'on clique sur une réponse
def verifier_reponse(index):
    global score, current_question, time_left
    # Si le temps est écoulé sans réponse
    if index is None:
        index = -1  # Indique qu'il n'y a pas de réponse
        time_left = 0  # Arrêter le compte à rebours

    if index != -1:  # Si l'utilisateur a cliqué sur une option
        selected_option = answers[selected_indices[current_question]][index]
        if selected_option == correct_answer[selected_indices[current_question]]:
            score += 10
    
    current_question += 1
    afficher_question()

# Création de la zone pour afficher la question
question_label = tk.Label(fenetre, text="", font=("Arial", 14), width=50, height=2)
question_label.pack(pady=20)

# Création des boutons pour les réponses
boutons_reponse = []
for i in range(4):
    bouton = tk.Button(fenetre, text="", font=("Arial", 12), width=30, height=2)
    bouton.pack(pady=5)
    boutons_reponse.append(bouton)

# Création du label pour afficher le temps restant
timer_label = tk.Label(fenetre, text=f"Temps restant : {time_limit} secondes", font=("Arial", 12))
timer_label.pack(pady=10)

# Lancer le quiz avec la première question
afficher_question()

# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()
