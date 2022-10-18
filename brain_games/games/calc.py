from random import choice, randint
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'

MIN_NUM = 1
MAX_NUM = 100


def make_game():
    op_first = randint(MIN_NUM, MAX_NUM)
    op_second = randint(MIN_NUM, MAX_NUM)
    operation, operator = choice([(add, '+'), (sub, '-'), (mul, '*')])
    correct_answer = operation(op_first, op_second)
    question = f"{op_first} {operator} {op_second}"
    return question, str(correct_answer)
