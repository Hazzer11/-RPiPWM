import RPi.GPIO as GPIO
import time
"""GPIO.cleanup()""" 
GPIO.setmode(GPIO.BOARD)
pinTrigger = 18
led_pin = 16
pinEcho = 22
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

#frequency 500 Hz
led_pwm = GPIO.PWM(led_pin, 50)
#duty cycle = 100
led_pwm.start(100)


while True:#loop
    ##############Starting for distance#############
    # set Trigger to HIGH
    GPIO.output(pinTrigger, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    startTime = time.time()
    stopTime = time.time()

    while 0 == GPIO.input(pinEcho):
        startTime = time.time()
        

    while 1 == GPIO.input(pinEcho):
        stopTime = time.time()
        
    TimeElapsed = stopTime - startTime
    distance = (TimeElapsed * 34300) / 2
    print ("Distance: %.1f cm" % distance)
    ##############Starting for lights#############
    if(distance<5.0):
        if(distance>=0):
            led_pwm.ChangeDutyCycle(100)
    if (distance<10.0):
        if (distance>=5.0):
            led_pwm.ChangeDutyCycle(60)
    if (distance<15.0 ):
        if (distance>=10.0):
            led_pwm.ChangeDutyCycle(40)
    if (distance<20.0):
        if (distance>=15.0):
            led_pwm.ChangeDutyCycle(20)
    if (distance>=20.0):
        led_pwm.ChangeDutyCycle(0)
