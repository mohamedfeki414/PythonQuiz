import random
import time

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
indice = 0

# Ouverture du fichier HTML pour écrire les résultats
with open("quiz_results.html", "w") as f:
    # Ajouter l'entête HTML
    f.write("<html><head><title>Quiz Results</title></head><body>")
    f.write("<h1>Quiz Results</h1>")
    f.write("<table border='1'><tr><th>Question</th><th>Your Answer</th><th>Correct Answer</th><th>Score</th></tr>")
    
    for i in selected_indices:
        indice += 1
        f.write(f"<tr><td>Question {indice}: {questions[i]}</td>")
        f.write(f"<td>{', '.join(answers[i])}</td>")
        start_time = time.time()
        answer = None
        while True:
            if time.time() - start_time > 10:
                f.write("<td>Time's up!</td><td>0</td></tr>")
                break
            answer = input(f"Question {indice}: {questions[i]}\nOptions: {answers[i]}\nVotre réponse est (1-4): ")
            if answer.isdigit() and 1 <= int(answer) <= 4:
                answer = int(answer)
                break
            else:
                print("Invalid input. Please choose a valid number between 1 and 4.")

        if answer is None or time.time() - start_time > 10:
            f.write("<td>Time's up!</td><td>0</td></tr>")
        else:
            if answers[i][answer - 1] == correct_answer[i]:
                f.write(f"<td>{answers[i][answer - 1]}</td><td>10</td></tr>")
                score += 10
            else:
                f.write(f"<td>{answers[i][answer - 1]}</td><td>0</td></tr>")
                f.write(f"<p>Nice try! The correct answer is: {correct_answer[i]}</p>")
    
    # Ajouter le score total à la fin du fichier HTML
    f.write(f"<h2>Your total score is: {score}</h2>")
    f.write("</table></body></html>")

print(f"Your results have been saved in 'quiz_results.html'.")

