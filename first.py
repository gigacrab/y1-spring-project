from gpiozero import Robot, Motor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Pin definitions (BCM numbering)
IN1 = 27
IN2 = 22
ENA = 18

IN3 = 23
IN4 = 24
ENB = 19

# Use pigpio for hardware PWM
factory = PiGPIOFactory()

left_motor = Motor(
    forward=IN1,
    backward=IN2,
    enable=ENA,
    pwm=True,
    pin_factory=factory
)

right_motor = Motor(
    forward=IN3,
    backward=IN4,
    enable=ENB,
    pwm=True,
    pin_factory=factory
)

robot = Robot(
    left=left_motor,
    right=right_motor,
    pin_factory=factory
)

# Move forward at 50% speed
robot.forward(0.5)
sleep(1)
robot.forward(0)