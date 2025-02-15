Uses SSH to connect to a device , uses templates in json and extractes the data from the json file to , uses those in the commands later on for configuration.


Doing this into a bot ?
Database of Servers?
Multiple Devices Not Just ONe
List of Routers/Switches to connect to 



# Version



Option: 

# Important use netmiko (prob)

-https://pypi.org/project/netmiko/



SSH 1.99


# Version of OS that is running on the switch/router
So cisco , etc...
If the vendor is cisco, the commands are gonna be like this :
If the vendor is bla bla , the commands are gonna be like this :
Support as many vendors !!!
Also FTP Server 
So when u ssh for the first time the app checks the vendor , and uses the templates with that vendor.




Paramiko






# Ansible but better


- (Commands basically)
-https://github.com/paramiko/paramiko (Used for connecting ssh)



 
# Use Post Api to maybe use the json template ? and then when u send that api with the headers u do the config ??????  -- Use GO ??




# Samples



import paramiko

def key_based_connect(server):
host = "192.0.2.0"
special_account = "user1"
pkey = paramiko.RSAKey.from_private_key_file("./id_rsa")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=special_account, pkey=pkey)
return client

def examine_last(server, connection):
command = "sudo last"
expected = ["user1", "reboot", "root", "sys-admin"]
stdin, stdout, stderr = connection.exec_command(command)
lines = stdout.read().decode()
connection.close()
for line in lines.split("\n"):
if line.startswith("wtmp begins"):
break
parts = line.split()
if parts:
account = parts[0]
if account not in expected:
print(f"Entry '{line}' is a surprise on {server}.")

def main():
server_list = ["worker1", "worker2", "worker3"]
for server in server_list:
connection = key_based_connect(server)
examine_last(server, connection)

main()

# Keys up 




import paramiko

# Update with your server's information
host = "YOUR_IP_ADDRESS"
username = "YOUR_LIMITED_USER_ACCOUNT"
password = "YOUR_PASSWORD"

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
client.connect(host, username=username, password=password)

# Execute a command
stdin, stdout, stderr = client.exec_command("df")
print(stdout.read().decode())

# Close the connection
client.close()

# Password 



# https://stackoverflow.com/questions/17335728/connect-to-host-localhost-port-22-connection-refused




# How to send multiple commands { stdin, stdout, stderr = client.exec_command("command1 && command2 - &&  - command3") }
