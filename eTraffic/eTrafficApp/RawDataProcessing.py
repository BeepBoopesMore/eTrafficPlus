import re
import paramiko
import unicodedata

#Using this for doing the data mostly 

#Vlan 


with open("testingdata.txt","r") as file:
    data = file.read()
    pattern_vlan_name = r'^\d+\s+([A-Za-z0-9\s]+)\s+(\w+)\s+'
    pattern = r'^\d+\s+[a-zA-Z0-9\s]+(?:\s+active)?\s+([a-zA-Z0-9/,\s]+)'

 


matches_vlan_name = re.findall(pattern_vlan_name, data, re.MULTILINE)
matches_vlan_ports = re.findall(pattern, data, re.MULTILINE)

vlans_status = []
vlans_names = []
vlans_ports = []
#Going Through Matches vlan
for match in matches_vlan_name:
    #Statuses
    vlans_status.append(match[1])
    #Names 
    match  = "".join(match[0].split())
    vlans_names.append(match)

#Data Formmatting for spanning tree
def spanning_tree():
    with open("testingdata.txt","r") as file:
        data = file.read()
        pattern = ""





host = ""
username = ""
password = ""

d = "f0/1"
first_index = d[0]
allowed_prefixes = ["g","f","e"]
if first_index in allowed_prefixes and(d[1] in ["0","1"] and d[3] in ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]):
    if d[2] != "/":
        print("Not a valid interface")
    else:
        interface = d.split(first_index)[1]
        if first_index == "g":
            name = "gi" # I assume ?


        elif first_index == "f":
            name = "fa"


        elif first_index == "e":
            name = "eth" # I assume again ?
            
   

        

        command = "enable && show interfaces switchport | begin " + name + interface
        print(command)


        
       # client = paramiko.client.SSHClient()
        #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #client.connect(host, username=username, password=password)
        #_stdin, _stdout,_stderr = client.exec_command(command)
       # command_output = "".join(_stdout.read().decode())





else:
    print("Not a valid interface")






