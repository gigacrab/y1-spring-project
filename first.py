from gpiozero import Robot
from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory

# IN1 BCM21
# IN2 BCM20
# ENA BCM18

# IN3 BCM5
# IN4 BCM6
# ENB BCM13

IN1 = "BCM27"
IN2 = "BCM22"
ENA = "BCM18"

IN3 = "BCM23"
IN4 = "BCM24"
ENB = "BCM19"

# Use pigpio for hardware-based timing
factory = PiGPIOFactory()
robot = Robot(left=Motor(forward=IN3, backward=IN4, pwm=ENB, pin_factory=factory), right=Motor(forward=IN1, backward=IN2, pwm=ENA, pin_factory=factory), pin_factory=factory)

# Robot will now use hardware-driven PWM for speed
robot.forward(0.5) 
