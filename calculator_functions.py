operators_dict: dict = {'+': 1, '-': 1,
                        '*': 2, '/': 2,
                        '^': 3, '@': 5,
                        '$': 5, '&': 5,
                        '%': 4, '~': 6,
                        '!': 6}


def infix_to_post(input_infix: str) -> str:

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

        elif operators_dict.keys().__contains__(current_char):
            while not operators_stack and operators_stack[operators_stack.__len__()-1] != '(':  # not working
                postfix += operators_stack.pop(-1)
                postfix_index += 1
                operators_stack.append(current_char)
    while not operators_stack:
        postfix += operators_stack.pop(-1)
        postfix_index += 1
    return postfix


def postfix_to_result(input_postfix: str):  # 1[][]*- = 1-2*3
    calculate_stack: list = []
    for c in input_postfix:
        if c.isdigit():
            calculate_stack.append(c)
        if operators_dict.keys().__contains__(c):
            calculate_stack.append(c)
            post_calculate(calculate_stack)


def post_calculate(stack: list):
    result: float = 0
    operator: str = stack.pop(-1)
    operand2: int = stack.pop(-1)
    operand1: int = stack.pop(-1)
    match operator:
        case '+':
            math_add(operand1, operator, operand2)
        case '+':
        case '+':
        case '+':
        case '+':
        case '+':
        case '+':
        case '+':
        case '+':

def math_add(operand1: int, operator: str, operand2: int):


