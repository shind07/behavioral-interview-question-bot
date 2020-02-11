import random

question_file_path = "questions.txt"


def load_questions():
    """Load a txt file of interview questions into a list"""
    with open(question_file_path, "r") as f:
        return [question for question in f.readlines()]


def main():
    """Ask a random question until the user terminates the loop"""
    questions = load_questions()
    
    n = 1
    while True:
        question = random.choice(questions)
        answer = input(f"{n}: {question}")
        n += 1


if __name__ == "__main__":
    main()