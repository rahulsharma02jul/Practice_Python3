# https://docs.python.org/3.8/library/telnetlib.html#telnet-example

# Backup configuration of Multiple switches Nested loops

# $ cat myswitches.txt
# 192.168.122.72
# 192.168.122.73
# 192.168.122.74
# 192.168.122.75
# 192.168.122.76

import getpass
import telnetlib

user = input("Enter your remote account: ")
password = getpass.getpass()
f = open(myswitches.txt)
for IP in f:
    print(f"Getting running config from Switch {IP}")
    HOST = IP.strip()
    tn = telnetlib.Telnet(HOST)

    # tn.read_until(b"login: ")
    tn.read_until(b"Username: ")
    # Change login to Username: in above line

    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switch_"+ HOST, "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close()

    # print(tn.read_all().decode('ascii'))


# The advantage of this process is that if we create a byte object it is directly stored in the computer’s disk, whereas if a string object is created it is first converted into a byte object then it is stored. 
# So, by directly creating a byte object we are saving time.

# User can also collect pre-check command outputs from a device
