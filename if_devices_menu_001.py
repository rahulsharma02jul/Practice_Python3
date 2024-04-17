print("These are the available devices: ")
print("1 -- router")
print("2 -- switch")
print("3 -- firewall")
choice = input("Please enter the number of the device you want: ")
if choice == "1":
    dev = "router"
elif choice == "2":
    dev = "switch"
elif choice == "3":
    dev = "firewall"
else:
    print("Sorry, that is not a valid choice!")
    dev = "nothing"
print()
print("You have chosen: " + dev)
