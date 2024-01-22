import pytest
import calculator_functions
from calculator_exceptions import InvalidInputException
from validation_functions import check_input
error_list = []


def interface() -> str:
    equation: str = ""
    while True:
        print("calculator:")
        print("for exit press x")
        print("for calculator press c")
        command = input()
        if command == 'x':
            return
        print("insert equation: ")
        equation: str = input()
        equation.replace(" ", "")
        equation.replace("  ", "")
        _output: float
        try:
            _output = cal(equation)
        except ArithmeticError as e:
            print(e)
        except InvalidInputException as e:
            print(e)
        else:
            print(_output)



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
    interface()


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


if __name__ == "__main__":
    main()
