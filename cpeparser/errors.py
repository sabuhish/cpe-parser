
class CpeFormatError(Exception):
    """
        message  explanation of the error
    """
    def __init__(self, message: str):
        self.message = message
