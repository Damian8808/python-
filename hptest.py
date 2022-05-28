from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

passwd = getpass.getpass ('Podaj haslo:')

hp_comware = {
    'device_type': 'hp_comware',
     'ip':   '10.58.10.11',
     'username': 'admin',
     'password': 'passwd',
     'verbose': False,
 }

 start_time = datetime.now()
  for a_device in (hp_comware):
...     net_connect = ConnectHandler(**a_device)
...     output = net_connect.send_command("show vlan brief")
...     print "\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['device_type'])
...     print output
...     print ">>>>>>>>> End <<<<<<<<<"
... 
end_time = datetime.now()

total_time = end_time - start_time 