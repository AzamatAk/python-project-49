from random import choice, randint
from operator import add, sub, mul

description = 'What is the result of the expression?'


def make_all_games():
    min_num = 1
    max_num = 100
    op_first = randint(min_num, max_num)
    op_second = randint(min_num, max_num)
    operation, operator = choice([(add, '+'), (sub, '-'), (mul, '*')])
    correct_answer = operation(op_first, op_second)
    question = f"{op_first} {operator} {op_second}"
    return question, str(correct_answer)
