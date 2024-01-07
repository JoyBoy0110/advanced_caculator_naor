error_list = []

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
