import random

# Define questions
questions = [
    {
        "question": "What is the capital of France?",
        "type": "multiple_choice",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "type": "multiple_choice",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "type": "fill_in_the_blank",
        "answer": "H2O"
    },
    {
        "question": "In which year did the Titanic sink?",
        "type": "multiple_choice",
        "options": ["A) 1912", "B) 1913", "C) 1914", "D) 1915"],
        "answer": "A"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "type": "fill_in_the_blank",
        "answer": "Harper Lee"
    }
]

# Function to ask multiple choice questions
def ask_multiple_choice(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Enter your answer (A, B, C, D): ").strip().upper()
    return answer == question["answer"]

# Function to ask fill-in-the-blank questions
def ask_fill_in_the_blank(question):
    print(question["question"])
    answer = input("Enter your answer: ").strip()
    return answer.lower() == question["answer"].lower()

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + "="*50)
        if question["type"] == "multiple_choice":
            if ask_multiple_choice(question):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {question['answer']}.")
        elif question["type"] == "fill_in_the_blank":
            if ask_fill_in_the_blank(question):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {question['answer']}.")
        print("="*50)
    print(f"\nYour final score is: {score}/{len(questions)}")

# Main function to start the quiz
def main():
    print("Welcome to the Quiz Game!")
    random.shuffle(questions)  # Shuffle questions for variety
    run_quiz(questions)

if __name__ == "__main__":
    main()
