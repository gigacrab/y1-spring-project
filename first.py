from gpiozero import Robot
from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory

# IN1 BCM21
# IN2 BCM20
# ENA BCM18

# IN3 BCM5
# IN4 BCM6
# ENB BCM13

# Use pigpio for hardware-based timing
factory = PiGPIOFactory()
robot = Robot(left=Motor(forward="BCM5", backward="BCM6", pwm="BCM13", pin_factory=factory), right=Motor(forward="BCM21", backward="BCM20", pwm="BCM18", pin_factory=factory), pin_factory=factory)

# Robot will now use hardware-driven PWM for speed
robot.forward(0.5) 
