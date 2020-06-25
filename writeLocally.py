import time
from time import strftime, sleep
import http.client, urllib.request, urllib.parse
import netifaces as ni
import os

server = "yellowpages.rw"
path = "/projects/benax/run/catch-device-ip.php"
client_ip = ni.ifaddresses("wlan0")[2][0]["addr"]
  
def ipBroadcast():
    data = {}
    fields = ["upload_start", "client_ip", "device_name"]
    data[fields[0]] = time.strftime("%Y-%b-%d %H:%M:%S %Z")
    data[fields[1]] = client_ip
    data[fields[2]] = "Benax-002"
    params = urllib.parse.urlencode(data)
    headers = {}
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Connection"] = "close"
    headers["Content-Length"] = len(params)
    connect_now = http.client.HTTPConnection(server)
    connect_now.request("POST", path, params, headers)
    os.system("clear")
    print(time.strftime("%Y-%b-%d %H:%M:%S %Z")+": "+client_ip+" sent a packet to server")

def recordOffline():     
    file = open("connection.txt","w")
    file.write("[{\"ip\":\"")
    file.write(client_ip)
    file.write("\",\"upload_start\":\"")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S"))
    file.write("\"}]")
    file.close()


def createTheFlag():     
    file = open("flag-001","w")
    file.write("1")
    file.close()
    
def update():
    while True:
        try:
            recordOffline()
            sleep(1)
            ipBroadcast()
            createTheFlag()
            sleep(5)
            os.system("rm flag-001")
            
        except:
            print ("Error getting IP")

if __name__ == "__main__":
    sleep(30)
    update()