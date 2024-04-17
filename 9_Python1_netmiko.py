# Configure multiple config lines...reading from file iosv2_l2_cisco_design, iosv_core_design
# switches using netmiko library
# CORE as well as ACCESS SWITCHES
from netmiko import ConnectHandler

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'cisco',
    'password': 'cisco',
}
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'cisco',
    'password': 'cisco',
}
iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.74',
    'username': 'cisco',
    'password': 'cisco',
}
iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'cisco',
    'password': 'cisco',
}
iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.76',
    'username': 'cisco',
    'password': 'cisco',
}


with open('iosv_core_design') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s6, iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)