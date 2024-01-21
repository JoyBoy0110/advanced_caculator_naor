import math
from calculator_exceptions import InvalidInputException
from calculator_exceptions import UndefinedException


operators: dict = {'+': [1, 'in'], '-': [1, 'in'],
                   '*': [2, 'in'], '/': [2, 'in'],
                   '^': [3, 'in'], '@': [5, 'in'],
                   '$': [5, 'in'], '&': [5, 'in'],
                   '%': [4, 'in'], '~': [6, 'pre'],
                   'N': [6.5, 'pre'],
                   '!': [6, 'post'], '#': [6, 'post'],
                   '(': [10, 'pre'], ')': [10, 'post'], }


def infix_to_postfix(input_infix: str) -> list:
    try:
        infix_list: list = str_to_list(input_infix)
        infix_list = reduce_minuses(infix_list)
        check_valid_input(infix_list)
    except RuntimeError as run_error:
        raise
    else:
        operators_stack: list = []
        postfix_list: list = []
        for i in range(0, len(infix_list)):
            if type(infix_list[i]) is float:
                postfix_list.append(infix_list[i])
            else:
                if (operators_stack and (priority_check(operators_stack[-1], infix_list[i])
                                         or operators_stack[-1] == '(') and infix_list[i] != ')'):
                    operators_stack.append(infix_list[i])
                elif not operators_stack:
                    operators_stack.append(infix_list[i])
                elif not priority_check(operators_stack[-1], infix_list[i]) or infix_list[i] == ')':  # *(+    )
                    while operators_stack and (not priority_check(operators_stack[-1], infix_list[i])
                                               or infix_list[i] == ')') and operators_stack[-1] != '(':
                        if operators_stack[-1] != ')' and operators_stack[-1] != '(':
                            postfix_list.append(operators_stack.pop(-1))
                    if not operators_stack:
                        if infix_list[i] != ')':
                            operators_stack.append(infix_list[i])
                    else:
                        if infix_list[i] == ')':
                            operators_stack.pop(-1)
                        if infix_list[i] != ')':
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
            while j + i < len(string) and string[j + i].isdigit():
                num = num * 10 + float(string[j + i])
                j += 1
            i += j - 1
            result_list.append(num)
        i += 1
    return result_list


def check_valid_input(invalid_input: list):  # ~- => '', ---
    valid = 'V'
    left_bracket_counter: int = 0
    right_bracket_counter: int = 0
    changeable_list = list(invalid_input)
    for i in range(0, len(changeable_list)):
        if changeable_list[i] == '~' and i != 0:  # exception: 6~, ~~, )~, 1--~2
            if ((type(changeable_list[i + 1]) is not float or changeable_list[i - 1] == '-')
                    and (type(changeable_list[i - 1].isdigit()) is float
                         or changeable_list[i - 1] == '~' or changeable_list[i - 1] == ')')):
                raise
        if changeable_list[i] == '(':
            left_bracket_counter += 1
        if changeable_list[i] == ')':
            right_bracket_counter += 1
    #
    if left_bracket_counter != right_bracket_counter:
        error_char: str = ''
        if left_bracket_counter > right_bracket_counter:
            error_char = '('
        else:
            error_char = ')'
        raise InvalidInputException(str("invalid input: there is an extra " + error_char))


def reduce_minuses(infix_list: list) -> list:
    index: int = 0
    while (infix_list[index] == '-' and infix_list[index + 1] == '-'
           and (type(infix_list[index + 2]) is float or infix_list[index + 2] == '-' or infix_list[
                index + 2] == '(') and index < len(infix_list)):
        infix_list.pop(index)
        infix_list.pop(index)
    while index < len(infix_list):
        if infix_list[index] == '-' and infix_list[index + 1] == '-':
            if index - 1 >= 0 and type(infix_list[index - 1]) is not float:
                infix_list.pop(index)
                infix_list.pop(index)
            else:
                index += 1

        else:
            index += 1

    index: int = 0
    while index < len(infix_list):
        if infix_list[index] == '-':
            if (index - 1 >= 0 and type(infix_list[index - 1]) is not float and (operators[infix_list[index - 1]])[
                1] != 'post' and infix_list[index + 1] != '('
                    and infix_list[index - 1] != ')'):
                infix_list.pop(index)
                num: float = float(infix_list[index])
                infix_list[index] = 0 - num
        index += 1
    for index in range(0, len(infix_list)):
        if (infix_list[index] == '-' and (infix_list[index + 1] == '(' or type(infix_list[index + 1]) is float)
                and (index == 0 or type(infix_list[index - 1]) is not float and (operators[infix_list[index - 1]])[
                    1] != 'post')):
            infix_list[index] = 'N'
    print(infix_list)
    return infix_list


def postfix_to_result(postfix_list: list) -> float:
    calculate_stack: list = []
    for c in postfix_list:
        if type(c) is float:
            calculate_stack.append(c)
        elif operators.keys().__contains__(c):
            calculate_stack.append(c)
            print(calculate_stack)
            try:
                post_calculate(calculate_stack)
            except Exception as exc:
                raise
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
            case 'N':
                result = math_not(operand1)
    except Exception as exc:
        raise
    stack.append(result)


def math_add(operand1: float, operand2: float) -> float:
    return operand1 + operand2


def math_sub(operand1: float, operand2: float) -> float:
    return operand1 - operand2


def math_mul(operand1: float, operand2: float) -> float:
    return operand1 * operand2


def math_div(operand1: float, operand2: float) -> float or None:
    if operand2 == 0:
        raise ZeroDivisionError("can't divide by zero")
    if operand2 == 0 and operand1 == 0:
        raise UndefinedException("undefined")
    return operand1 / operand2


def math_mod(operand1: float, operand2: float) -> float or None:
    if operand2 == 0 and operand1 != 0:
        raise ZeroDivisionError("can't divide by zero")
    if operand2 == 0 and operand1 == 0:
        raise UndefinedException("undefined")
    return operand1 % operand2


def math_pow(operand1: float, operand2: float) -> float or None:
    if operand1 == 0 and operand2 < 0:
        raise ZeroDivisionError("can't divide by 0")
    if operand1 == 0 and operand2 == 0:
        raise UndefinedException("undefined")
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
            fact = fact * float(i)

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
