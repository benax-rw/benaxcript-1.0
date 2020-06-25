from functions import *

# Intialize the library (must be called once before other functions).
strip.begin()

init()
forward(0.1,60)
pause(0.5)
backward(0.1,50)
stop()
beepThrice()
finish()

#print ('Color wipe animations.')
colorWipe(strip, Color(255, 0, 0))  # Red wipe
colorWipe(strip, Color(0, 255, 0))  # Blue wipe
colorWipe(strip, Color(0, 0, 255))  # Green wipe
#print ('Theater chase animations.')
theaterChase(strip, Color(127, 127, 127))  # White theater chase

#clear at the end
colorWipe(strip, Color(0,0,0), 0)

