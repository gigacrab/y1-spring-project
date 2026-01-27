from gpiozero import Robot, Motor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# pin definitions (BCM numbering)
IN1 = "BCM27"
IN2 = "BCM22"
ENA = "BCM18"

IN3 = "BCM23"
IN4 = "BCM24"
ENB = "BCM19"

# use pigpio for hardware PWM backend
factory = PiGPIOFactory()

robot = Robot(
    left=Motor(forward=IN3, backward=IN4, enable=ENB),
    right=Motor(forward=IN1, backward=IN2, enable=ENA),
    pin_factory=factory
)

def turn():
    pass

robot.forward(speed=0.5)
sleep(1)
robot.forward(0)