from calculator_exceptions import UndefinedException
from math import pow

operators_dictionary: dict = {'+': [1, 'in'], '-': [1, 'in'],
                              '*': [2, 'in'], '/': [2, 'in'],
                              '^': [3, 'in'], '@': [5, 'in'],
                              '$': [5, 'in'], '&': [5, 'in'],
                              '%': [4, 'in'], '~': [6, 'pre'],
                              'N': [6.5, 'pre'], 'UM': [3.5, 'pre'],
                              '!': [6, 'post'], '#': [6, 'post'],
                              '(': [10, 'pre'], ')': [10, 'post'], }

def add(operand1: float, operand2: float) -> float:
    return operand1 + operand2


def sub(operand1: float, operand2: float) -> float:
    return operand1 - operand2


def mul(operand1: float, operand2: float) -> float:
    return operand1 * operand2


def div(operand1: float, operand2: float) -> float or None:
    if operand2 == 0:
        raise ZeroDivisionError("can't divide by zero")
    if operand2 == 0 and operand1 == 0:
        raise UndefinedException("undefined")
    return operand1 / operand2


def mod(operand1: float, operand2: float) -> float or None:
    if operand2 == 0 and operand1 != 0:
        raise ZeroDivisionError("can't divide by zero")
    if operand2 == 0 and operand1 == 0:
        raise UndefinedException("undefined")
    return operand1 % operand2


def my_pow(operand1: float, operand2: float) -> float or None:
    if operand1 == 0 and operand2 < 0:
        raise ZeroDivisionError("can't divide by 0")
    if operand1 == 0 and operand2 == 0:
        raise UndefinedException("undefined")
    return pow(operand1, operand2)


def max(operand1: float, operand2: float) -> float:
    if operand1 > operand2:
        return operand1
    return operand2


def min(operand1: float, operand2: float) -> float:
    if operand1 <= operand2:
        return operand1
    return operand2


def avg(operand1: float, operand2: float) -> float:
    return (operand1 + operand2) / 2


def factorial(operand1: float) -> float:
    if operand1 < 0:
        raise ArithmeticError("can't factor a negative number")
    if (operand1 - int(operand1)) != 0:
        raise ArithmeticError("can't factor a decimal number")

    fact: float = 1.0
    if operand1 != 0:
        for i in range(int(operand1), 1, -1):
            if fact == float("inf"):
                return fact
            fact = fact * float(i)

    return fact


def sum_of_digits(operand1: float) -> float:
    num_str = str(operand1)
    sum: float = 0.0
    index: int = 0
    while index < len(num_str) and num_str[index] != 'e':
        if num_str[index] != '.':
            sum = sum + float(num_str[index])
        index += 1
    return sum


def arithmetic_not(operand1: float) -> float:
    return -operand1
