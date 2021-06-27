from .pin import Pin
from .controller import gpio
from .pins import Pins


class GPIO(object):
    def __init__(self) -> None:
        gpio.setmode(gpio.BOARD)

    def __getitem__(self, pin_id):
        if issubclass(type(pin_id), list):
            return Pins(self[i] for i in pin_id)
        else:
            return Pin(self, pin_id)

    def apply_on_many_pins(self, method, **pin_ids_values):
        for pin_id, value in pin_ids_values.items():
            getattr(self[pin_id], method)(value)

    def set_mode(self, **pin_ids_values):
        self.apply_on_many_pins("set_mode", **pin_ids_values)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        gpio.cleanup()
