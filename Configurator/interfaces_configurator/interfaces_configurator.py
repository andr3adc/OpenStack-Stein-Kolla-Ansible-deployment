print("\n##############################")
print("Interfaces configurator\n")

file = open('./kolla-ansible-config/interfaces', 'w')

#Loopback interface
file.write("auto lo\niface lo inet loopback\n\n")

#Setup primary interface
primary_interface = raw_input("Insert your primary interface name [enp0s25]: ")
file.write("auto " + primary_interface + "\niface " + primary_interface + " inet static\n")

ip_address = raw_input("Insert your primary interface IP address [192.168.0.101]: ")
file.write("  address " + ip_address + "\n")

netmask = raw_input("Insert your primary interface netmask [255.255.255.0]: ")
file.write("  netmask " + netmask + "\n")

dg_address = raw_input("Insert your Default Gateway IP address [192.168.0.1]: ")
file.write("  gateway " + dg_address + "\n")

response = raw_input("\nIs your interface a wireless Interface? [Y/n]: ")
if (response == "yes" or response == "y" or response == "Yes" or response == "Y" or response == "YES"):
    wpa_ssid = raw_input("Insert your wirless network SSID: ")
    file.write("\nwpa-ssid " + wpa_ssid + "\n")

    wpa_psk = raw_input("Insert your wirless network password: ")
    file.write("wpa-psk " + wpa_psk + "\n\n")


#DNS Servers
while True:
    dns_address=raw_input("Insert your DNS IP address (q to quit): ")
    if (dns_address == 'q'):
	break
    file.write("dns-nameserver " + dns_address + "\n")

#Setup secondary interface
secondary_interface = raw_input("\nInsert your secondary interface name: ")
file.write("\nauto " + secondary_interface + "\niface " + secondary_interface + " inet manual\n")
file.write("up ip link set dev " + secondary_interface + " up\n")
file.write("down ip link set dev " + secondary_interface + " down\n\n")

#Close file
file.close()
