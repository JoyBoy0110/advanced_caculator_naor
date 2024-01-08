error_list = []


class InputErrorException(RuntimeError):
    def __init__(self):
        pass

    def __str__(self):
        return "the input you have entered is an invalid input"


def check_input(inpt: str):
    raise RuntimeError


def interface() -> str:
    equation: str = ""
    try:
        equation: str = input()
        check_input(equation)
    except RuntimeError as run_time_error:
        print(run_time_error)
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
    calculate()
    return


if __name__ == "__main__":
    main()
