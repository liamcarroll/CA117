from math import sqrt
from stack_092 import Stack


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def negate(x):
    return -x


binops = {'+': add, '-': subtract, '*': multiply, '/': divide}
uniops = {'n': negate, 'r': sqrt}


def calculator(line):
    stack = Stack()
    for e in line():
        if e in binops:
            stack.push(binops[e](stack.pop(), stack.pop()))
        elif e in uniops:
            stack.push(uniops[e](stack.pop())
        else:
            stack.push(float(e))
