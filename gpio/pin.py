from .controller import gpio as GPIO
from .decorators import assert_input, assert_output


class Pin(object):
    INPUT = GPIO.IN
    OUTPUT = GPIO.OUT
    FALLING = GPIO.FALLING
    RISING = GPIO.RISING

    def __init__(self, gpio, pin_id):
        self.__gpio = gpio
        self.pin_id = pin_id
        self._direction = None

    def setup(self, mode, *args, **kwargs):
        self._direction = mode
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
    def value(self) -> bool:
        return GPIO.input(self.pin_id)

    def read(self) -> bool:
        return self.value

    @value.setter
    @assert_output
    def value(self, value: bool):
        GPIO.output(self.pin_id, value)

    @assert_input
    def wait(self, event):
        GPIO.wait_for_edge(self.pin_id, event)

    def wait_falling(self):
        self.wait(GPIO.FALLING)

    def wait_rising(self):
        self.wait(GPIO.RISING)

    def wait_both(self):
        self.wait(GPIO.BOTH)

    @assert_input
    def on_interrupt(self, event, callback, bouncetime=100, **kwargs):
        GPIO.add_event_detect(self.pin_id, event, callback=callback, bouncetime=bouncetime, **kwargs)

    def on_rising(self, *args, **kwargs):
        self.on_interrupt(GPIO.RISING, *args, **kwargs)

    def on_falling(self, *args, **kwargs):
        self.on_interrupt(GPIO.FALLING, *args, **kwargs)

    def on_both(self, *args, **kwargs):
        self.on_interrupt(GPIO.BOTH, *args, **kwargs)
