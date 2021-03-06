import prompt


ROUNDS_COUNT = 3


def run(generate_round, description):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(F'Hello, {user_name}!')
    print(description)
    for _ in range(ROUNDS_COUNT):
        question, answer = generate_round()
        print(F'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if not user_answer == answer:
            print(
                F'"{user_answer}" is wrong answer ;(. '
                F'Correct answer was "{answer}".\n'
                F'Let\'s try again, {user_name}!')
            return
        print('Correct!')
    print(F'Congratulations, {user_name}!')
