import functions as y
from functions import *
init()

while (True):
 if os.path.exists("stop-script"):
  break
 else:
  senseRange()
  if y.distance<20:
   beepOnce(1)
os.remove('/var/www/html/1.0/stop-script')


finish()
