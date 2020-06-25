import RPi.GPIO as GPIO
from time import strftime, sleep, time
import os
from neopixel import *
import _rpi_ws281x as ws

front_left_motor_enable = 7
front_left_motor_forward = 11
front_left_motor_backward = 12
front_left_motor = (front_left_motor_enable, front_left_motor_forward, front_left_motor_backward)

front_right_motor_enable = 13
front_right_motor_forward = 15
front_right_motor_backward = 16
front_right_motor = (front_right_motor_enable, front_right_motor_forward, front_right_motor_backward)

rear_left_motor_enable = 18
rear_left_motor_forward = 22
rear_left_motor_backward = 29
rear_left_motor = (rear_left_motor_enable, rear_left_motor_forward, rear_left_motor_backward)

rear_right_motor_enable = 31
rear_right_motor_forward = 35
rear_right_motor_backward = 36
rear_right_motor = (rear_right_motor_enable, rear_right_motor_forward, rear_right_motor_backward)


#neopixel = 32
beep = 33

trigger = 37
echo = 38

hand = 40

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 12      # pin 32 BOARD
#LED_PIN        = 18     # pin 12 BOARD
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

speed = 40   #Not a pin number, but a speed 40%

def GPIOSetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def setupTheMotor ():
    #print ("Setting up...")
    GPIOSetup()
    GPIO.setup (front_left_motor, GPIO.OUT)
    GPIO.setup (front_right_motor, GPIO.OUT)
    GPIO.setup (rear_left_motor, GPIO.OUT)
    GPIO.setup (rear_right_motor, GPIO.OUT)     
    #print ("Ready")
    
