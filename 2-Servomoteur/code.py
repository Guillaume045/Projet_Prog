import time
import machine

p4 = machine.Pin(4)
servo = machine.PWM(p4,freq=50)

while True:
    servo.duty(40)
    time.sleep(2)
    servo.duty(120)
    time .sleep(2)
    
