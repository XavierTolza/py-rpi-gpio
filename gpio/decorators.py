from gpio.error import PinDirectionError
from .controller import gpio as GPIO


class assert_mode(object):
    def __init__(self, mode):
        self.mode = mode

    def __call__(self, f):
        def wrapper(s, *args, **kwargs):
            if s._direction != self.mode:
                raise PinDirectionError(f"Your pin must be set in direction {self.mode} to call this method")
            return f(s, *args, **kwargs)

        return wrapper


assert_input = assert_mode(GPIO.IN)
assert_output = assert_mode(GPIO.OUT)
