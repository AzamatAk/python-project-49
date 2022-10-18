from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


def make_game():
    number = randint(MIN_NUM, MAX_NUM)
    question = str(number)
    if is_prime(number) is False:
        return question, 'no'
    else:
        return question, 'yes'
