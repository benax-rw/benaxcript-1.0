import functions as y
from functions import *
init()

server = 'yellowpages.rw'
path = '/projects/benax/run/catch-feedback.php'

import functions as y
from functions import *
init()

server = 'yellowpages.rw'
path = '/projects/benax/run/catch-feedback.php'

while (True):
 senseRangeRight()
 if(y.distanceRight<10):
  beepOnce(0.5)
feedBack('while (True)--- senseRangeRight()--- if(y.distanceRight<10):---  beepOnce(0.5)',server,path,'Benax-3.0-1')


finish()


while(True):
    senseRangeRight()
    
    if (0.8<y.distanceRight<10):
        beepOnce(0.3)



finish()
