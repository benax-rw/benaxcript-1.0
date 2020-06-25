from time import strftime, sleep
import os
import http.client
import urllib

    
def feedBack(cmd, server, path, device):
    fields = ["command", "device"]
    data = {}
    data[fields[0]] = cmd
    data[fields[1]] = device
    params = urllib.parse.urlencode(data)
    headers = {}
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Connection"] = "close"
    headers["Content-Length"] = len(params)
    c = http.client.HTTPConnection(server)
    c.request("POST", path, params, headers)
    sleep(0.01)  