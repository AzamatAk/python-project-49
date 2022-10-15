from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_all_games():
    min_num = 1
    max_num = 99
    num = randint(min_num, max_num)
    question = str(num)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
