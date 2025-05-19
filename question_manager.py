import random

def generate_question(level):
    num1 = random.randint(1, 10 * level)
    num2 = random.randint(1, 10 * level)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    else:
        correct_answer = num1 + num2
    question = f"{num1} {operation} {num2}"
    return question, correct_answer

def generate_answers(correct_answer, num_choices=3):
    answers = [correct_answer]
    while len(answers) < num_choices:
        fake_answer = random.randint(correct_answer - 10, correct_answer + 10)
        if fake_answer != correct_answer and fake_answer not in answers:
            answers.append(fake_answer)
    random.shuffle(answers)
    return answers
