import prompt

MAX_ROUNDS = 3


def run_game(game_name):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(game_name.DESCRIPTION)
    round_num = 1
    while round_num <= MAX_ROUNDS:
        question, correct_answer = game_name.make_game()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if not (user_answer == correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {user_name}!")
            break
        print("Correct!")
        round_num += 1
    else:
        print(f"Congratulations, {user_name}!")
