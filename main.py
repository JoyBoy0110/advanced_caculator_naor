import pytest
import calculator_functions
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
    """

    :param inpt:
    :return:
    """
    opr_set = operators_dict.keys()
    for char in inpt:
        if char.isalpha():
            raise InputErrorException
        if not operators_dict.__contains__(char) and not char.isdigit():
            raise InputErrorException


def interface() -> str:
    equation: str = ""
    try:
        equation: str = input()
        equation.replace(" ", "")
        equation.replace("  ", "")
        check_input(equation)
    except InputErrorException as input_error:
        print(input_error)
        return ""
    return equation


def check_and_return_value(calc_str: str) -> str:  # 1+2-3 => 12+3- => 0/ 1+2*3 => 123*+/ -1*2 => (-1)2*/ ~1+5 => (-1)5+
    result: str = "0"

    return result


def calculate():
    while True:
        calc_str: str = interface()
        try:
            result: str = check_and_return_value(calc_str)
        except Exception as e:
            badui()
        else:
            escape: bool = to_end()
            if escape:
                return



def main():
    calculator_functions.infix_to_postfix2("1+2!-3+2*2-3!") # 12!+3-22*+3!-
    return


def test_mytest():
      assert check_and_return_value("1+2") == 3


if __name__ == "__main__":
    main()
