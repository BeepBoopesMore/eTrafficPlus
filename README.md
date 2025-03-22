# A guide to eTraffic , I want brownies!
## What is eTraffic?
eTraffic is a FrameWork , designed in python which is meant to be used for  switches and routers managing them easier


# Important!! 
Although eTraffic makes configuration easier that does not mean you don't need networking knowledge at all with the respective device , you still need to know the syntax of things like access lists and know what inside local and inside global is for NAT aswell as other functions , the framework just connects instantly via ssh into a device and uses templates but some things you have to write yourself.
If you know those just use the instructions in the respective function. P.S Please read Templates.MD
 -Also someone please lend me a cisco router or a switch to actually test this thing



## Why eTraffic?
eTraffic is genuinely easier to use  and u barely have to do anything besides just editing the provided template and use the base models functions which are all pretty straight forward
## How does eTraffic work?
eTraffic made with paramiko works by using SSH ,agent-free on the respective router/switch and it just does specific commands based on json templates that u can model.

## What is the future like for eTraffic?
Well i plan on releasing this in forms of not only network but Enterprise such as Servers(Linux/Windows) aswell.
- And i also plan on making a go framework aswell
   # Also, also
   - I do want to make the Office Manager which is basically a subnetting tool which you just put ur router in and you setup your vlans etc into things called Offices


# Where are the templates docs?
There is no need for docs for that , you can just read 
the file Templates.md to see how to use the respective template such for port-security , port-channel , etc. it's all there.

# To do 
- Process the Router and Switch Raw data using Re

# What vendors are available?
- Cisco
- Juniper
- Huawei(Future)
- TP_Link(Future)
- Others in the future

# Code Sample

```python3

import eTraffic
from eTraffic import Router
from eTrafficUtils import Office
from eTraffic import Switch


router1 = Router("10.0.0.1","Musk","password","Cisco")
clock_r1 = router1.clock
version_r1 = router1.version
router1.configure_interfaces(template_path="YOUR_JSON_FILE_PATH_HERE")
router2 = Router("10.0.0.2","Banny","password","Juniper")
clock_r2 = router2.clock
version_r2 = router2.version
router2.setup_NTP("10.0.0.1",become_host=False)




```
