
class CpeFormatError(Exception):
    """
    explanation of the error with message param
    """
    def __init__(self, message: str):
        self.message = message
