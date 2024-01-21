class InvalidInputException(RuntimeError):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class UndefinedException(ArithmeticError):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
