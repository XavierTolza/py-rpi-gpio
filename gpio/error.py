class GPIOException(Exception):
    pass

class PinException(GPIOException):
    pass

class PinDirectionError(PinException):
    pass


class InvalidPinError(PinException):
    pass