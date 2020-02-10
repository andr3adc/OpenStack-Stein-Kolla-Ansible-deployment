# kolla-ansible-config
Kolla ansibile configuration on Ubuntu server 18.04 with Open Stack Stein

### Authors:
###     - Della Chiesa Andrea
###     - Ferretti Igor
### kolla-ansible, all-in-one and multinode
### stein, bionic, source
### v3: 20200301
### run as normal user

### kolla-ansible -v "stein" on Ubuntu Server 18.04 BM

must change in /etc/network/interfaces:
	- interfaces name ens3 and ens4
	- IP address of enr3 with netmask, gateway and so on
    - the second interface must not have any Ip address
    
must change in globals.yml:
	kolla_internal_vip_address  ### with the same parameters of /etc/network/interfaces
	network_interface           ### with the same parameters of /etc/network/interfaces
	neutron_external_interface  ### choose another net for the management (doesn't matter)

must change in kolla-stein-step03.sh: vdb --> DISK_NAME
    # to see disks tap 'sudo fdisk -l'
    sudo pvcreate /dev/vdb
	sudo vgcreate cinder-volumes /dev/vdb

must change in init-runonce:
	EXT_NET_CIDR='10.0.3.0/24' # change with the externl network
	EXT_NET_RANGE='start=10.0.3.50,end=10.0.3.99' # set of external IP address avaiables for VMs
	EXT_NET_GATEWAY='10.0.3.1' # IP address for the external network
	
# remember: after each .sh the system should be rebooted
run system-config.sh
run kolla-stein-0x.sh from 1 to 5

# notes:
# kolla-config scripts are indipendent from the system they are running on, could be baremetal or a VM.
# system script is NOT, so you must check it that everything it's ok.