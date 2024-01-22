import pytest
import calculator_functions
from calculator_exceptions import InvalidInputException

error_list = []
allowed_chars: list = ['+', '-', '*', '/', '^', '@', '$', '&', '%', '~', '!', '.', '#', '(', ')']


def check_input(inpt: str):
    """

    :param inpt:
    :return:
    """
    for char in inpt:
        if char.isalpha():
            raise InvalidInputException("the input you have entered is an invalid input")
        if not allowed_chars.__contains__(char) and not char.isdigit():
            raise InvalidInputException("the input you have entered is an invalid input")


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


def main():  # ((((~-3!!^~-3!)#/5) ^ 100)#!#)
    _input = ""  # ((((3!!^3!)#/5) ^ 100)#!#)
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
    try:
        _input = _input.replace(" ", "")
        _input = _input.replace("  ", "")
        check_input(_input)
    except Exception:
        raise
    else:
        print(calculator_functions.str_to_list(_input))
        try:
            input_list = calculator_functions.infix_to_postfix(_input)
        except Exception:
            raise
        else:
            try:
                result = calculator_functions.postfix_to_result(input_list)
            except Exception:
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
