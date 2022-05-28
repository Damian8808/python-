>>> from netmiko import ConnectHandler

>>> GDBUDA-3.0-SWA11 = {
...   'device_type': 'hp_comware',
...   'ip': '10.58.10.11',
      'username': 'pyclass',
...   'password': 'password',
... } 
connection = ConnectHandler(
device_type='hp_comware',
host='10.58.10.11',  
username='admin', 
password='Bi0l0gi@')

connection.enable() 
connection.config_mode()
output = connection.send_command('vlan 4000 | name test')
output=connection.send_command('show vlan brief')

print(output)
print('Zamykam polaczenie')

connection.disconnect()

