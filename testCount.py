import functions as y
from functions import *
init()

beepTwice()
server = 'yellowpages.rw'
path = '/projects/benax/run/catch-feedback.php'

count = 0
while(count < 5):
  count += 1
  forward(1,66)
backward(1,70)

feedBack('while (True):--- if os.path.exists("stop-script"):---  break--- else:------  senseRangeMiddle()---  if(y.distanceMiddle<50):---    backward(0.1,60)---    left(0.2,60)---  else:---    for i in range(5):---      forward(0.1,50)------  senseRangeLeft()---  if(y.distanceLeft<50):---    backward(0.1,60)---    right(0.2,60)---  else:---    forward(0.1,50)------  senseRangeRight()---  if(y.distanceRight<50):---    backward(0.1,60)---    left(0.2,60)---  else:---    forward(0.1,50)',server,path,'Benax-3.0-1')


finish()
