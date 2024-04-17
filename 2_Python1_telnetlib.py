# https://docs.python.org/3.8/library/telnetlib.html#telnet-example

# configure switch vlans

import getpass
import telnetlib

HOST = "localhost"
# Change the hostname in above line
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

# tn.read_until(b"login: ")
tn.read_until(b"Username: ")
# Change login to Username: in above line

tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# tn.write(b"ls\n")
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"vlan 10\n")
tn.write(b"name VLAN_10\n")
tn.write(b"vlan 20\n")
tn.write(b"name VLAN_20\n")
tn.write(b"vlan 30\n")
tn.write(b"name VLAN_30\n")
tn.write(b"vlan 40\n")
tn.write(b"name VLAN_40\n")
tn.write(b"vlan 50\n")
tn.write(b"name VLAN_50\n")
tn.write(b"vlan 60\n")
tn.write(b"name VLAN_60\n")
tn.write(b"vlan 70\n")
tn.write(b"name VLAN_70\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))


# The advantage of this process is that if we create a byte object it is directly stored in the computer’s disk, whereas if a string object is created it is first converted into a byte object then it is stored. 
# So, by directly creating a byte object we are saving time.

# User can also collect pre-check command outputs from a device
