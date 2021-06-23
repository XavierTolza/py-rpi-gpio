class Pins(list):
    @property
    def values(self) -> [bool]:
        return [i.values for i in self]

    @values.setter
    def values(self, value: [bool]):
        for i, v in zip(self, value):
            i.values = v
