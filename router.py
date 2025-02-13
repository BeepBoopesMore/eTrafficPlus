import paramiko
import json
import time 
import requests


class Router():
    def __init__(self,host:str,username:str,password:str,vendor:str):
        #Defining The Router
        self.vendor = vendor
        self.host = host
        self.username = username
        self.password = password
        #Commands for Cisco
        if vendor == "Cisco":
            #Clock
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command("en && show clock detail")
            raw = _stdout.read().decode()
            self.clock = "".join(raw)
            #Hostname
            client2 = paramiko.client.SSHClient()
            client2.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client2.connect(self.host, username=self.username, password=self.password) 
            _stdin, _stdout,_stderr = client.exec_command("show running-config | include hostname")
            raw2 = _stdout.read().decode()
            self.hostname = "".join(raw2) 
            #Something new

        #Commands for Cisco
        if vendor == "cisco":
            #Clock
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command("en && show clock detail")
            raw = _stdout.read().decode()
            self.clock = "".join(raw)
            #Hostname
            client2 = paramiko.client.SSHClient()
            client2.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client2.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command("show running-config | include hostname")
            raw2 = _stdout.read().decode()
            self.hostname = "".join(raw2)
            #Something new



    
        if vendor == "Juniper":
                print("")
        if vendor == "juniper":
                print("")
        if vendor == "Huawei":
                print("")
        if vendor == "huawei":
                print("")
        else:
                print("We don't have this Vendor curently,email us to discuss more...")

        #WiP INFO ABOUT THE ROUTER 

        pass
      
    #Send a specific command 
    def send_command(self,command:str):
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        client.connect(self.host, username=self.username, password=self.password)
        _stdin, _stdout,_stderr = client.exec_command("cd")
        raw = _stdout.read().decode()
        #Turning Decoding Into String For Scraping 
        command_output = "".join(raw)
        print(command_output)


    #INTERFACES IPV4
    def show_ipv4_interfaces(self):
        print("Waiting")


    #License 
    def license(self,mode:str):
        if mode == "mode1here":
            print("do sum")
        elif mode == "mode2here":
             print("do sum here")
        elif mode == "mode3here":
             print('do some here')
        else:
             print("This option does not exist...")


    #INTERFACES IPV6
    def show_ipv6_interfaces(self):
        print("Waiting")





    #Show Running Config
    def show_running_config(self):
        if self.vendor == "Cisco":
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command("en && show running_config")
            command_output = "".join(_stdout.read().decode())
            print(command_output)
        if self.vendor == "cisco":
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command("en && show running_config")
            command_output = "".join(_stdout.read().decode())
            print(command_output)
        if self.vendor == "Juniper":
            print("Coming")
        if self.vendor == "juniper":
            print("Coming")
    

    


    def routing_protocol(self):
        if self.vendor == "Cisco":
           client = paramiko.client.SSHClient()
           client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
           client.connect(self.host, username=self.username, password=self.password)
           _stdin, _stdout,_stderr = client.exec_command("en && show ip protocols")
           command_output = "".join(_stdout.read().decode())
        if self.vendor == "cisco":
           client = paramiko.client.SSHClient()
           client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
           client.connect(self.host, username=self.username, password=self.password)
           _stdin, _stdout,_stderr = client.exec_command("en && show ip protocols")
           command_output = "".join(_stdout.read().decode())
        if self.vendor == "Juniper":
            command = 'show configuration protocols'
        
        if self.vendor == "juniper":
             command = 'show configuration protocols'




    #Make multiple changes for multiple routers based on a template
    def make_changes(self,template_path):
        #template_path =  
        #JSON
        print("Waiting")
    
   

    #Static Route Maker
    #In the future allow more PTP
    def static_route(self,destination_ip:str,destination_prefix:str,next_hop:str,administrative_distance:str,ip_type:str):
        #IPV4
        if ip_type == "ipv4":
            if self.vendor == "Cisco":
                command = "ip route " + destination_ip + " " + destination_prefix + " " + next_hop +  " "  + administrative_distance
            if self.vendor == "cisco":
                command = "ip route " + destination_ip + " " + destination_prefix + " " + next_hop +  " "  + administrative_distance

        #IPV6
        elif ip_type  == "ipv6":
            if self.vendor == "cisco":
                print("Will DO!!!!!!!!!!!!!!!!!!!")


    #Using CDP and LLDP to find neighbours , you need to have cdp or lldp enabled on the int 
    def neighbours(self,cdp:bool,lldp:bool,detailed:bool):
        if self.vendor == "Cisco":

            print("")
        if self.vendor == "cisco":
            #Checking the boolean 
            if cdp == True and lldp == False:
                 #prefered_thing = "CDP"
                 if detailed == True:
                      command  = "en && show cdp neigh deta"
                 else:
                      command =  "en && show cdp nei"
            elif cdp == False and lldp == True:
                  #preffered_thing =  "LLDP"
                 if detailed == True:
                      command = "en && show lldp neigh det"
                 else:
                      command = "en && show lldp nei"
            elif cdp == True and lldp == True:
                 preffered_thing = "Both"
                 command1  = "show lldp neigh"
                 command2 = ""
            else:       
               print("!!!You have to select a Layer 2 Discovery Method...")           
        if self.vendor  == "juniper":
            cdp = False
            print("")
        if self.vendor == "Juniper":
            cdp = False
            print("")






#FTP SERVER
class FTP_SERVER():
    def __init__(self):
        pass



#TFTP SERVER
class TFTP_SERVER():
    def __init__(self):
        pass




#Switch LATER ON
class Switch():
    def __init__(self):
         pass