def rangeSensorSetup():
    GPIOSetup()
    GPIO.setup(trigger,GPIO.OUT)
    GPIO.setup(echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
def rangeSensorLeftSetup():
    GPIOSetup()
    GPIO.setup(triggerLeft,GPIO.OUT)
    GPIO.setup(echoLeft, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
    
def rangeSensorMiddleSetup():
    GPIOSetup()
    GPIO.setup(triggerMiddle,GPIO.OUT)
    GPIO.setup(echoMiddle, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    

def rangeSensorRightSetup():
    GPIOSetup()
    GPIO.setup(triggerRight,GPIO.OUT)
    GPIO.setup(echoRight, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
def beepSetup():
    GPIOSetup()
    GPIO.setup(beep,GPIO.OUT)
    
def blueLEDSetup():
    GPIOSetup()
    GPIO.setup(blueLED,GPIO.OUT)

def handSetup():
    GPIOSetup()
    GPIO.setup(hand, GPIO.OUT)
    global handControl
    handControl = GPIO.PWM(hand, 75)
        
def forward(t,speed):
    print ("Forward, speed = ", speed)
    GPIO.output (front_left_motor_forward, 1)
    GPIO.output (front_left_motor_backward, 0)

    pwmFrontLeft.ChangeDutyCycle(speed)
    
    GPIO.output (rear_left_motor_forward, 1)
    GPIO.output (rear_left_motor_backward, 0)
    
    pwmRearLeft.ChangeDutyCycle(speed)
    
    GPIO.output (front_right_motor_forward, 1)
    GPIO.output (front_right_motor_backward, 0)
    
    pwmFrontRight.ChangeDutyCycle(speed)
    
    GPIO.output (rear_right_motor_forward, 1)
    GPIO.output (rear_right_motor_backward, 0)
    
    pwmRearRight.ChangeDutyCycle(speed)
    sleep(t)
    
def backward(t,speed):  
    print ("Reverse, speed = ", speed)
    GPIO.output (front_left_motor_forward, 0)
    GPIO.output (front_left_motor_backward, 1)

    pwmFrontLeft.ChangeDutyCycle(speed)
    
    GPIO.output (rear_left_motor_forward, 0)
    GPIO.output (rear_left_motor_backward, 1)
    
    pwmRearLeft.ChangeDutyCycle(speed)
    
    GPIO.output (front_right_motor_forward, 0)
    GPIO.output (front_right_motor_backward, 1)
    
    pwmFrontRight.ChangeDutyCycle(speed)
    
    GPIO.output (rear_right_motor_forward, 0)
    GPIO.output (rear_right_motor_backward, 1)
    
    pwmRearRight.ChangeDutyCycle(speed)
    sleep(t)

def right(t,speed):   
    print ("Right, speed = ", speed)
    GPIO.output (front_left_motor_forward, 1)
    GPIO.output (front_left_motor_backward, 0)

    pwmFrontLeft.ChangeDutyCycle(speed)
    
    GPIO.output (rear_left_motor_forward, 1)
    GPIO.output (rear_left_motor_backward, 0)
    
    pwmRearLeft.ChangeDutyCycle(speed)
    
    GPIO.output (front_right_motor_forward, 0)
    GPIO.output (front_right_motor_backward, 1)
    
    pwmFrontRight.ChangeDutyCycle(speed)
    
    GPIO.output (rear_right_motor_forward, 0)
    GPIO.output (rear_right_motor_backward, 1)
    
    pwmRearRight.ChangeDutyCycle(speed)
    sleep(t)
    
def left(t,speed):   
    print ("Left, speed = ", speed)
    GPIO.output (front_left_motor_forward, 0)
    GPIO.output (front_left_motor_backward, 1)

    pwmFrontLeft.ChangeDutyCycle(speed)
    
    GPIO.output (rear_left_motor_forward, 0)
    GPIO.output (rear_left_motor_backward, 1)
    
    pwmRearLeft.ChangeDutyCycle(speed)
    
    GPIO.output (front_right_motor_forward, 1)
    GPIO.output (front_right_motor_backward, 0)
    
    pwmFrontRight.ChangeDutyCycle(speed)
    
    GPIO.output (rear_right_motor_forward, 1)
    GPIO.output (rear_right_motor_backward, 0)
    
    pwmRearRight.ChangeDutyCycle(speed)
    sleep(t)

def leftBackward(t,speed):  
    print ("Left Backward, speed = ", speed)
    GPIO.output (front_left_motor_forward, 1)
    GPIO.output (front_left_motor_backward, 0)
    pwmFrontLeft.ChangeDutyCycle(speed)
    GPIO.output (front_right_motor_forward, 0)
    GPIO.output (front_right_motor_backward, 1)
    pwmFrontRight.ChangeDutyCycle(speed)
    sleep(t)


def rightBackward(t,speed):     
    print ("Left Backward, speed = ", speed)
    GPIO.output (front_left_motor_forward, 0)
    GPIO.output (front_left_motor_backward, 1)
    pwmFrontLeft.ChangeDutyCycle(speed)
    GPIO.output (front_right_motor_forward, 1)
    GPIO.output (front_right_motor_backward, 0)
    pwmFrontRight.ChangeDutyCycle(speed)
    sleep(t)
    
def pause(t):
    GPIO.output (front_left_motor_forward, 0)
    GPIO.output (front_left_motor_backward, 0)
    pwmFrontLeft.ChangeDutyCycle(0)
    GPIO.output (front_right_motor_forward, 0)
    GPIO.output (front_right_motor_backward, 0)
    pwmFrontRight.ChangeDutyCycle(0)
    sleep(t)

def stop():
    GPIO.output (front_left_motor_forward, 0)
    GPIO.output (front_left_motor_backward, 0)
    pwmFrontLeft.ChangeDutyCycle(0)
    GPIO.output (front_right_motor_forward, 0)
    GPIO.output (front_right_motor_backward, 0)
    pwmFrontRight.ChangeDutyCycle(0)
    
#initialize() must be called everytime in the beginning
def init():
    #print("Initializing...")
    global pwmFrontLeft
    global pwmFrontRight
    global pwmRearLeft
    global pwmRearRight
    
    setupTheMotor ()
    
    pwmFrontLeft = GPIO.PWM (front_left_motor_enable, 100)
    pwmFrontRight = GPIO.PWM (front_right_motor_enable, 100)
    pwmFrontLeft.start (0)
    pwmFrontRight.start (0)

    pwmRearLeft = GPIO.PWM (rear_left_motor_enable, 100)
    pwmRearRight = GPIO.PWM (rear_right_motor_enable, 100)
    pwmRearLeft.start (0)
    pwmRearRight.start (0)

#ifinish() must be called everytime in the end
def finish():
    #print("Done")
    GPIO.output (front_left_motor_enable, 0)
    GPIO.output (front_left_motor_forward, 0)
    GPIO.output (front_left_motor_backward, 0)
    GPIO.output (front_right_motor_enable, 0)
    GPIO.output (front_right_motor_forward, 0)
    GPIO.output (front_right_motor_backward, 0)
    GPIO.output (rear_left_motor_enable, 0)
    GPIO.output (rear_left_motor_forward, 0)
    GPIO.output (rear_left_motor_backward, 0)
    GPIO.output (rear_right_motor_enable, 0)
    GPIO.output (rear_right_motor_forward, 0)
    GPIO.output (rear_right_motor_backward, 0)    
    pwmFrontLeft.stop ()
    pwmFrontRight.stop ()
    pwmRearLeft.stop ()
    pwmRearRight.stop ()    
    GPIO.cleanup

def senseRange():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(trigger, GPIO.OUT)
	GPIO.setup(echo, GPIO.IN)
	GPIO.output(trigger, False)
	
	#print "waiting for sensor to settle"
	
	sleep(1)
	GPIO.output(trigger, True)
	sleep(0.00001)
	GPIO.output(trigger, False)
	while GPIO.input(echo)==0:
			pulse_start = time()
	while GPIO.input(echo)==1:
			pulse_end = time()
	
	pulse_duration = pulse_end - pulse_start
	
	#multiply with the sonic speed (34300 cm/s)
	#and divide by 2, because there and back
	
	global distance
	
	distance = (pulse_duration * 34300) / 2
	distance = round(distance, 2)

    
def senseRangeLeft():
    rangeSensorLeftSetup()
    global distanceLeft
    GPIO.output(triggerLeft, 0)
    sleep(0.5)
    GPIO.output(triggerLeft, 1)
    sleep(0.00001)
    GPIO.output(triggerLeft, 0)
    while GPIO.input(echoLeft)==0:
        pulse_start = time()
    while GPIO.input(echoLeft)==1:
        pulse_end = time()       
    pulse_duration = pulse_end - pulse_start
    distanceLeft = pulse_duration * 17150
    distanceLeft = round(distanceLeft, 0)   


def senseRangeMiddle():
    rangeSensorMiddleSetup()
    global distanceMiddle
    GPIO.output(triggerMiddle, 0)
    sleep(0.5)
    GPIO.output(triggerMiddle, 1)
    sleep(0.00001)
    GPIO.output(triggerMiddle, 0)
    while GPIO.input(echoMiddle)==0:
        pulse_start = time()
    while GPIO.input(echoMiddle)==1:
        pulse_end = time()       
    pulse_duration = pulse_end - pulse_start
    distanceMiddle = pulse_duration * 17150
    distanceMiddle = round(distanceMiddle, 0)
    
def senseRangeRight():
    rangeSensorRightSetup()
    global distanceRight
    GPIO.output(triggerRight, 0)
    sleep(0.5)
    GPIO.output(triggerRight, 1)
    sleep(0.00001)
    GPIO.output(triggerRight, 0)
    while GPIO.input(echoRight)==0:
        pulse_start = time()
    while GPIO.input(echoRight)==1:
        pulse_end = time()       
    pulse_duration = pulse_end - pulse_start
    distanceRight = pulse_duration * 17150
    distanceRight = round(distanceRight, 0)


def beepOnce(t):
    beepSetup()
    GPIO.output(beep,1)
    sleep(t)
    GPIO.output(beep,0)

def beepTwice():
    beepSetup()
    for i in range(2):
        GPIO.output(beep,1)
        sleep(0.1)
        GPIO.output(beep,0)
        sleep(0.1)

def beepThrice():
    beepSetup()
    for i in range(3):
        GPIO.output(beep,1)
        sleep(0.1)
        GPIO.output(beep,0)
        sleep(0.1)
         
def blinkGreen():
    strip.begin()
    theaterChase(strip, Color(255, 0, 0))  # Green theater chase
    theaterChase(strip, Color(0, 0, 0))  # White theater chase

def turnONgreenLED(t):
    strip.begin()
    colorWipe(strip, Color(255, 0, 0))
    sleep(t)
    colorWipe(strip, Color(0, 0, 0))
    
def blinkRed():
    strip.begin()
    theaterChase(strip, Color(0, 255, 0))  # Green theater chase
    theaterChase(strip, Color(0, 0, 0))  # White theater chase
   
def turnONredLED(t):
    strip.begin()
    colorWipe(strip, Color(0, 255, 0))
    sleep(t)
    colorWipe(strip, Color(0, 0, 0))
   
def clearLED():
    strip.begin()
    theaterChase(strip, Color(0, 0, 0))
    sleep()
    
def turnONblueLED():
    blueLEDSetup()
    GPIO.output(blueLED,1)    

def turnOFFblueLED():
    blueLEDSetup()
    GPIO.output(blueLED,0)
    

def blinkBlue():
    for i in range(2):
        turnONblueLED()
        sleep(0.25)
        turnOFFblueLED()
        sleep(0.25)
    sleep(7)

def handOpen():    
    handSetup()
    handControl.start(3)
    sleep(1)
    GPIO.cleanup()    
    
def handClose():
    handSetup()
    handControl.start(6) 
    sleep(1)
    GPIO.cleanup()
    
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    #"""Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    #"""Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    #"""Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    #"""Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    #"""Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    #"""Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
                
