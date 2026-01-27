from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory

# Use pigpio for hardware-based timing
factory = PiGPIOFactory()
robot = Robot(left=("GPIO13", "GPIO19"), right=("GPIO12", "GPIO18"), pin_factory=factory)

# Robot will now use hardware-driven PWM for speed
robot.forward(0.5) 
