import math
import calculator_exceptions
operators: dict = {'+': [1,'in'], '-': [1,'in'],
                      '*': [2,'in'], '/': [2,'in'],
                      '^': [3,'in'], '@': [5,'in'],
                      '$': [5,'in'], '&': [5,'in'],
                      '%': [4,'in'], '~': [6,'pre'],
                      'N': [10,'pre'],'!': [6,'post'],
                      '#': [6,'post']}


def infix_to_postfix(input_infix: str) -> str:
    try:
        check_valid_input(input_infix)
    except RuntimeError as Rterror:
        print(Rterror)
    else:
        operators_stack: list = []
        infix_len = input_infix.__len__()
        postfix: str = ""
        postfix_index = 0
        for current_char in input_infix:
            if current_char.isdigit():
                postfix += current_char
                postfix_index += 1

            elif current_char == '(':
                operators_stack.append(current_char)
            elif current_char == ')':
                while not operators_stack and operators_stack[operators_stack.__len__()-1] != '(':
                    postfix += operators_stack.pop(-1)
                    postfix_index += 1
                postfix += operators_stack.pop(-1)  # Discard the (

            elif operators.keys().__contains__(current_char):
                while not operators_stack and operators_stack[operators_stack.__len__()-1] != '(':  # not working
                    postfix += operators_stack.pop(-1)
                    postfix_index += 1
                    operators_stack.append(current_char)
        while not operators_stack:
            postfix += operators_stack.pop(-1)
            postfix_index += 1
        return postfix


def infix_to_postfix2(input_infix: str) -> str:
    try:
        check_valid_input(input_infix)
    except RuntimeError as run_error:
        print(run_error)
    else:
        operators_stack: list = []
        postfix: str = "" # 1+2!-3 = 12!+3-
        for current_char in input_infix:
            if current_char.isdigit():
                postfix += current_char
            else:
                if operators_stack and priority_check(operators_stack[-1], current_char):
                    operators_stack.append(current_char)
                elif not operators_stack:
                    operators_stack.append(current_char)
                elif not priority_check(operators_stack[-1], current_char):
                    while operators_stack:
                        postfix += operators_stack.pop(-1)
                    operators_stack.append(current_char)

        while operators_stack:
            postfix += operators_stack.pop(-1)
        print(postfix)
        return postfix


def priority_check(operator1: str, operator2: str):
    return (operators[operator1])[0] < (operators[operator2])[0]


def check_valid_input(input: str):
    valid = 'V'
    changable_str = str(input)
    for i in range(0,len(changable_str)):
        match changable_str:
            case '-':
                while

def postfix_to_result(input_postfix: str):  # 1[][]*- = 1-2*3
    calculate_stack: list = []
    for c in input_postfix:
        if c.isdigit():
            calculate_stack.append(c)
        if operators.keys().__contains__(c):
            calculate_stack.append(c)
            post_calculate(calculate_stack)


def post_calculate(stack: list):
    result: float = 0
    operator: str = stack.pop(-1)
    operand2: float = 0
    if (operators[operator])[0] == "mid":
        operand2 = stack.pop(-1)
    operand1: float = stack.pop(-1)
    try:
        match operator:
            # in operators
            case '+':
                result = math_add(operand1, operand2)
            case '-':
                result = math_sub(operand1, operand2)
            case '*':
                result = math_mul(operand1, operand2)
            case '/':
                result = math_div(operand1, operand2)
            case '%':
                result = math_mod(operand1, operand2)
            case '^':
                result = math_pow(operand1, operand2)
            case '$':
                result = math_max(operand1, operand2)
            case '&':
                result = math_min(operand1, operand2)
            case '@':
                result = math_avg(operand1, operand2)

            # right operators
            case '!':
                result = math_factorial(operand1)
            case '#':
                result = math_sum_of_digits(operand1)

            # left operators
            case '~':
                result = math_not(operand1)
    except Exception as exc:
        print(exc)
        return
    stack.append(result)
    print(stack)

def math_add(operand1: float, operand2: float) -> float:
    return operand1 + operand2


def math_sub(operand1: float, operand2: float) -> float:
    return operand1 - operand2


def math_mul(operand1: float, operand2: float) -> float:
    return operand1 * operand2


def math_div(operand1: float, operand2: float) -> float or None:
    if operand2 == 0:
        raise ZeroDivisionError
    return operand1 / operand2


def math_mod(operand1: float, operand2: float) -> float or None:
    if operand2 == 0:
        raise ZeroDivisionError
    return operand1 % operand2


def math_pow(operand1: float, operand2: float) -> float or None:
    if operand1 == 0 and operand2 < 0:
        raise ZeroDivisionError
    return math.pow(operand1, operand2)


def math_max(operand1: float, operand2: float) -> float:
    if operand1 > operand2:
        return operand1
    return operand2


def math_min(operand1: float, operand2: float) -> float:
    if operand1 <= operand2:
        return operand1
    return operand2


def math_avg(operand1: float, operand2: float) -> float:
    return (operand1 + operand2)/2


def math_factorial(operand1: float) -> float:
    if operand1 < 0:
        raise Exception
    if (operand1 - int(operand1)) != 0:
        raise Exception

    fact: float = 1
    if operand1 != 0:
        for i in range(int(operand1), 1, -1):
            if fact == float("inf"):
                return fact
            fact = fact * i

    return fact


def math_sum_of_digits(operand1: float) -> float:
    """

    :param operand1:
    :return:
    """
    sum_of_digits: float = 0
    while operand1 / 10 != 0:
        sum_of_digits += operand1 % 10
        operand1 = float(int(operand1/10))
    sum_of_digits += operand1 % 10
    return sum_of_digits


def math_not(operand1: float) -> float:
    return -operand1
