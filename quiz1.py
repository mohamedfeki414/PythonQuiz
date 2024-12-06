import random

# Liste des questions
questions = [
    {"question": "What is the largest continent by land area?",
     "options": ["Africa", "Asia", "Europe", "South America"],
     "answer": "Asia"},
    
    {"question": "Which river is the longest in the world?",
     "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
     "answer": "Nile River"},
    
    {"question": "Which country has the most natural lakes?",
     "options": ["Canada", "United States", "India", "Russia"],
     "answer": "Canada"},
    
    {"question": "Which famous artist is known for the painting 'Starry Night'?",
     "options": ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí"],
     "answer": "Vincent van Gogh"},
    
    {"question": "The Louvre Museum is located in which city?",
     "options": ["Rome", "London", "Paris", "Madrid"],
     "answer": "Paris"},
    
    {"question": "In which sport would you perform a slam dunk?",
     "options": ["Tennis", "Football", "Basketball", "Volleyball"],
     "answer": "Basketball"},
    
    {"question": "Which country has won the most FIFA World Cups?",
     "options": ["Brazil", "Germany", "Italy", "Argentina"],
     "answer": "Brazil"},
    
    {"question": "What is the top prize awarded in the Olympic Games?",
     "options": ["Bronze Medal", "Silver Medal", "Gold Medal", "Platinum Medal"],
     "answer": "Gold Medal"},
    
    {"question": "Who wrote the play 'Romeo and Juliet'?",
     "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
     "answer": "William Shakespeare"},
    
    {"question": "Who painted the Mona Lisa?",
     "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
     "answer": "Leonardo da Vinci"}
]

# Fonction principale du quiz
def quiz():
    score = 0
    print("Welcome to the Quiz! Answer the questions below:\n")
    for i in range(5):  # Pose 5 questions aléatoires
        question = random.choice(questions)
        print(f"Q{i+1}: {question['question']}")
        for idx, option in enumerate(question["options"], 1):
            print(f"{idx}. {option}")
        try:
            user_choice = int(input("Enter the number of your choice: ")) - 1
            if question["options"][user_choice] == question["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['answer']}\n")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid number.\n")
    print(f"Your final score is: {score}/5")

# Exécution du quiz
if __name__ == "__main__":
    quiz()
