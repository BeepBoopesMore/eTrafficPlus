import paramiko
import json
import time 
import requests
from time import sleep as wait 

# Doing yet just Juniper And Cisco
#To Do:
#TP_LINK
#Huawei
#Private Companies (The Secret Guys) # Or the ones that work at Mr.Krabs
#
#
#
#
#



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
    def license(self):
         if self.vendor == "cisco":
              command = "en && show license all"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         if self.vendor == "Cisco":
              command = "en && show license all"
              command = "en && show license all"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         if self.vendor == "Juniper":
              command = "show system license"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         if self.vendor == "juniper":
              command = "show system license "
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         


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
    def make_changes(self):
        with open("template.json","r") as file:
             l = json.load(file)
      #!!!!
    
   
    #!!!!!Tomorrow
    #Static Route Maker IPV4
    #In the future allow more PTP
    def static_route_ipv4(self,destination_ip:str,destination_prefix:int,next_hop:str,administrative_distance:int,):
        #Transforming the subnetmasks into prefixes in a lazy way
        prefix_0 = "0.0.0.0"
        prefix_1 = "128.0.0.0"
        prefix_2 = "192.0.0.0"
        prefix_3 = "224.0.0.0"
        prefix_4 = "240.0.0.0"
        prefix_5 = "248.0.0.0"
        prefix_6 = "252.0.0.0"
        prefix_7 = "254.0.0.0"
        prefix_8 = "255.0.0.0"
        prefix_9 = "255.128.0.0"
        prefix_10 = "255.192.0.0"
        prefix_11 = "255.224.0.0"
        prefix_12 = "255.240.0.0"
        prefix_13 = "255.248.0.0"
        prefix_14 = "255.252.0.0"
        prefix_15 = "255.254.0.0"
        prefix_16 = "255.255.0.0"
        prefix_17 = "255.255.128.0"
        prefix_18 = "255.255.192.0"
        prefix_19  = "255.255.224.0"
        prefix_20  = "255.255.240.0"
        prefix_21  = "255.255.248.0"
        prefix_22 = "255.255.252.0"
        prefix_23 = "255.255.254.0"
        prefix_24 = "255.255.255.0"
        prefix_25 = "255.255.255.128"
        prefix_26 = "255.255.255.192"
        prefix_27 = "255.255.255.224"
        prefix_28 = "255.255.255.240"
        prefix_29 = "255.255.255.248"
        prefix_30 = "255.255.255.252"
        prefix_31 = "255.255.255.254"
        prefix_32 = "255.255.255.255"
        final_command = ""
        if self.vendor == "Cisco":
            if destination_prefix == 0:
                subnet_mask = prefix_0
            elif destination_prefix == 1:
                subnet_mask = prefix_1 
            elif destination_prefix == 2:
                subnet_mask = prefix_2
            elif destination_prefix == 3:
                subnet_mask = prefix_3
            elif destination_prefix == 4:
                subnet_mask = prefix_4
            elif destination_prefix == 5:
                subnet_mask = prefix_5
            elif destination_prefix == 6:
                subnet_mask = prefix_6
            elif destination_prefix == 7:
                subnet_mask = prefix_7
            elif destination_prefix == 8:
                subnet_mask = prefix_8
            elif destination_prefix == 9:
                subnet_mask = prefix_9
            elif destination_prefix == 10:
                subnet_mask = prefix_10
            elif destination_prefix  == 11:
                subnet_mask = prefix_11
            elif destination_prefix == 12:
                subnet_mask = prefix_12
            elif destination_prefix == 13:
                 subnet_mask = prefix_13
            elif destination_prefix == 14:
                 subnet_mask = prefix_14 
            elif destination_prefix == 15:
                 subnet_mask = prefix_15
            elif destination_prefix == 16:
                 subnet_mask = prefix_16
            elif destination_prefix == 17:
                 subnet_mask = prefix_17
            elif destination_prefix == 18:
                 subnet_mask = prefix_18
            elif destination_prefix == 19:
                 subnet_mask = prefix_19
            elif destination_prefix == 20:
                 subnet_mask = prefix_20
            elif destination_prefix == 21:
                 subnet_mask = prefix_21
            elif destination_prefix == 22:
                 subnet_mask = prefix_22
            elif destination_prefix == 23:
                 subnet_mask = prefix_23
            elif destination_prefix == 24:
                 subnet_mask = prefix_24
            elif destination_prefix == 25:
                 subnet_mask = prefix_25
            elif destination_prefix == 26:
                 subnet_mask = prefix_26
            elif destination_prefix == 27:
                 subnet_mask = prefix_28
            elif destination_prefix == 28:
                 subnet_mask = prefix_28
            elif destination_prefix == 29:
                subnet_mask = prefix_29
            elif destination_prefix == 30:
                subnet_mask = prefix_30
            elif destination_prefix == 31:
                subnet_mask = prefix_31
            elif destination_prefix == 32:
                subnet_mask = prefix_32
            command = "en && conf t  && ip route " + destination_ip + " " + subnet_mask + " " + next_hop +  " "  + administrative_distance + " && exit && write"
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
        if self.vendor == "cisco":
            if destination_prefix == 0:
                subnet_mask = prefix_0
            elif destination_prefix == 1:
                subnet_mask = prefix_1 
            elif destination_prefix == 2:
                subnet_mask = prefix_2
            elif destination_prefix == 3:
                subnet_mask = prefix_3
            elif destination_prefix == 4:
                subnet_mask = prefix_4
            elif destination_prefix == 5:
                subnet_mask = prefix_5
            elif destination_prefix == 6:
                subnet_mask = prefix_6
            elif destination_prefix == 7:
                subnet_mask = prefix_7
            elif destination_prefix == 8:
                subnet_mask = prefix_8
            elif destination_prefix == 9:
                subnet_mask = prefix_9
            elif destination_prefix == 10:
                subnet_mask = prefix_10
            elif destination_prefix  == 11:
                subnet_mask = prefix_11
            elif destination_prefix == 12:
                subnet_mask = prefix_12
            elif destination_prefix == 13:
                 subnet_mask = prefix_13
            elif destination_prefix == 14:
                 subnet_mask = prefix_14 
            elif destination_prefix == 15:
                 subnet_mask = prefix_15
            elif destination_prefix == 16:
                 subnet_mask = prefix_16
            elif destination_prefix == 17:
                 subnet_mask = prefix_17
            elif destination_prefix == 18:
                 subnet_mask = prefix_18
            elif destination_prefix == 19:
                 subnet_mask = prefix_19
            elif destination_prefix == 20:
                 subnet_mask = prefix_20
            elif destination_prefix == 21:
                 subnet_mask = prefix_21
            elif destination_prefix == 22:
                 subnet_mask = prefix_22
            elif destination_prefix == 23:
                 subnet_mask = prefix_23
            elif destination_prefix == 24:
                 subnet_mask = prefix_24
            elif destination_prefix == 25:
                 subnet_mask = prefix_25
            elif destination_prefix == 26:
                 subnet_mask = prefix_26
            elif destination_prefix == 27:
                 subnet_mask = prefix_28
            elif destination_prefix == 28:
                 subnet_mask = prefix_28
            elif destination_prefix == 29:
                subnet_mask = prefix_29
            elif destination_prefix == 30:
                subnet_mask = prefix_30
            elif destination_prefix == 31:
                subnet_mask = prefix_31
            elif destination_prefix == 32:
                subnet_mask = prefix_32
            command = "en && conf && ip route " + destination_ip + " " + subnet_mask + " " + next_hop +  " "  + administrative_distance +  " && exit && write  "
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
        if self.vendor == "Juniper":

            #reference_command = "set qualified-next-hop 192.168.2.2 preference 25"
            command  = "conf && set routing-options static route  " + destination_ip +str(destination_prefix) + " next-hop " + next_hop + " metric " +  administrative_distance 
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
        if self.vendor == "juniper":
            command = "conf && set routing-options static route  " + destination_ip +str(destination_prefix) + " next-hop " + next_hop + " metric " +  administrative_distance 
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
    #Show ip table for ipv4
    def show_ip_route_table_ipv4(self):
         if self.vendor == "Cisco":
              command = "en && show ip route "
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         if self.vendor == "cisco":
              command = "en and && show ip route"
              command = "en && show ip route "
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         if self.vendor == "Juniper":
              command = ""

    #Using CDP and LLDP to find neighbours , you need to have cdp or lldp enabled on the int 
    def neighbours(self,cdp:bool,lldp:bool,detailed:bool):
        #Cisco Routers
        if self.vendor == "Cisco":
            if cdp == True and lldp == False:
                 #prefered_thing = "CDP"
                 if detailed == True:
                      command  = "en && show cdp neigh deta"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
                 else:
                      command =  "en && show cdp nei"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
            elif cdp == False and lldp == True:
                  #preffered_thing =  "LLDP"
                 if detailed == True:
                      command = "en && show lldp neigh det"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
                 else:
                      command = "en && show lldp nei"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
            elif cdp == True and lldp == True:
                 #preffered_thing = "Both"
                 command1  = "en && show lldp neigh"
                 command2 = "en && show cdp neigh "
                 client = paramiko.client.SSHClient()
                 client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                 client.connect(self.host, username=self.username, password=self.password)
                 _stdin, _stdout,_stderr = client.exec_command(command1)
                 command_output = "".join(_stdout.read().decode())
                 print(command_output)
                 wait(1)
                 client  = paramiko.client.SSHClient()
                 client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                 client.connect(self.host, username=self.username, password=self.password)
                 _stdin, _stdout,_stderr = client.exec_command(command2)
                 command_output = "".join(_stdout.read().decode())
                 print(command_output)
                 


            else:       
               print("!!!You have to select a Layer 2 Discovery Method...")

            print("")
        if self.vendor == "cisco":
            #Checking the boolean 
            if cdp == True and lldp == False:
                 #prefered_thing = "CDP"
                 if detailed == True:
                      command  = "en && show cdp neigh deta"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
                 else:
                      command =  "en && show cdp nei"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
            elif cdp == False and lldp == True:
                  #preffered_thing =  "LLDP"
                 if detailed == True:
                      command = "en && show lldp neigh det"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
                 else:
                      command = "en && show lldp nei"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
            elif cdp == True and lldp == True:
                 #preffered_thing = "Both"
                 command1  = "en && show lldp neigh"
                 command2 = "en && show cdp neigh "
                 client = paramiko.client.SSHClient()
                 client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                 client.connect(self.host, username=self.username, password=self.password)
                 _stdin, _stdout,_stderr = client.exec_command(command1)
                 command_output = "".join(_stdout.read().decode())
                 print(command_output)
                 wait(1)
                 client  = paramiko.client.SSHClient()
                 client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                 client.connect(self.host, username=self.username, password=self.password)
                 _stdin, _stdout,_stderr = client.exec_command(command2)
                 command_output = "".join(_stdout.read().decode())
                 print(command_output)
                 

            else:       
               print("!!!You have to select a Layer 2 Discovery Method...")   

        #Juniper Routers    
        if self.vendor  == "juniper": 
            command =  "show lldp neigh"
            cdp = False
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
            
        if self.vendor == "Juniper":
            command =  "show lldp neigh"
            cdp = False
            cdp = False
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)







class DHCP_Server():
     def __init__(self,ip_address,):
          self.ip_adress = ip_address
          pass 
     



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
