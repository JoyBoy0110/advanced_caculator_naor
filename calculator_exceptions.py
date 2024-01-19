class InvalidInputException(RuntimeError):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid input"
