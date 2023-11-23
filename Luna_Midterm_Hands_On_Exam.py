
import random


def generate_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

    operation = random.choice(['+', '-', '*', '/'])

    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    else:
        num1, remainder = divmod(num1, num2)
        answer = num1

    question = f"What is {num1} {operation} {num2}? "
    return question, answer


def main():
    print("Welcome! Let's practice!")
    score = 0
    num_questions = 5

    for _ in range(num_questions):
        question, correct_answer = generate_question()
        user_answer = input(question)

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid Input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong!The correct answer is {correct_answer}\n")

    print(f"Quiz completed! Your score is {score}/{num_questions}")


if __name__ == "__main__":
    main()
