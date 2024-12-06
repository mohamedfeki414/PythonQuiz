import tkinter as tk
import random
import time

# Questions et réponses
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

# Mélanger les indices pour rendre les questions aléatoires
selected_indices = random.sample(range(len(questions)), len(questions))

# Variables pour le score et l'indice de question
score = 0
indice = 0

# Fonction pour afficher la question suivante
def next_question():
    global indice
    if indice < len(selected_indices):
        # Afficher la question actuelle
        question_label.config(text=questions[selected_indices[indice]])
        options = answers[selected_indices[indice]]
        for i in range(4):
            buttons[i].config(text=options[i])

        # Réinitialiser le chronomètre et commencer la nouvelle question
        start_time = time.time()
        time_left_label.config(text="Time left: 10s")
        # Attendre que l'utilisateur réponde ou que le temps soit écoulé
        root.after(1000, check_time_left, start_time)

def check_time_left(start_time):
    elapsed_time = time.time() - start_time
    time_left = max(0, 10 - int(elapsed_time))  # Calcul du temps restant
    time_left_label.config(text=f"Time left: {time_left}s")
    
    if elapsed_time > 10:
        time_left_label.config(text="Time's up!")
        check_answer(None)  # Si le temps est écoulé, vérifier la réponse (aucune réponse)

    else:
        root.after(1000, check_time_left, start_time)

def check_answer(answer):
    global score, indice
    if answer is None:
        # Temps écoulé sans réponse
        answer_label.config(text=f"Time's up! Correct answer: {correct_answer[selected_indices[indice]]}")
    else:
        if answers[selected_indices[indice]][answer] == correct_answer[selected_indices[indice]]:
            score += 10
            answer_label.config(text="Correct answer!")
        else:
            answer_label.config(text=f"Incorrect! Correct answer: {correct_answer[selected_indices[indice]]}")
    
    # Attendre un peu avant de passer à la prochaine question
    if indice + 1 < len(selected_indices):
        next_button.config(state="normal")
    else:
        finish_quiz()

def select_answer(answer):
    next_button.config(state="normal")
    check_answer(answer)

def finish_quiz():
    question_label.config(text="Quiz Finished!")
    answer_label.config(text=f"Your final score is: {score}")
    for btn in buttons:
        btn.config(state="disabled")

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Quiz Game")

# Labels pour afficher les questions et le temps restant
question_label = tk.Label(root, text="", font=("Arial", 14), width=50, height=4)
question_label.pack(pady=20)

time_left_label = tk.Label(root, text="Time left: 10s", font=("Arial", 12))
time_left_label.pack(pady=10)

answer_label = tk.Label(root, text="", font=("Arial", 12))
answer_label.pack(pady=10)

# Boutons pour les réponses
buttons = [tk.Button(root, text="", width=50, height=2, command=lambda i=i: select_answer(i)) for i in range(4)]
for btn in buttons:
    btn.pack(pady=5)

# Bouton suivant pour la question suivante
next_button = tk.Button(root, text="Next", state="disabled", command=lambda: [next_question(), next_button.config(state="disabled")])
next_button.pack(pady=20)

# Lancer le quiz
next_question()

# Lancer la boucle principale de Tkinter
root.mainloop()
