error_list = []
operators_dict: dict = {'+': 1, '-': 1,
                        '*': 2, '/': 2,
                        '^': 3, '@': 5,
                        '$': 5, '&': 5,
                        '%': 4, '~': 6,
                        '!': 6}


class InputErrorException(RuntimeError):
    def __init__(self):
        pass

    def __str__(self):
        return "the input you have entered is an invalid input"


def check_input(inpt: str):
    opr_set = operators_dict.keys()
    for char in inpt:
        if char.isalpha():
            raise InputErrorException
        if char.isspace():
            raise InputErrorException
        if not operators_dict.__contains__(char) and not char.isdigit():
            raise InputErrorException


def interface() -> str:
    equation: str = ""
    try:
        equation: str = input()
        check_input(equation)
    except InputErrorException as input_error:
        print(input_error)
        return ""
    return equation


def calculate():
    while True:
        calc_str = interface()
        check_&_ret_value(calc_str)
        if not error_list:
            badui()
        escape: bool = end(escape)
        if escape:
            return



def main():
    check_input("")
    return


if __name__ == "__main__":
    main()
