
try:
 cana umutuk(1)
 
except Exception as e:
 file = open("exception.txt","w")
 file.write(e)
 file.close()

