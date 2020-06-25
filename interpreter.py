from functions import *

def interpreter(post, server, path):
    command=post
    command=command.replace(":","\n") #Enforcing newline
    command=command.replace(";","\n") #Enforcing newline
    
    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
        os.system("rm /home/pi/benaxFlask/forLoopScript.py")
    if os.path.exists("/home/pi/benaxFlask/forLoopScript.pyc"):
        os.system("rm /home/pi/benaxFlask/forLoopScript.pyc")
    if os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
        os.system("rm /home/pi/benaxFlask/whileLoopScript.py")
    if os.path.exists("/home/pi/benaxFlask/whileLoopScript.pyc"):
        os.system("rm /home/pi/benaxFlask/whileLoopScript.pyc")
                 
# Level One Splitting: Command body is split into lines

    allCommandLines=command.split("\n")
    for i in range(0, len(allCommandLines)):

    #Level Two Splitting: Every line of command body is then processed
    #Every command is made up two parts: Function func and argument arg
    #Below commands takes arguments so they are characterized by "(" and ")"
        
        if ("(" in allCommandLines[i]):
            everyCommandLine = allCommandLines[i].split("(")
            func = everyCommandLine[0].strip()
            arg = everyCommandLine[1]
            arg = arg.replace(")", "")
            #arg = int(arg)

            #Actual interpretation occurs here

            if ("imbere" in func):
                arg = float(arg)
                if(">" in func):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  forward(%d)\n" % arg)
                    file.close()
                else:
                    forward(arg)
                    feedBack("done", server, path)
                
            if ("inyuma" in func):
                arg = float(arg)
                if(">" in func):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  backward(%d)\n" % arg)
                    file.close()
                else:
                    backward(arg)
                    feedBack("done", server, path)

            if ("ibumoso" in func):
                arg = float(arg)
                if(">" in func):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  left(%d)\n" % arg)
                    file.close()
                else:
                    left(arg)
                    feedBack("done", server, path)
                
                
            if ("iburyo" in func):
                arg = float(arg)
                if(">" in func):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  right(%d)\n" % arg)
                    file.close()
                else:
                    right(arg)
                    feedBack("done", server, path)
            
                
            if ("kamera-x" in func):
                arg = int(arg)
                if(">" in func):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  frontCamRotateHorizontal(%d)\n" % arg)
                    file.close()
                else:
                    frontCamRotateHorizontal(arg)
                    feedBack("done", server, path)
                    
            if ("kamera-y" in func):
                arg = int(arg)
                if(">" in func):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  frontCamRotateVertical(%d)\n" % arg)
                    file.close()
                else:
                    frontCamRotateVertical(arg)
                    feedBack("done", server, path)

            if ("cana" in func):
                arg = int(arg)
                if(">" in func):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  topLightON(%d)\n" % arg)
                    file.close()
                else:
                    topLightON(arg)
                    feedBack("done", server, path)

            if ("sinzira" in func):
                arg = int(arg)
                if(">" in func):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  sleep(%d)\n" % arg)
                    file.close()
                else:
                    sleep(arg)
                    feedBack("done", server, path)
                    
            elif (func == "bisubiremo"):
                if (arg=="burundu"):
                    file = open("/home/pi/benaxFlask/whileLoopScript.py","w")
                    file.write("from functions import *\n")
                    file.write("while(True):\n")
                    file.write(" if os.path.exists(\"stop-script\"):\n") #One space Indent
                    file.write("  break\n") #Two space indent
                    file.write(" else:\n") #One space Indent
                    file.close()                        
                else:
                    arg = int(arg)
                    file = open("/home/pi/benaxFlask/forLoopScript.py","w")
                    file.write("from functions import *\n")
                    file.write("for i in range(%d):\n" % arg)
                    file.close()

        #Below comes the part of commands that takes no argument
        else:
            if (allCommandLines[i]=="kina music"):
                os.system("aplay /home/pi/benaxFlask/audio/WhatAboutUs.wav")
                
            elif (allCommandLines[i]=="fotora"):
                takePic()
                feedBack("done", server, path)

            elif ("fungura" in allCommandLines[i]):
                if(">" in allCommandLines[i]):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  handOpen()\n")
                    file.close()
                else:
                    handOpen()
                    feedBack("done", server, path)
                    
            elif ("funga" in allCommandLines[i]):
                if(">" in allCommandLines[i]):
                    if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
                        file = open("/home/pi/benaxFlask/forLoopScript.py","a+")
                    elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
                        file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
                    file.write("  handClose()\n")
                    file.close()
                else:
                    handClose()
                    feedBack("done", server, path)
    
if os.path.exists("/home/pi/benaxFlask/forLoopScript.py"):
    import forLoopScript
elif os.path.exists("/home/pi/benaxFlask/whileLoopScript.py"):
    file = open("/home/pi/benaxFlask/whileLoopScript.py","a+")
    file.write("os.system(\"sudo rm /home/pi/benaxFlask/stop-script\")\n")
    file.close()
    sleep(0.5)
    import whileLoopScript