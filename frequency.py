from gpiozero import DigitalOutputDevice, PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import sys

pwm_freq = 800

if __name__ == "__main__":
    if len(sys.argv) > 2:
        left_speed = float(sys.argv[1])
        right_speed = float(sys.argv[2])
        if len(sys.argv) == 4:
            pwm_freq = int(sys.argv[3])
    else:
        raise Exception("Didn't input appropriate variables")

# use pigpio for hardware PWM backend
factory = PiGPIOFactory()

# pin definitions (BCM numbering)
IN1 = DigitalOutputDevice(27, pin_factory=factory)
IN2 = DigitalOutputDevice(22, pin_factory=factory)
ENA = PWMOutputDevice(18, pin_factory=factory)

IN3 = DigitalOutputDevice(23, pin_factory=factory)
IN4 = DigitalOutputDevice(24, pin_factory=factory)
ENB = PWMOutputDevice(19, pin_factory=factory)

def forward(a, b, f):
    ENA.frequency = ENB.frequency = f
    if a > 0:
        IN1.on()
        IN2.off()
    elif a < 0:
        IN1.off()
        IN2.on()
    else: 
        IN1.off()
        IN2.off()
    if b > 0:
        IN3.on()
        IN4.off()
    elif b < 0:
        IN3.off()
        IN4.on()
    else:
        IN3.off()
        IN4.off()

        
        

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
robot.value = (left_speed, right_speed)
time.sleep(2)
robot.stop()