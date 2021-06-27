from gpio.error import InvalidPinError
from .controller import gpio as GPIO
from .decorators import assert_input, assert_output


class GenericPin(object):
    abstract = NotImplementedError("This method is abstract")

    INPUT = GPIO.IN
    OUTPUT = GPIO.OUT
    FALLING = GPIO.FALLING
    RISING = GPIO.RISING
    ON = True
    OFF = False

    def __init__(self, pin_id):
        self._pin_id = pin_id
        self._direction = None

    @property
    def pin_id(self):
        return self._pin_id

    def setup(self, mode, *args, **kwargs):
        self._direction = mode

    def set_input(self, **kwargs):
        self.setup(self.INPUT, **kwargs)

    def set_output(self, **kwargs):
        self.setup(self.OUTPUT, **kwargs)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self.setup(value)

    @property
    @assert_input
    def value(self) -> bool:
        raise self.abstract

    @property
    def inverted_value(self):
        return self.invert_pin_level(self.value)

    @value.setter
    @assert_output
    def value(self, value: bool):
        raise self.abstract

    @staticmethod
    def invert_pin_level(value: bool):
        return 1 - value

    def toggle(self) -> None:
        self.value = self.inverted_value

    def read(self) -> bool:
        return self.value

    @assert_input
    def wait(self, event):
        raise self.abstract

    def wait_falling(self):
        self.wait(GPIO.FALLING)

    def wait_rising(self):
        self.wait(GPIO.RISING)

    def wait_both(self):
        self.wait(GPIO.BOTH)

    @assert_input
    def on_interrupt(self, event, callback, bouncetime=100, **kwargs):
        raise self.abstract

    def on_rising(self, *args, **kwargs):
        self.on_interrupt(GPIO.RISING, *args, **kwargs)

    def on_falling(self, *args, **kwargs):
        self.on_interrupt(GPIO.FALLING, *args, **kwargs)

    def on_both(self, *args, **kwargs):
        self.on_interrupt(GPIO.BOTH, *args, **kwargs)


class Pin(GenericPin):
    def setup(self, mode, *args, **kwargs):
        super(Pin, self).setup(mode, *args, **kwargs)
        try:
            GPIO.setup(self.pin_id, mode, *args, **kwargs)
        except ValueError as e:
            if "channel sent is invalid" in str(e):
                raise InvalidPinError(f"Pin {self.pin_id} is invalid on Rapsberry Pi")

    @property
    @assert_input
    def value(self) -> bool:
        return GPIO.input(self.pin_id)

    @value.setter
    @assert_output
    def value(self, value: bool):
        GPIO.output(self.pin_id, value)

    @assert_input
    def wait(self, event):
        GPIO.wait_for_edge(self.pin_id, event)

    @assert_input
    def on_interrupt(self, event, callback, bouncetime=100, **kwargs):
        GPIO.add_event_detect(
            self.pin_id, event, callback=callback, bouncetime=bouncetime, **kwargs)
