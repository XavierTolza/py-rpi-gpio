from gpio import GPIO
from time import sleep

pin = GPIO[16]
pin.set_output()

with GPIO:
    try:
        while True:
            pin.toggle()
            sleep(0.1)
    except Exception:
        pass