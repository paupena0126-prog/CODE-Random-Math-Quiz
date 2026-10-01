import random


def main():
    # Randomly choose an operation from this tuple for each question
    math_operations = ("add", "subtract", "multiply")

    # Your code begins here
number of questions = random.randint(1, 5)
correct_answers = 0

print("Welcome to the Random Math Quiz!")
print(f"You will be asked {number_of_questions} questions")

for question in range(number_of_questions):
    operation = random.choice(math_operations)
    if operation == "multiply":
        number1 = random.randint(1, 12)
        number2 = random.randint(1, 12)
    else:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)

if operation == "add":
    correct_answer = number1 + number2
    symbol = "+"
elif operation == "subtract":
    correct_answer = number1 - number2
    symbol = "-"
else:
    correct_answer = number1 * number2
    symbol = "*"

user_answer = int(input(f"\nWhat is {number 1} {symbol} {number2}? "))

if user_answer == correct_answer:
    print("Correct!")
    correct_answers += 1
else:
    print(f"Incorrect. The answer was {correct_answer}")

print(f"\nYou got {correct_answers}/{number_of_questions} correct.")


if __name__ == "__main__":
    main()
