// Liste des questions
const questions = [
    { question: "What is the largest continent by land area?", options: ["Africa", "Asia", "Europe", "South America"], answer: "Asia" },
    { question: "Which river is the longest in the world?", options: ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], answer: "Nile River" },
    { question: "Which country has the most natural lakes?", options: ["Canada", "United States", "India", "Russia"], answer: "Canada" },
    { question: "Which famous artist is known for the painting 'Starry Night'?", options: ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí"], answer: "Vincent van Gogh" },
    { question: "The Louvre Museum is located in which city?", options: ["Rome", "London", "Paris", "Madrid"], answer: "Paris" },
    { question: "In which sport would you perform a slam dunk?", options: ["Tennis", "Football", "Basketball", "Volleyball"], answer: "Basketball" },
    { question: "Which country has won the most FIFA World Cups?", options: ["Brazil", "Germany", "Italy", "Argentina"], answer: "Brazil" },
    { question: "What is the top prize awarded in the Olympic Games?", options: ["Bronze Medal", "Silver Medal", "Gold Medal", "Platinum Medal"], answer: "Gold Medal" },
    { question: "Who wrote the play 'Romeo and Juliet'?", options: ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"], answer: "William Shakespeare" },
    { question: "Who painted the Mona Lisa?", options: ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"], answer: "Leonardo da Vinci" }
];

// Variables globales
let currentQuestionIndex = 0;
let score = 0;

// Références aux éléments HTML
const quizContainer = document.getElementById("quiz-container");
const nextButton = document.getElementById("next-btn");
const resultContainer = document.getElementById("result");

// Afficher une question
function showQuestion() {
    const currentQuestion = questions[currentQuestionIndex];
    quizContainer.innerHTML = `
        <div class="question">${currentQuestion.question}</div>
        <ul class="options">
            ${currentQuestion.options.map(option => `<li><button class="option-btn">${option}</button></li>`).join('')}
        </ul>
    `;
    document.querySelectorAll(".option-btn").forEach(btn => {
        btn.addEventListener("click", selectAnswer);
    });
}

// Gérer la sélection d'une réponse
function selectAnswer(event) {
    const selectedOption = event.target.textContent;
    const correctAnswer = questions[currentQuestionIndex].answer;

    if (selectedOption === correctAnswer) {
        score++;
        event.target.style.backgroundColor = "green";
    } else {
        event.target.style.backgroundColor = "red";
    }

    // Désactiver tous les boutons après une sélection
    document.querySelectorAll(".option-btn").forEach(btn => btn.disabled = true);
}

// Passer à la question suivante
nextButton.addEventListener("click", () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        showResult();
    }
});

// Afficher le résultat final
function showResult() {
    quizContainer.innerHTML = "";
    nextButton.style.display = "none";
    resultContainer.textContent = `You scored ${score} out of ${questions.length}`;
}

// Lancer le quiz
showQuestion();
