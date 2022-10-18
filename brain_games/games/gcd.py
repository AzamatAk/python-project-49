from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


MIN_NUM = 1
MAX_NUM = 99


def make_game():
    number_first = randint(MIN_NUM, MAX_NUM)
    number_second = randint(MIN_NUM, MAX_NUM)
    question = f'{number_first} {number_second}'
    correct_answer = gcd(number_first, number_second)
    return question, str(correct_answer)
