# About Templates  How to use them ?




- Well all the templates are in The Router Folder in /eTrafficApp for Router and in the Switch Folder , you copy one of those templates put it your info into another json file for multiple Routers , for exemple you want to change interfaces for 2 Routers , you make a Router1.json and put the template , and make Router2.json
for the second router , and then

you do :



```

import eTraffic
from eTraffic import Router




router1 = Router("HOST_IP","HOST_NAME","Password","Vendor")
router1.configure_interfaces(template_path="Your template file path")











```
