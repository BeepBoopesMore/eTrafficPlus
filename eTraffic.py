import paramiko
import json
import paramiko.client
import paramiko.ssh_exception
import requests
from time import sleep as wait 
import os
import socket
from socket import gaierror
# Doing yet just Juniper And Cisco
#TO DO:
#Dell
#Huawei
#The ones that work at Mr.Krabs
# I am not completely devoted to this but I WILL  finish it
#
#DONE/70% Router
#Cisco / 70%
#Juniper / 60% maybe?



class Router():
    def __init__(self,host:str,username:str,password:str,vendor:str):
        try:
             #Defining The Router
             self.vendor = vendor
             self.host = host
             self.username = username
             self.password = password
             #These are raw i need to beautify them !!!!!! TO DO BTW
             #Commands for Cisco , to use in others or strings unlike the show functions which you just use to see stuff and can't work around
             if vendor.lower() == "cisco":
               #Clock
                 client = paramiko.client.SSHClient()
                 client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                 client.connect(self.host, username=self.username, password=self.password)
                 _stdin, _stdout,_stderr = client.exec_command("enable && show clock detail")
                 raw = _stdout.read().decode()
                 self.clock = "".join(raw)
               #Hostname
                 client2 = paramiko.client.SSHClient()
                 client2.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                 client2.connect(self.host, username=self.username, password=self.password) 
                 _stdin, _stdout,_stderr = client.exec_command("enable && show running-config | include hostname")
                 raw2 = _stdout.read().decode()
                 self.hostname = "".join(raw2) 
               #Model
                 client3 = paramiko.client.SSHClient()
                 client3.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                 client3.connect(self.host, username=self.username, password=self.password) 
                 _stdin, _stdout,_stderr = client.exec_command("enable && show version | include Model")
                 raw3 = _stdout.read().decode()
                 self.model = "".join(raw3)
               #Version 
                 client4 = paramiko.client.SSHClient()
                 client4.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client4.connect(self.host,username=self.username,password=self.password)
                 _stdin, _stdout,_stderr = client.exec_command("enable && show version")
                 raw4 = _stdout.read().decode()
                 self.version = "".join(raw4)
               #Running Config
                 client5 = paramiko.client.SSHClient()
                 client5.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client5.connect(self.host,username=self.username,password=self.password)
                 _stdin, _stdout,_stderr = client.exec_command("enable && show running-config")
                 raw5 = _stdout.read().decode()
                 self.running_config = "".join(raw5)
               #Memory usage
                 client6 = paramiko.client.SSHClient()
                 client6.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client6.connect(self.host,username=self.username,password=self.password)
                 _stdin, _stdout,_stderr = client.exec_command("enable && show memory")
                 raw6 = _stdout.read().decode()
                 self.memory = "".join(raw6)
               #Arp Table
                 client7 = paramiko.client.SSHClient()
                 client7.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client7.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip arp")
                 raw7 = _stdout.read().decode()
                 self.arp_table = "".join(raw7)
               #License
                 client8 = paramiko.client.SSHClient()
                 client8.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client8.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show license all")
                 raw8 = _stdout.read().decode()
                 self.license = "".join(raw8)
               #Primary Routing Protocol
                 client9 = paramiko.client.SSHClient()
                 client9.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client9.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip protocols")
                 raw9 = _stdout.read().decode()
                 self.routing_protocol_used = "".join(raw9)
               #NAT Translations
                 client10 = paramiko.client.SSHClient()
                 client10.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client10.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip nat translations")
                 raw10 = _stdout.read().decode()
                 self.nat_translations = "".join(raw10)
                #CDP Neighbors Non-Detailed
                 client11 = paramiko.client.SSHClient()
                 client11.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client11.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show cdp neighbors")
                 raw11 = _stdout.read().decode()
                 self.cdp_neighbours = "".join(raw11)
               #LLDP Neighbors If Active
                 client12 = paramiko.client.SSHClient()
                 client12.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client12.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show lldp neighbors")
                 raw12 = _stdout.read().decode()
                 self.lldp_neighbours = "".join(raw12)
               #CDP Neighbors Detailed
                 client13 = paramiko.client.SSHClient()
                 client13.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client13.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show cdp neighbors detail")
                 raw13 = _stdout.read().decode()
                 self.cdp_neighbors_detailed = "".join(raw13)
               #LLDP Neighbors Detailed if Active
                 client14 = paramiko.client.SSHClient()
                 client14.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client14.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show lldp neighbors detail")
                 raw14 = _stdout.read().decode()
                 self.lldp_neighbours_detailed = "".join(raw14)
              #Ip Route Table IPV4  
                 client15 = paramiko.client.SSHClient()
                 client15.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client15.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip route")
                 raw15 = _stdout.read().decode()
                 self.ipv4_routes = "".join(raw15)
              #Ip Route Table IPV6  
                 client16 = paramiko.client.SSHClient()
                 client16.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client16.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ipv6 route")
                 raw16 = _stdout.read().decode()
                 self.ipv6_routes = "".join(raw16)
              #DHCP Bindings if the router acts as the server providing ips
                 client17 = paramiko.client.SSHClient()
                 client17.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client17.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip dhcp bindings")
                 raw17 = _stdout.read().decode()
                 self.dhcp_bindings  = "".join(raw17)
              #Startup config
                 client18 = paramiko.client.SSHClient()
                 client18.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client18.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip startup-config")
                 raw18 = _stdout.read().decode()
                 self.dhcp_bindings  = "".join(raw18)
              #Users
                 client19 = paramiko.client.SSHClient()
                 client19.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client19.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show users")
                 raw19 = _stdout.read().decode()
                 self.users_connected  = "".join(raw19)
              #Vlan info
                 client20 = paramiko.client.SSHClient()
                 client20.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client20.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show vlan brief")
                 raw20 = _stdout.read().decode()
                 self.users_connected  = "".join(raw20)
              #AAA info
                 client21 = paramiko.client.SSHClient()
                 client21.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client21.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show aaa")
                 raw21 = _stdout.read().decode()
                 self.users_connected  = "".join(raw21)
              #NTP Status
                 client22 = paramiko.client.SSHClient()
                 client22.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client22.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ntp status")
                 raw22 = _stdout.read().decode()
                 self.ntp_status  = "".join(raw22)
              #Cpu Utilization
                 client23 = paramiko.client.SSHClient()
                 client23.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client23.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show cpu")
                 raw23 = _stdout.read().decode()
                 self.cpu_utilization  = "".join(raw23)
              #Ospf Neighbors
                 client24 = paramiko.client.SSHClient()
                 client24.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client24.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip ospf neighbor")
                 raw24 = _stdout.read().decode()
                 self.ospf_neighbors  = "".join(raw24)       
              #Ospf Database
                 client25 = paramiko.client.SSHClient()
                 client25.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client25.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip ospf database")
                 raw25 = _stdout.read().decode()
                 self.ospf_database  = "".join(raw25)    
              #BGP Info
                 client26 = paramiko.client.SSHClient()
                 client26.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client26.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip bgp")
                 raw26 = _stdout.read().decode()
                 self.bgp_info  = "".join(raw26)
              #RIP Info
                 client27 = paramiko.client.SSHClient()
                 client27.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client27.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show ip rip")
                 raw27 = _stdout.read().decode()
                 self.rip_info  = "".join(raw27)
              #Memory Utilization
                 client28 = paramiko.client.SSHClient()
                 client28.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client28.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && show memory")
                 raw28 = _stdout.read().decode()
                 self.memory_use  = "".join(raw28)
              #Processes  
                 client29 = paramiko.client.SSHClient()
                 client29.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 client29.connect(self.host,username=self.username,password=self.password)
                 _stdin,_stdout,_stderr = client.exec_command("enable && processes")
                 raw29 = _stdout.read().decode()
                 self.processes  = "".join(raw29)

             
                 
                 
          
                

             else:
                  print("!!! This Vendor is not yet coded or not existent !!! ".upper())

     
 
        except  paramiko.ssh_exception.NoValidConnectionsError:
             d = "!!!!!! The connection doesn't exist or the host doesn't allow ssh connections.. !!!!!!!!".upper()
             print(d)
        except TimeoutError:
             print("!!! OOPS SOMETHING HAPPENED BUT MOST LIKELY THE HOST IS DOWN OR DOESN'T EXIST OR DOESN'T ACCEPT PORT 22 !!!")
        except UnicodeError:
             print("!!! rewrite the router info  , it is not valid you idiot !!!  ".upper())
        pass
      
    #Send a specific command ,curently just testing
    def send_command(self,command:str):
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        client.connect(self.host, username=self.username, password=self.password)
        _stdin, _stdout,_stderr = client.exec_command("cd")
        raw = _stdout.read().decode()
        #Turning Decoding Into String For Scraping 
        command_output = "".join(raw)
        print(command_output)
    #Show memory usage of the router
    def show_memory_usage(self):
         if self.vendor.lower() == "cisco":
              command = "enable && show memory"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         elif self.vendor.lower() == "juniper":
              command = "show system memory"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)

    #Show ARP table          
    def show_arp(self):
         if self.vendor.lower():
              command = "enable && show ip arp"
    #INTERFACES IPV4
    def show_ipv4_interfaces(self):
        if self.vendor.lower() == "cisco":
             command = "enable && show ip int brief"
             client = paramiko.client.SSHClient()
             client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
             client.connect(self.host, username=self.username, password=self.password)
             _stdin, _stdout,_stderr = client.exec_command(command)
             command_output = "".join(_stdout.read().decode())
             print(command_output)

        if self.vendor.lower() == "juniper":
             command =  "show interfaces terse"
             client = paramiko.client.SSHClient()
             client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
             client.connect(self.host, username=self.username, password=self.password)
             _stdin, _stdout,_stderr = client.exec_command(command)
             command_output = "".join(_stdout.read().decode())
             print(command_output)

    def set_hostname(self,hostname:str):
         if self.vendor.lower() == "cisco":
              command = "enable && configure terminal && hostname " + hostname + " && exit && write"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         elif self.vendor.lower() == "juniper":
              command = "configure && set system host-name " + hostname + " && commit"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
    #License 
    def license(self):
         if self.vendor == "cisco":
              command = "enable && show license all"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         if self.vendor == "Cisco":
              command = "enable && show license all"
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
        if self.vendor.lower() == "cisco":
          command = "en && show ipv6 interface brief"
          client = paramiko.client.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
          client.connect(self.host, username=self.username, password=self.password)
          _stdin, _stdout,_stderr = client.exec_command(command)
          command_output = "".join(_stdout.read().decode())
          print(command_output)
        if self.vendor.lower() == "juniper":
          command = "cli && show interfaces terse | match inet6"
          client = paramiko.client.SSHClient()
          client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
          client.connect(self.host, username=self.username, password=self.password)
          _stdin, _stdout,_stderr = client.exec_command(command)
          command_output = "".join(_stdout.read().decode())
          print(command_output)


    #Only on cisco !! Activating LLDP
    def activate_lldp(self,file_path:str):
         if self.vendor.lower() == "cisco":
              path = "../eTrafficApp/Router/lldp.json"
              with open(file_path,"r") as file:
                   data = json.load(file)
                   interfaces_receive = data["interfaces_receive"]
                   interfaces_transmit = data["interfaces_transmit"]
                   command_run_lldp = "enable && configure terminal && lldp run"
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command_run_lldp)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output)
                   wait(1.2)
                   for interface in interfaces_receive:
                        command = "enable && configure terminal && interface " + interface + " && lldp receive && exit && exit && write"
                        client = paramiko.client.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                        client.connect(self.host, username=self.username, password=self.password)
                        _stdin, _stdout,_stderr = client.exec_command(command)
                        command_output = "".join(_stdout.read().decode())
                        print(command_output)
                        wait(1.2)
                   for interface in interfaces_transmit:
                        command = "enable && configure terminal && interface " + interface + " && lldp transmit && exit && exit && write"
                        client = paramiko.client.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                        client.connect(self.host, username=self.username, password=self.password)
                        _stdin, _stdout,_stderr = client.exec_command(command)
                        command_output = "".join(_stdout.read().decode())
                        print(command_output)
         elif self.vendor.lower() == "juniper":
              print("!!!! Juniper already has lldp by default activated !!!! ".upper())
    def disable_lldp(self):
         if self.vendor.lower() == "cisco":
              command = "enable && configure terminal && no lldp run"

    #Create a dynamic_protocol on the Router
    def dynamic_protocol(self):
         with open("templatedynamic.json","r") as file:
              data = json.load(file)
              if self.vendor.lower() == "cisco":
                   command = "Will see "
              elif self.vendor.lower() =="juniper":
                   command = "will see"
    #Turning on an interface
    def turn_on_interfaces(self,interfaces:list):
     apendixes = ["g","f","s"]
     if self.vendor.lower() == "cisco":
          for item in interfaces:
               command = "enable && configure terminal && interface " + item + " && no shutdown && exit && exit && write"
               client = paramiko.client.SSHClient()
               client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
               client.connect(self.host, username=self.username, password=self.password)
               _stdin, _stdout,_stderr = client.exec_command(command)
               command_output = "".join(_stdout.read().decode())
               print(command_output)
               wait(1.2)
     elif self.vendor.lower() == "juniper":
          for item in interfaces :
               command = "configure && edit interfaces " + item  + " && delete disable && commit"
               client = paramiko.client.SSHClient()
               client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
               client.connect(self.host, username=self.username, password=self.password)
               _stdin, _stdout,_stderr = client.exec_command(command)
               command_output = "".join(_stdout.read().decode())
               print(command_output)

     #Disable interfaces
    def disable_interfaces(self,interfaces:list):
         if self.vendor.lower() == "cisco":
              for item in interfaces:
                   command = "enable && configure terminal && " + item + " && shutdown && exit && exit && write"
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output)

         elif self.vendor.lower() == "juniper":
              for item in interfaces:
                   command = "configure && edit interfaces " + item + " && set disable && commit"
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output)
    #Configure Ipv4 the default way obv and ipv6 using EUI-64
    def configure_interfaces(self,template_path:str):
         if self.vendor.lower() == "cisco":
              with open(template_path,"r") as file:
                   if self.vendor.lower() == "cisco":
                        data = json.load(file)
                        so = data["interfaces"]
                        for datas in so :
                             interface = datas["interface"]
                             ip = datas["ip_address"]
                             subnet_mask = datas["subnet_mask"]
                             list_subnets = ["0.0.0.0","128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0","248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0","255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0","255.255.128.0","255.255.192.0","255.255.224.0","255.255.240.0","255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0","255.255.255.128","255.255.255.192","255.255.255.224","255.255.255.240","255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255"]
                             interface_type = datas["interface_type"]
                             if interface_type == "ipv6":
                                  command = "enable && configure terminal && interface " + interface + " && ipv6 address " + ip + " eui-64" + " && no shutdown && exit && exit && write"
                                  client = paramiko.client.SSHClient()
                                  client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                                  client.connect(self.host, username=self.username, password=self.password)
                                  _stdin, _stdout,_stderr = client.exec_command(command)
                                  command_output = "".join(_stdout.read().decode())
                                  print(command_output)
                             elif interface_type == "ipv4":
                                  if subnet_mask not in list_subnets:
                                      print("!!! "  + subnet_mask +  " is not a valid subnet mask !!!! ".upper())
                                  else:
                                       command = "enable && configure terminal && interface " + interface + " && ip address " + ip + " " + subnet_mask + " && no shutdown && exit && exit && write "
                                       client = paramiko.client.SSHClient()
                                       client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                                       client.connect(self.host, username=self.username, password=self.password)
                                       _stdin, _stdout,_stderr = client.exec_command(command)
                                       command_output = "".join(_stdout.read().decode())
                                       print(command_output)
                             else:
                                  print("!!! " + interface_type + " is not an ipv6 or ipv4 so please mention which..  !!! ")
                   elif self.vendor.lower() == "juniper":
                        data = json.load(file)
                        so = data["interfaces"]
                        for datas in so:
                             interface = datas["interface"]
                             ip = datas["ip_address"]
                             subnet_mask = datas["subnet_mask"]
                             list_subnets = ["0.0.0.0","128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0","248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0","255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0","255.255.128.0","255.255.192.0","255.255.224.0","255.255.240.0","255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0","255.255.255.128","255.255.255.192","255.255.255.224","255.255.255.240","255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255"]
                             interface_type = datas["interface_type"]
                             if interface_type == "ipv6":
                                  command = "configure  && edit interfaces " + interface + " && set unit 0 family inet6 address " + ip + " && set unit 0 family inet6 disable && commit " 
                                  client = paramiko.client.SSHClient()
                                  client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                                  client.connect(self.host, username=self.username, password=self.password)
                                  _stdin, _stdout,_stderr = client.exec_command(command)
                                  command_output = "".join(_stdout.read().decode())
                                  print(command_output)
                             elif interface_type == "ipv4":
                                  #Done the prefixes YEYE!!
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
                                  if subnet_mask not in list_subnets:
                                        print("!!! "  + subnet_mask +  " is not a valid subnet mask !!!! ".upper())
                                  else:
                                       if subnet_mask == prefix_0:
                                            prefix = "/0"
                                       elif subnet_mask == prefix_1:
                                            prefix = "/1"
                                       elif subnet_mask == prefix_2:
                                            prefix = "/2"
                                       elif subnet_mask == prefix_3:
                                            prefix = "/3"
                                       elif subnet_mask == prefix_4:
                                            prefix = "/4"
                                       elif subnet_mask == prefix_5:
                                            prefix = "/5"
                                       elif subnet_mask == prefix_6:
                                            prefix = "/6"
                                       elif subnet_mask == prefix_7:
                                            prefix = "/7"
                                       elif subnet_mask == prefix_8:
                                            prefix = "/8"
                                       elif subnet_mask == prefix_9:
                                            prefix = "/9"
                                       elif subnet_mask == prefix_10:
                                            prefix = "/10"
                                       elif subnet_mask == prefix_11:
                                            prefix = "/11"
                                       elif subnet_mask == prefix_12:
                                            prefix = "/12"
                                       elif subnet_mask == prefix_13:
                                            prefix = "/13"
                                       elif subnet_mask == prefix_14:
                                            prefix = "/14"
                                       elif subnet_mask == prefix_15:
                                            prefix = "/15"
                                       elif subnet_mask == prefix_16:
                                            prefix = "/16"
                                       elif subnet_mask == prefix_17:
                                            prefix = "/17"
                                       elif subnet_mask == prefix_18:
                                            prefix = "/18"
                                       elif subnet_mask == prefix_19:
                                            prefix = "/19"
                                       elif subnet_mask == prefix_20:
                                            prefix = "/20"
                                       elif subnet_mask == prefix_21:
                                            prefix = "/21"
                                       elif subnet_mask == prefix_22:
                                            prefix = "/22"
                                       elif subnet_mask == prefix_23:
                                            prefix = "/23"
                                       elif subnet_mask == prefix_24:
                                            prefix = "/24"
                                       elif subnet_mask == prefix_25:
                                            prefix = "/25"
                                       elif subnet_mask == prefix_26:
                                            prefix = "/26"
                                       elif subnet_mask == prefix_27:
                                            prefix = "/27"
                                       elif subnet_mask == prefix_28:
                                            prefix = "/28"
                                       elif subnet_mask == prefix_29:
                                            prefix = "/29"
                                       elif subnet_mask == prefix_30:
                                            prefix = "/30"
                                       elif subnet_mask == prefix_31:
                                            prefix = "/31"
                                       elif subnet_mask == prefix_32:
                                            prefix = "/32"
                                       ip_finished = ip + prefix
                                       command = "configure && set interfaces " + interface  +  " unit 0 family inet address " +  ip_finished + " && set unit 0 family inet disable  && commit"
                                       client = paramiko.client.SSHClient()
                                       client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                                       client.connect(self.host, username=self.username, password=self.password)
                                       _stdin, _stdout,_stderr = client.exec_command(command)
                                       command_output = "".join(_stdout.read().decode())
                                       print(command_output)
                                                       
                             else:
                                  print("!!! " + interface_type + " is not an ipv6 or ipv4 so please mention which..  !!! ")
                                  

    #Configuring sub interfaces                   
    def configure_sub_interfaces(self,file_path:str):
         try:
              #Prefixes again yey!!
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
              path = "../eTrafficApp/Router/config_subinterfaces.json"
              with open(file_path,"r") as file:
                   data = json.load(file)   
                   interfaces = data["interfaces"]  
                   subnet_mask_used = item["subnet_mask"]
                   if subnet_mask_used == prefix_0:
                        prefix = 0 
                   elif subnet_mask_used == prefix_1:
                        prefix = 1 
                   elif subnet_mask_used == prefix_2:
                        prefix = 2
                   elif subnet_mask_used == prefix_3:
                         prefix = 3 
                   elif subnet_mask_used == prefix_4:
                         prefix = 4 
                   elif subnet_mask_used == prefix_5:
                         prefix = 5 
                   elif subnet_mask_used == prefix_6:
                         prefix = 6 
                   elif subnet_mask_used == prefix_7:
                         prefix = 7 
                   elif subnet_mask_used == prefix_8:
                        prefix = 8
                   elif subnet_mask_used == prefix_9:
                        prefix = 9 
                   elif subnet_mask_used == prefix_10:
                        prefix = 10 
                   elif subnet_mask_used == prefix_11:
                         prefix = 11 
                   elif subnet_mask_used == prefix_12:
                         prefix = 12
                   elif subnet_mask_used == prefix_13:
                         prefix = 13 
                   elif subnet_mask_used == prefix_14:
                         prefix = 14 
                   elif subnet_mask_used == prefix_15:
                         prefix = 15 
                   elif subnet_mask_used == prefix_16:
                        prefix = 16
                   elif subnet_mask_used == prefix_17:
                        prefix = 17 
                   elif subnet_mask_used == prefix_18:
                        prefix = 18 
                   elif subnet_mask_used == prefix_19:
                         prefix = 19 
                   elif subnet_mask_used == prefix_20:
                         prefix = 20 
                   elif subnet_mask_used == prefix_21:
                         prefix = 21 
                   elif subnet_mask_used == prefix_22:
                         prefix = 22 
                   elif subnet_mask_used == prefix_23:
                         prefix = 23 
                   elif subnet_mask_used == prefix_24:
                        prefix = 24
                   elif subnet_mask_used == prefix_25:
                        prefix = 25 
                   elif subnet_mask_used == prefix_26:
                        prefix = 26
                   elif subnet_mask_used == prefix_27:
                         prefix = 27 
                   elif subnet_mask_used == prefix_28:
                         prefix = 28 
                   elif subnet_mask_used == prefix_29:
                         prefix = 29 
                   elif subnet_mask_used == prefix_30:
                         prefix = 30 
                   elif subnet_mask_used == prefix_31:
                         prefix = 31 
                   elif subnet_mask_used == prefix_32:
                        prefix = 32
                   else:
                        print("PLEASE USE A CORRECT SUBNET MASK")
                   
                   #Cisco       
                   if self.vendor.lower() == "cisco":
                        for item in interfaces:
                         main_interface_used = item["main_interface"]
                         sub_interface = item["sub_interface"]
                         sub_interface_ip =  item["sub_interface_ip"]
                         subnet_mask_used = item["subnet_mask"]
                         vlan = item["vlan"] 
                         native_vlan = item["native_vlan"]
                         #Enabling the interface if is shutdown just in case
                         command1  = "enable && configure terminal && interface " + main_interface_used + " && no shutdown && exit && exit && write"
                         client = paramiko.client.SSHClient()
                         client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                         client.connect(self.host, username=self.username, password=self.password)
                         _stdin, _stdout,_stderr = client.exec_command(command1)
                         command_output = "".join(_stdout.read().decode())
                         print(command_output)     
                         #Checking if they select native vlan
                         if native_vlan == "None":
                              #Main one ig
                              command = "enable && configure terminal && interface "   + main_interface_used + sub_interface + " && encapsulation dot1Q " + int(vlan) + " && ip address " + sub_interface_ip + " " + subnet_mask_used  + " && no shutdown && exit && exit && write"
                              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                              client.connect(self.host, username=self.username, password=self.password)
                              _stdin, _stdout,_stderr = client.exec_command(command)
                              command_output = "".join(_stdout.read().decode())
                              print(command_output)     
                         if len(native_vlan) >= 1 :
                              command = "enable && configure terminal && interface "   + main_interface_used + sub_interface + " && encapsulation dot1Q " + int(vlan) + "native" + " && ip address " + sub_interface_ip + " " + subnet_mask_used  + " && no shutdown && exit && exit && write"
                              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                              client.connect(self.host, username=self.username, password=self.password)
                              _stdin, _stdout,_stderr = client.exec_command(command)
                              command_output = "".join(_stdout.read().decode())
                              print(command_output)
                         else:
                              print("Please specify a value correctly")
                   #Juniper
                   if self.vendor.lower() == "juniper":
                        
                        for item in interfaces: 
                             main_interface_used = item["main_interface"]
                             sub_interface = item["sub_interface"]
                             sub_interface_ip =  item["sub_interface_ip"]
                             subnet_mask_used = item["subnet_mask"]
                             vlan = item["vlan"]
                             native_vlan = "".join(item["native_vlan"])
                             sub_interface_done = sub_interface.replace(".","")
                             ip_address_done = sub_interface_ip+prefix
                             #Enabling the interface if it is shutdown just in case aswell
                             command_interface_just_in_case = "configure && set interfaces " + sub_interface_done + " disable && commit " 
                             client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                             client.connect(self.host, username=self.username, password=self.password)
                             _stdin, _stdout,_stderr = client.exec_command(command)
                             command_output1 = "".join(_stdout.read().decode())
                             print(command_output1)

     
                             #Checking if they select native vlan
                             if native_vlan == "None":
                                  command = "configure && set interfaces " + main_interface_used + " unit " + sub_interface_done + " vlan-id " + vlan + " && commit"
                                  command2 = "configure && set interfaces " + main_interface_used + " unit " + sub_interface_done + " family inet address "  + ip_address_done + " && commit "
                                  client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                                  client.connect(self.host, username=self.username, password=self.password)
                                  _stdin, _stdout,_stderr = client.exec_command(command)
                                  command_output1 = "".join(_stdout.read().decode())
                                  print(command_output1)
                                  client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                                  client.connect(self.host, username=self.username, password=self.password)
                                  _stdin, _stdout,_stderr = client.exec_command(command2)
                                  command_output2 = "".join(_stdout.read().decode())
                                  print(command_output2)

                             elif len(native_vlan) >= 1:    
                                  command = "configure && set interfaces " + main_interface_used + " unit 0 native-vlan-id " + native_vlan + " && commit " 
                                  command2 = "configure && set interfaces " + main_interface_used + " unit " + sub_interface_done + " family inet address "  + ip_address_done + " && commit "
                                  client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                                  client.connect(self.host, username=self.username, password=self.password)
                                  _stdin, _stdout,_stderr = client.exec_command(command)
                                  command_output1 = "".join(_stdout.read().decode())
                                  print(command_output1)
                                  client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                                  client.connect(self.host, username=self.username, password=self.password)
                                  _stdin, _stdout,_stderr = client.exec_command(command2)
                                  command_output2 = "".join(_stdout.read().decode())
                                  print(command_output2)
                             else:
                                  print("Please mention eiter None or a native vlan number corresponding".upper())
                             #Checking if they select native vlan
                                  
         except TypeError: 
              print("!!! PLEASE USE THE CORRECT TEMPLATE FORMAT !!!")
                         
                        
              
   
      #Setup an NTP server , you can either choose to become one or get time from one 
    def setup_NTP(self,server:str,become_host:bool):
         if self.vendor.lower() == "cisco":
              if become_host == True:
                   command = "enable && configure terminal && ntp master && ntp update-calendar && exit && wr  " 
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output)
              else:
                   command = "enable && configure terminal && ntp " + server  + " && ntp update-calendar && exit && wr"
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output)
         if self.vendor.lower() == "juniper":
              if become_host == True:
                   command = "configure &&  set system ntp master && commit"
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output)
              else:
                   command = "configure && set system ntp server " + server  + " && commit"
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output) 
                   
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
    

    


    def show_routing_protocol(self):
        if self.vendor == "Cisco":
           client = paramiko.client.SSHClient()
           client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
           client.connect(self.host, username=self.username, password=self.password)
           _stdin, _stdout,_stderr = client.exec_command("enable && show ip protocols")
           command_output = "".join(_stdout.read().decode())
           print(command_output)
        if self.vendor == "cisco":
           client = paramiko.client.SSHClient()
           client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
           client.connect(self.host, username=self.username, password=self.password)
           _stdin, _stdout,_stderr = client.exec_command("enable && show ip protocols")
           command_output = "".join(_stdout.read().decode())
           print(command_output)
        if self.vendor == "Juniper":
            command = 'show configuration protocols'
        
        if self.vendor == "juniper":
             command = 'show configuration protocols'

    

    #Make multiple changes for multiple routers based on a template
    def make_changes(self):
        with open("template.json","r") as file:
             l = json.load(file)
      #!!!!
    
    def static_route_ipv6(self,destination_ip:str,next_hop:str,admistrative_distance:int):
         if self.vendor.lower() == "cisco":
              command = "enable && configure terminal && ipv6 route " + destination_ip + " " + next_hop + " " + str(admistrative_distance) + " && exit && write"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())  
              print(command_output)
         elif self.vendor.lower() == "juniper":
              command = "configure && set routing-options static route " + destination_ip + " next-hop " + next + " preference " + str(admistrative_distance) + " && commit"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())  
              print(command_output)
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
                 subnet_mask = prefix_27
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
            command = "enable && configure terminal  && ip route " + destination_ip + " " + subnet_mask + " " + next_hop +  " "  + administrative_distance + " && exit && write"
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
            command = "enable && configure terminal  && ip route " + destination_ip + " " + subnet_mask + " " + next_hop +  " "  + administrative_distance + " && exit && write"
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
        if self.vendor == "Juniper":
            #reference_command = "set qualified-next-hop 192.168.2.2 preference 25"
            command  = "configure && set routing-options static route  " + destination_ip +str(destination_prefix) + " next-hop " + next_hop + " metric " +  administrative_distance + " && commit" 
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
        if self.vendor == "juniper":
            command = "configure && set routing-options static route  " + destination_ip +str(destination_prefix) + " next-hop " + next_hop + " metric " +  administrative_distance  + " && commit"
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
              command = "en && show ip route "
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         if self.vendor == "Juniper":
              command = "show route ipv4"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         if self.vendor == "juniper":
              command = "show route ipv4"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
    #Showing startup_config
    def show_startup_config(self):
         if self.vendor.lower() == "cisco":
              command =  "enable && show startup-config "
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
         elif self.vendor.lower() == "juniper":
              command = "cli && show configuration"
              client = paramiko.client.SSHClient()
              client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
              client.connect(self.host, username=self.username, password=self.password)
              _stdin, _stdout,_stderr = client.exec_command(command)
              command_output = "".join(_stdout.read().decode())
              print(command_output)
     #Configure NAT
    def NAT(self,inside_interface:str,outside_interface:str,pool_name:str,pool_start_ip:str,pool_end_ip:str,netmask:str,standard_access_list_number:int,access_list_syntax:str):
         #Making the NAT for Cisco
         if self.vendor.lower() == "cisco":
              if standard_access_list_number <= 99:
                   #Defining the commands for the NAT configuration cisco only
                   command_first = "enable && configure terminal && interface " + inside_interface + " && ip nat inside && exit && interface " + outside_interface + " && ip nat outside && exit && write"
                   command_second = "en && configure terminal &&  access list " +  standard_access_list_number + " " + access_list_syntax + " && exit && write"
                   command_third = "enable && configure terminal && ip nat pool " + pool_name + " " + pool_start_ip + " " + pool_end_ip + " " + netmask + " && ip nat inside source list  " + standard_access_list_number + " pool " + pool_name + " && exit && write"
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command_first)
                   command_output_1 = "".join(_stdout.read().decode())
                   print(command_output_1)
                   wait(1)
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command_second)
                   command_output_2 = "".join(_stdout.read().decode())
                   print(command_output_2)
                   wait(1)
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command_third)
                   command_output_3 = "".join(_stdout.read().decode())
                   print(command_output_3)
              else:
                   message = "!!! Please use a standard access list number !!! ".upper()
                   print(message) 
         #Making the NAT for Juniper
         if self.vendor.lower() == "juniper":
              print("We don't got NAT for this yet..")
     
     #Create an access list
    def access_list(self,access_list_number:int,syntax:str):
         if self.vendor.lower() == "cisco":
              if access_list_number <= 99 and access_list_number > 0 :
                   list = "Standard"
              elif access_list_number >= 1300 and access_list_number <= 1999 :
                   list = "Standard"
              elif access_list_number > 99 and access_list_number <= 199:
                   list = "Extended"
              elif access_list_number  >= 2000 and access_list_number <= 2699:
                   list = "Extended"
              else:
                   print("!!!!! Not a valid list !!!".upper())
              
              if list == "Standard":
                   command = "enable && configure terminal && access-list " + str(access_list_number) + " " + syntax
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output)
              elif list == "Extended":
                   command = "enable && configure terminal && access-list" + str(access_list_number) + " " + syntax
                   client = paramiko.client.SSHClient()
                   client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                   client.connect(self.host, username=self.username, password=self.password)
                   _stdin, _stdout,_stderr = client.exec_command(command)
                   command_output = "".join(_stdout.read().decode())
                   print(command_output)


               
          
         elif self.vendor.lower() == "juniper":
              print("do sum")

    #Showing translations for NAT and clearing them if choice
    def show_nat_translations(self,clear_translations:bool):
     if self.vendor.lower() == "cisco":
          if clear_translations == True:
               command = "enable && clear ip nat translations * "
          else:
               command = "enable && show ip nat translations"

     elif self.vendor.lower() == "juniper":
          if clear_translations == True:
               command = "cli && clear security nat translation"
               client = paramiko.client.SSHClient()
               client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
               client.connect(self.host, username=self.username, password=self.password)
               _stdin, _stdout,_stderr = client.exec_command(command)
               command_output = "".join(_stdout.read().decode())
               print(command_output)
          else:
               command = "cli && show security nat source translation"
               client = paramiko.client.SSHClient()
               client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
               client.connect(self.host, username=self.username, password=self.password)
               _stdin, _stdout,_stderr = client.exec_command(command)
               command_output = "".join(_stdout.read().decode())
               print(command_output)


    #Using CDP and LLDP to find neighbours , you need to have cdp or lldp enabled on the int 
    def neighbours(self,cdp:bool,lldp:bool,detailed:bool):
        #Cisco Routers
        if self.vendor == "Cisco":
            if cdp == True and lldp == False:
                 #prefered_thing = "CDP"
                 if detailed == True:
                      command  = "enable && show cdp neighbors detail"
                      client = paramiko.client.SSHClient()
                      client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                      client.connect(self.host, username=self.username, password=self.password)
                      _stdin, _stdout,_stderr = client.exec_command(command)
                      command_output = "".join(_stdout.read().decode())
                      print(command_output)
                 else:
                      command =  "enable && show cdp neighbors"
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
        elif self.vendor == "cisco":
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
        elif self.vendor  == "juniper": 
            command =  "show lldp neigh"
            cdp = False
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
            
        elif self.vendor == "Juniper":
            command =  "show lldp neigh"
            cdp = False
            cdp = False
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
            client.connect(self.host, username=self.username, password=self.password)
            _stdin, _stdout,_stderr = client.exec_command(command)
            command_output = "".join(_stdout.read().decode())
            print(command_output)
      
      



#Parse the fuckin Router here , and do everything configs and shit but with DHCP!!! yeeeyeyeeyye
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
    
    #def port_channel(self):
         #vendor2 = self.vendor.lower
         #with open("portchannelsetting.json","r") as portchannel:
              #info = json.load(portchannel)
              #interfaces = info["Interfaces"]
              #port_id = info["PORT-ID"]
              #protocol  = info["Channel-Protocol"]
              #if vendor2 == "cisco":
                   #if protocol == "LACP":
                        #command = "en && conf t && int " + item + " && channel-group " + port_id + " active" + " && ex && ex && wr"
                   #for item in interfaces:
                        #client = paramiko.client.SSHClient()
                        #client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
                        #client.connect(self.host, username=self.username, password=self.password)
                       # _stdin, _stdout,_stderr = client.exec_command(command + item + " && channel-group " + port_id)
                        #command_output = "".join(_stdout.read().decode())
                        #print(command_output)

