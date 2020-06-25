import os
import sys
sys.path.insert(0, "/var/www/html/1.0")
from functions import init,blinkBlue

init()
while (True):
    try:
        if os.path.exists("/var/www/html/1.0/blink-script"):
            blinkBlue()
    except:
        print ("Error blinking!")
        
