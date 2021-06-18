from gpio import GPIO
from time import sleep, time


def callback(*args, **kwargs):
    print(args+(time(),))


with GPIO:
    pin = GPIO[16]
    pin.set_input()
    pin.on_falling(callback, bouncetime=200)
    try:
        while True:
            sleep(1)
    except Exception:
        pass
