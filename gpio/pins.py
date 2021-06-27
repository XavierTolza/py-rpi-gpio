from math import floor, log

from .pin import Pin


class Pins(list):
    @property
    def values(self) -> [bool]:
        return [i.values for i in self]

    @values.setter
    def values(self, value: [bool]):
        vtype = type(value)
        if vtype == int:
            values = ((value >> i) % 2 for i in range(floor(log(5) / log(2)) + 1))
        elif vtype != list:
            values = (value for _ in self)
            
        for i, v in zip(self, values):
            i.values = v

    def set_output(self, **kwargs):
        for i in self:  # type: Pin
            i.set_output(**kwargs)

    def set_input(self, **kwargs):
        for i in self:  # type: Pin
            i.set_input(**kwargs)
