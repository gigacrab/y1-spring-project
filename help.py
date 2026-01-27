from gpiozero import DigitalOutputDevice, PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import sys

pwm_freq = 800

# time to complete one rev at max speed
T_360 = 1.5

# __main__ is the script that was passed to execute
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
ENA = PWMOutputDevice(18)

IN3 = DigitalOutputDevice(23, pin_factory=factory)
IN4 = DigitalOutputDevice(24, pin_factory=factory)
ENB = PWMOutputDevice(19)
ENA.frequency = pwm_freq
ENB.frequency = pwm_freq

def move(a, b, f):
    ENA.value, ENB.value = a, b
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
    turn_time = (1 / speed) * T_360 * (angle / 360)
    if (dir.lower() == "left"):
        move(-left_speed, -right_speed, pwm_freq)
    else:   
        move(left_speed, -right_speed, pwm_freq)
    time.sleep(turn_time)
    move(0, 0, pwm_freq)

move(left_speed, right_speed, pwm_freq)
time.sleep(13)
move(0, 0, pwm_freq)