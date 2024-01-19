import math
import calculator_exceptions

operators: dict = {'+': [1, 'in'], '-': [1, 'in'],
                   '*': [2, 'in'], '/': [2, 'in'],
                   '^': [3, 'in'], '@': [5, 'in'],
                   '$': [5, 'in'], '&': [5, 'in'],
                   '%': [4, 'in'], '~': [6, 'pre'],
                   'N': [10, 'pre'], '!': [6, 'post'],
                   '#': [6, 'post'], '(': [10, 'pre'],
                   ')': [6, 'post'], }


def infix_to_postfix(input_infix: str) -> list:
    try:
        pass
        #  check_valid_input(input_infix)
    except RuntimeError as run_error:
        print(run_error)
    else:
        infix_list: list = str_to_list(input_infix)
        operators_stack: list = []
        postfix_list: list = []  # 1+2!-3 = 12!+3-
        for i in range(0, len(infix_list)):
            if type(infix_list[i]) is float:
                postfix_list.append(infix_list[i])
            else:
                if operators_stack and priority_check(operators_stack[-1], infix_list[i]):
                    operators_stack.append(infix_list[i])
                elif not operators_stack:
                    operators_stack.append(infix_list[i])
                elif not priority_check(operators_stack[-1], infix_list[i]):
                    while operators_stack and not priority_check(operators_stack[-1], infix_list[i]):
                        postfix_list.append(operators_stack.pop(-1))
                    operators_stack.append(infix_list[i])

        while operators_stack:
            postfix_list.append(operators_stack.pop(-1))
        return postfix_list


def priority_check(operator1: str, operator2: str):
    return (operators[operator1])[0] < (operators[operator2])[0]


def str_to_list(string: str) -> list:
    i: int = 0
    result_list: list = []
    while i < len(string):
        if operators.keys().__contains__(string[i]):
            result_list.append(string[i])
        if string[i].isdigit():
            j: int = 0
            num: float = 0
            while j+i < len(string) and string[j + i].isdigit():
                num = num * 10 + float(string[j + i])
                j += 1
            i += j - 1
            result_list.append(num)
        i += 1
    return result_list


def check_valid_input(invalid_input: str):  # ----- => (delete: -, -, -, -)- => N, ~- => '', ---
    valid = 'V'
    changable_str = str(invalid_input)
    for i in range(0, len(changable_str)):
        if changable_str[i] == '~' and i != 0:
            if changable_str[i - 1].isdigit() and changable_str[i - 1] == '~':  # exception: 6~, ~~,
                raise Exception


def postfix_to_result(postfix_list: list) -> float:
    calculate_stack: list = []
    for c in postfix_list:
        if type(c) is float:
            calculate_stack.append(c)
        elif operators.keys().__contains__(c):
            calculate_stack.append(c)
            post_calculate(calculate_stack)
            print(calculate_stack)
    return calculate_stack.pop(-1)


def post_calculate(stack: list):
    result: float = 0
    operator: str = stack.pop(-1)
    operand2: float = 0
    if (operators[operator])[1] == "in":
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
    return (operand1 + operand2) / 2


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
        operand1 = float(int(operand1 / 10))
    sum_of_digits += operand1 % 10
    return sum_of_digits


def math_not(operand1: float) -> float:
    return -operand1
