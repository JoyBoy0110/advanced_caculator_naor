import my_math
from calculator_exceptions import InvalidInputException

operators: dict = {'+': [1, 'in'], '-': [1, 'in'],
                   '*': [2, 'in'], '/': [2, 'in'],
                   '^': [3, 'in'], '@': [5, 'in'],
                   '$': [5, 'in'], '&': [5, 'in'],
                   '%': [4, 'in'], '~': [6, 'pre'],
                   'N': [6.5, 'pre'], 'UM': [3.5, 'pre'],
                   '!': [6, 'post'], '#': [6, 'post'],
                   '(': [10, 'pre'], ')': [10, 'post'], }


def infix_to_postfix(input_infix: str) -> list:
    try:
        infix_list: list = str_to_list(input_infix)
        infix_list = reduce_minuses(infix_list)
        check_valid_input(infix_list)
    except Exception:
        raise
    else:
        operators_stack: list = []
        postfix_list: list = []
        for i in range(0, len(infix_list)):
            if i == 12:
                pass
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
        elif string[i].isdigit() or string[i] == '.':
            j: int = 0
            post_point: float = 0.1
            num: float = 0.0
            point_counter: int = 0
            while j + i < len(string) and (string[j + i].isdigit() or string[j + i] == '.'):
                if string[j + i] == '.':
                    if j + i != 0 and not string[j + i-1].isdigit() and not string[j + i+1].isdigit():
                        raise InvalidInputException("can't enter '.' alone")
                    point_counter += 1
                if point_counter == 0:
                    num = num * 10 + float(string[j + i])
                elif string[j + i].isdigit():
                    num = num + float(string[j + i]) * post_point
                j += 1
            num = round(num, 10)
            if num == int(num) and point_counter != 0:
                num += 0.0
            i += j - 1
            result_list.append(num)
        i += 1
    return result_list


def check_valid_input(invalid_input: list):  # ~- => '', ---
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
                if index == 0 or infix_list[index - 1] == '(':
                    infix_list[index] = 'UM'
                else:
                    infix_list.pop(index)
                    num: float = float(infix_list[index])
                    infix_list[index] = 0 - num
        index += 1
    for index in range(0, len(infix_list)):
        if (infix_list[index] == '-' and (infix_list[index + 1] == '(' or type(infix_list[index + 1]) is float)
                and (index == 0 or type(infix_list[index - 1]) is not float and (operators[infix_list[index - 1]])[
                    1] != 'post')):
            if index == 0 or infix_list[index - 1] == '(':
                infix_list[index] = 'UM'
            else:
                infix_list[index] = 'N'
    print(infix_list)
    return infix_list


def postfix_to_result(postfix_list: list) -> float:
    calculate_stack: list = []
    for c in postfix_list:
        if type(c) is float:
            calculate_stack.append(c)
            print(calculate_stack)
        elif operators.keys().__contains__(c):
            calculate_stack.append(c)
            print(calculate_stack)
            try:
                post_calculate(calculate_stack)
            except Exception:
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
                result = my_math.add(operand1, operand2)
            case '-':
                result = my_math.sub(operand1, operand2)
            case '*':
                result = my_math.mul(operand1, operand2)
            case '/':
                result = my_math.div(operand1, operand2)
            case '%':
                result = my_math.mod(operand1, operand2)
            case '^':
                result = my_math.my_pow(operand1, operand2)
            case '$':
                result = my_math.max(operand1, operand2)
            case '&':
                result = my_math.min(operand1, operand2)
            case '@':
                result = my_math.avg(operand1, operand2)

            # right operators
            case '!':
                result = my_math.factorial(operand1)
            case '#':
                result = my_math.sum_of_digits(operand1)

            # left operators
            case '~':
                result = my_math.arithmetic_not(operand1)
            case 'N':
                result = my_math.arithmetic_not(operand1)
            case 'UM':
                result = my_math.arithmetic_not(operand1)
    except Exception:
        raise
    result = round(result, 100)
    stack.append(result)
