from importlib.metadata import files
from netmiko import ConnectHandler
from getpass import getpass 

password = getpass()

buda = {
    'device_type': 'hp_comware',
     'ip':   '10.58.10.11',
     'username': 'admin',
     'password': password , 
}

GDBUDCC3SWA44 = {
    'device_type': 'hp_comware',
     'ip':   '10.58.10.44',
     'username': 'admin',
     'password': password , 
}

 
device_list = [GDBUDCC3SWA44,buda]

for device in device_list: print ('Connecting to the device :' + device ['ip'])
net_connect = ConnectHandler(**device)
for n in range (87):
    print ("Creating Vlan" + str(n))
     
output = net_connect.send_config_set('vlan' + str(n) , 'name vlan-SAP-87')
#output=net_connect.send_command ('display vlan brief')

print(output)
print('Zamykam polaczenie')

net_connect.disconnect() 