import json
from time import sleep
from eTrafficApp.eTraffic import Router
import paramiko
with open("portchannelsetting.json","r") as file :
    d = json.load(file)
    m = d["Interfaces"]
    #for item in m:
        #g = item
        #list.append(g)
    
    for item in m:
        host = "192.168.1.136"
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        client.connect(host,username="John",password="aff")
        _stdin, _stdout,_stderr = client.exec_command("mkdir " + item)
        command_output = "".join(_stdout.read().decode())
        print(command_output)