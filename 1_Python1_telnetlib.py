# https://docs.python.org/3.8/library/telnetlib.html#telnet-example

import getpass
import telnetlib

HOST = "localhost"
# Change the hostname in above line
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
# Change login to Username: in above line

tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# tn.write(b"ls\n")
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"int loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))


# The advantage of this process is that if we create a byte object it is directly stored in the computer’s disk, whereas if a string object is created it is first converted into a byte object then it is stored. 
# So, by directly creating a byte object we are saving time.

# User can also collect pre-check command outputs from a device
