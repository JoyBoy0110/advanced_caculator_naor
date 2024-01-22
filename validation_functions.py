from calculator_exceptions import InvalidInputException
from my_math import operators_dictionary

allowed_chars: list = ['+', '-', '*', '/', '^', '@', '$', '&', '%', '~', '!', '.', '#', '(', ')']


def check_input(inpt: str):
    for char in inpt:
        if char.isalpha():
            raise InvalidInputException("the input you have entered is an invalid input")
        if not allowed_chars.__contains__(char) and not char.isdigit():
            raise InvalidInputException("the input you have entered is an invalid input")

def check_valid_input1(invalid_input: list):  # ~- => '', ---
    valid = 'V'
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
        error_char: str = ''
        if left_bracket_counter > right_bracket_counter:
            error_char = '('
        else:
            error_char = ')'
        raise InvalidInputException(str("invalid input: there is an extra " + error_char))


def check_valid_input(invalid_input: list) -> Exception or None:
    bracket_counter: int = 0
    index: int = 0
    changeable_list = list(invalid_input)
    flag: bool == True

    # checking the start of the list
    if operators_dictionary[changeable_list[index]][1] != 'pre' and changeable_list[index] != '-':
        raise InvalidInputException(str(changeable_list[index] + " is not in a valid position"))
    else:
        for i in range(1, len(changeable_list)) and flag:
            if type(changeable_list[i]) is not float and changeable_list[i] != '(':
                if changeable_list[i] != '-':
                    raise InvalidInputException(changeable_list[i]+"is not in a valid place")
            else:
                flag = False


    # checking the end of the list
    if (operators_dictionary[changeable_list[len(changeable_list)-1]][1] != 'post' and
            type(changeable_list[len(changeable_list)-1]) is not float):
        raise InvalidInputException(str(changeable_list[index] + " is not in a valid position"))


    while index<len(changeable_list) -2:
        if changeable_list[index] == '(':
            bracket_counter += 1
        if changeable_list[index] == ')':
            if bracket_counter>0:
                bracket_counter-=1
            else:
                raise InvalidInputException(str("there is an extra ')'s"))

        if operators_dictionary.keys().__contains__(changeable_list[index]) and operators_dictionary.keys().__contains__(changeable_list[index+1]):
            if not check_valid_position(changeable_list[index], changeable_list[index+1]):
                raise InvalidInputException(changeable_list[index+1]+" is not in a valid place")


    if bracket_counter >0:
        raise InvalidInputException(str("there is an extra '('s"))

def decimal_point_check(collection_to_check, index_of_point: int):
    if type(collection_to_check) is str:
        if ((index_of_point == 0 and not str(collection_to_check[index_of_point + 1]).isdigit()) or
                (index_of_point == len(collection_to_check) - 1 and
                 not str(collection_to_check[index_of_point - 1]).isdigit()) or
                (str(collection_to_check[index_of_point + 1]).isdigit() and str(
                    collection_to_check[index_of_point - 1]).isdigit())):
            raise InvalidInputException("'.' is not in a valid position")

    if type(collection_to_check) is list:
        if ((index_of_point == 0 and type(collection_to_check[index_of_point + 1]) is not float) or
                (index_of_point == len(collection_to_check) - 1 and type(
                    collection_to_check[index_of_point - 1]) is not float) or
                (type(collection_to_check[index_of_point + 1]) is not float and type(
                    collection_to_check[index_of_point - 1]) is not float)):
            raise InvalidInputException("'.' is not in a valid position")
    return

def priority_check(operator1: str, operator2: str):
    return (operators_dictionary[operator1])[0] < (operators_dictionary[operator2])[0]


def check_valid_position(operator1: str, operator2: str) -> bool or None:
    if operators_dictionary[operator1][1] == 'in' and operators_dictionary[operator2][1] == 'in' and operator2 != '-':
        return False
    if operators_dictionary[operator1][1] == 'post' and operator2 == 'pre':
        return False
    if operators_dictionary[operator1][1] == 'pre' and operator2 == 'post':
        return False
    if operators_dictionary[operator1][1] == 'pre' and operator2 == 'pre':
        return False
    if operators_dictionary[operator1][1] == 'in' and operator2 == 'post':
        return False
    if operators_dictionary[operator1][1] == 'pre' and operator2 == 'in' and operator2 != '-':
        return False
    return True