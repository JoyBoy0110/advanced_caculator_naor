import pytest
import calculator_functions
from calculator_exceptions import InvalidInputException

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
            pass
            # badui()
        else:
            escape: bool = False
            if escape:
                return


def main():
    _input = "(-10)!"
    _output: float
    try:
        _output = cal(_input)
    except ArithmeticError as e:
        print(e)
    except InvalidInputException as e:
        print(e)
    else:
        print(_output)


def cal(_input: str) -> float:
    input_list: list = []
    print(calculator_functions.str_to_list(_input))
    try:
        input_list = calculator_functions.infix_to_postfix(_input)
    except Exception as exc:
        raise
    else:
        try:
            result = calculator_functions.postfix_to_result(input_list)
        except Exception as exc:
            raise
        else:
            return result


@pytest.mark.parametrize("_input, result", [
    ("1+2", 3.0),
    ("((15 * ~2) / (3^2+1)) + 4! % 135#", 3.0),
    ("(2^3 * ~5) + (10 / 32#) - 7", -45.0)
])
def test_mytest(_input, result):
    assert cal(_input) == result


if __name__ == "__main__":
    main()
