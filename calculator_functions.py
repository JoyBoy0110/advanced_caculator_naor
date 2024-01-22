import my_math
from calculator_exceptions import InvalidInputException
from validation_functions import check_valid_input
from validation_functions import check_valid_input1
from validation_functions import priority_check
from validation_functions import decimal_point_check
from my_math import operators_dictionary


def infix_to_postfix(input_infix: str) -> list:
    try:
        infix_list: list = str_to_list(input_infix)
        infix_list = reduce_minuses(infix_list)
        check_valid_input1(infix_list)
    except Exception:
        raise
    else:
        operators_dictionary_stack: list = []
        postfix_list: list = []
        for i in range(0, len(infix_list)):
            if i == 12:
                pass
            if type(infix_list[i]) is float:
                postfix_list.append(infix_list[i])
            else:
                if (operators_dictionary_stack and (priority_check(operators_dictionary_stack[-1], infix_list[i])
                                                    or operators_dictionary_stack[-1] == '(') and infix_list[i] != ')'):
                    operators_dictionary_stack.append(infix_list[i])
                elif not operators_dictionary_stack:
                    operators_dictionary_stack.append(infix_list[i])
                elif not priority_check(operators_dictionary_stack[-1], infix_list[i]) or infix_list[
                    i] == ')':  # *(+    )
                    while operators_dictionary_stack and (
                            not priority_check(operators_dictionary_stack[-1], infix_list[i])
                            or infix_list[i] == ')') and operators_dictionary_stack[-1] != '(':
                        if operators_dictionary_stack[-1] != ')' and operators_dictionary_stack[-1] != '(':
                            postfix_list.append(operators_dictionary_stack.pop(-1))
                    if not operators_dictionary_stack:
                        if infix_list[i] != ')':
                            operators_dictionary_stack.append(infix_list[i])
                    else:
                        if infix_list[i] == ')':
                            operators_dictionary_stack.pop(-1)
                        if infix_list[i] != ')':
                            operators_dictionary_stack.append(infix_list[i])

        while operators_dictionary_stack:
            postfix_list.append(operators_dictionary_stack.pop(-1))
        return postfix_list


def str_to_list(string: str) -> list:
    i: int = 0
    result_list: list = []
    while i < len(string):
        if operators_dictionary.keys().__contains__(string[i]):
            result_list.append(string[i])
        elif string[i].isdigit() or string[i] == '.':
            if string[i] == '.':
                decimal_point_check(string, i)
            j: int = 0
            post_point: float = 0.1
            num: float = 0.0
            point_counter: int = 0
            while j + i < len(string) and (string[j + i].isdigit() or string[j + i] == '.'):
                if string[j + i] == '.':
                    if j + i != 0 and not string[j + i - 1].isdigit() and not string[j + i + 1].isdigit():
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


def reduce_minuses(infix_list: list) -> list:
    index: int = 0
    while (index < len(infix_list) and infix_list[index] == '-' and infix_list[index + 1] == '-'
           and (type(infix_list[index + 2]) is float or infix_list[index + 2] == '-' or infix_list[
                index + 2] == '(')):
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
            if (index - 1 >= 0 and type(infix_list[index - 1]) is not float and
                    (operators_dictionary[infix_list[index - 1]])[
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
                and (index == 0 or type(infix_list[index - 1]) is not float and
                     (operators_dictionary[infix_list[index - 1]])[
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
        elif operators_dictionary.keys().__contains__(c):
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
    if (operators_dictionary[operator])[1] == "in":
        operand2 = stack.pop(-1)
    operand1: float = stack.pop(-1)
    try:
        match operator:
            # in operators_dictionary
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

            # right operators_dictionary
            case '!':
                result = my_math.factorial(operand1)
            case '#':
                result = my_math.sum_of_digits(operand1)

            # left operators_dictionary
            case '~':
                result = my_math.arithmetic_not(operand1)
            case 'N':
                result = my_math.arithmetic_not(operand1)
            case 'UM':
                result = my_math.arithmetic_not(operand1)
    except Exception:
        raise
    result = round(result, 10)
    stack.append(result)
