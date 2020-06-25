import time
from time import strftime, sleep
import http.client, urllib.request, urllib.parse
import netifaces as ni
import os

def ipBroadcast():
    server = "yellowpages.rw"
    path = "/projects/benax/run/catch-device-ip.php"
    client_ip = ni.ifaddresses("wlan0")[2][0]["addr"]
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

def update():
    while True:
        try:
            ipBroadcast()
            os.system("touch /var/www/html/1.0/blink-script")
            sleep(5)
            os.system("rm /var/www/html/1.0/blink-script")
            sleep(5)
        except:
            print ("Error getting IP")

if __name__ == "__main__":
    sleep(30)
    update()
