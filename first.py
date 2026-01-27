from gpiozero import Robot
from gpiozero import Motor
#from gpiozero.pins.pigpio import PiGPIOFactory

# Use pigpio for hardware-based timing
#factory = PiGPIOFactory()
robot = Robot(left=Motor("GPIO13", "GPIO19"), right=Motor("GPIO12", "GPIO18"))#, pin_factory=factory)

# Robot will now use hardware-driven PWM for speed
robot.forward(0.5) 
