
#import RPi.GPIO as GPIO
#import time
#import psutil
#import subprocess

# Print out welcome to provisioning script.  Do you want to provision this now?
# print("Welcome to the provisioning script")
ihm_welcome = input("Welcome to the provisioning script.  Would you like to provision this PI now or exit to the command line (Y/N) ")


#if yes, ask for IP address
if ihm_welcome in ('Y','y'):
    ipvar = input("Enter the IP address: ")
    #ask for IP addressY
    netvar = input ("Enter the netmask: ")
    #ask for netmask
    routervar = input ("Router IP: ")
    #ask for router ip
    dns1var = input ("DNS 1: ")
    #ask for DNS1
    dns2var = input("DNS 2: ")
    #ask for DNS2
        #write out /etc/dhcpcd.conf with new ip info
    with open('dhcpcd.conf','w') as f:
        for line in f:
            print(line, end='')


        #ask if you want to set the hostname
    hostvar = input ('Would you like to set the HOSTNAME? [Y/N]')
        if hostvar in ('Y','y'):
            hostsetvar = input('Enter HOSTNAME: ')
            #write out hostname
            #open /etc/hostname and replace 'raspberrypi' with hostsetvar and save
            #open /etc/hosts and replace 'raspberrypi' with hostsetvar and save

        #ask do you want to test the ip or reboot in onair mode?
    testipvar = input('Do you want to test the IP address? [Y/N]: ')
        if testipvar in ('Y','y'):
            #if yes, reboot with test script
            #set provision-test.py to start on reboot
            #say rebooting now
            #reboot
        #if no, reboot with onair mode

#if no ask if you want to activate onair-light mode
else:
    activatevar = input("Do you want to enable ONAIR MODE? [Y/N]: ")

    #if yes, set startup script to be onair-light.py
    if activatevar == ('Y','y'):
        #set startup script to ONAIR mode
        #State the PI will now reboot - pause 3 secs
        print ('PI will now reboot!')

        #Reboot PI

        #if no, say 'exiting to command line'
    else:
        print ('Exiting to command line')
        #exit to command line
