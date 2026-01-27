from gpiozero import Robot, Motor
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import sys

input_speed = 1
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_speed = sys.argv[1]

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

def turn(speed, angle, dir):
    # time to complete one rev at max speed
    t = 1.5
    turn_time = (1 / speed) * t * (angle / 360)
    if (dir.lower() == "left"):
        robot.left(speed=speed)
    else:
        robot.right(speed=speed)
    time.sleep(turn_time)
    robot.stop()

#turn(1, 360, "left")
robot.forward(input_speed)