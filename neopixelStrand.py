from functions import *

# Intialize the library (must be called once before other functions).
strip.begin()

while (True):
    if os.path.exists("/var/www/html/1.0/neopixel-running-script"):
        colorWipe(strip, Color(0,0,0), 2)   
        break
    else:
        #print ('Color wipe animations.')
        colorWipe(strip, Color(255, 0, 0))  # Red wipe
        colorWipe(strip, Color(0, 255, 0))  # Blue wipe
        colorWipe(strip, Color(0, 0, 255))  # Green wipe
        #print ('Theater chase animations.')
        theaterChase(strip, Color(127, 127, 127))  # White theater chase
        theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
        #print ('Rainbow animations.')
        rainbow(strip)
        rainbowCycle(strip)
        theaterChaseRainbow(strip)     
os.remove('/var/www/html/1.0/neopixel-running-script')

