from urllib import request, error
import os
import time
import http.client
import socket
import netifaces as ni
from interpreter import *


current_ip = ni.ifaddresses("wlan0")[2][0]["addr"]
server = current_ip
path="/run/catch-feedback.php"
URL_command='http://'+server+'/run/commands.txt'
URL_order='http://'+server+'/run/order.txt'

os.system("clear")

print ("Listening to "+current_ip+"...\n")

while(True):
    try:
        requestCommand = request.urlopen(URL_command)
        requestOrder = request.urlopen(URL_order)
        command = requestCommand.read().decode('utf-8').strip()
        order = requestOrder.read().decode('utf-8').strip()

        if (order == "do"):
            
            interpreter(command, server, path)
            

    except error.URLError as e:
        feedBack("done", server, path)
                                        

feedBack("done", server, path)