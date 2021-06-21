from warnings import warn

try:
    import RPi.GPIO as gpio
except (ImportError, RuntimeError):
    warn("Rpi gpio is not installed. Defaulting to simulated gpio")
    from gpio.simulated import SimulatedGPIO

    gpio = SimulatedGPIO()
