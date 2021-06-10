from .controller import gpio as GPIO
from .decorators import assert_input, assert_output


class Pin(object):
    INPUT = GPIO.IN
    OUTPUT = GPIO.OUT

    def __init__(self, gpio, pin_id):
        self.__gpio = gpio
        self.pin_id = pin_id
        self.__direction = None

    def setup(self, mode, *args, **kwargs):
        self.__direction = mode
        GPIO.setup(self.pin_id, mode, *args, **kwargs)

    def set_input(self, **kwargs):
        self.setup(self.INPUT, **kwargs)

    def set_output(self, **kwargs):
        self.setup(self.OUTPUT, **kwargs)

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.setup(value)

    @property
    @assert_input
    def value(self):
        return GPIO.input(self.pin_id)

    @value.setter
    @assert_output
    def value(self, value):
        GPIO.output(self.pin_id, value)