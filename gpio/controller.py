from easylogger import LoggingClass

try:
    import RPi.GPIO as gpio
except RuntimeError:
    class FakeGPIO(LoggingClass):
        IN = "IN"
        OUT = "out"
        FALLING = "falling"
        RISING = "RISING"
        BOARD = "BOARD"

        def setmode(self, mode):
            self.info(f"Set mode {mode}")


    gpio = FakeGPIO()
