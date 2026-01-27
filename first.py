from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory

# Use pigpio for hardware-based timing
factory = PiGPIOFactory()
robot = Robot(left=("BCM5", "BCM6", "BCM13"), right=("BCM21", "BCM20", "BCM18"), pin_factory=factory)

# Robot will now use hardware-driven PWM for speed
robot.forward(0.5) 
