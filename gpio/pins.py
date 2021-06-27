from math import floor, log

from .pin import Pin


class Pins(list):
    @property
    def values(self) -> [bool]:
        return [i.values for i in self]

    @values.setter
    def values(self, value: [bool]):
        if type(value) == int:
            value = ((value >> i) % 2 for i in range(floor(log(5) / log(2)) + 1))
        elif type(value) != list:
            value = (value for _ in self)
        for i, v in zip(self, value):
            i.values = v

    def set_output(self, **kwargs):
        for i in self:  # type: Pin
            i.set_output(**kwargs)

    def set_input(self, **kwargs):
        for i in self:  # type: Pin
            i.set_input(**kwargs)
