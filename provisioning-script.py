


# Print out welcome to provisioning script.  Do you want to provision this now?
# print("Welcome to the provisioning script")
ipvar = input("Enter the IP address")
print(ipvar)

#if yes, ask for IP address
    #ask for netmask
    #ask for router ip
    #ask for DNS1
    #ask for DNS2
        #write out /etc/dhcpcd.conf with new ip info
            #ask do you want to test the ip or reboot in onair mode?
                #if yes, reboot with test script
                    #set provision-test.py to start on reboot
                    #say rebooting now
                    #reboot
                #if no, reboot with onair mode

#if no ask if you want to activate onair-light mode

    #if yes, set startup script to be onair-light.py
        #set startup script to ONAIR mode
        #State the PI will now reboot - pause 3 secs
        #Reboot PI

        #if no, say 'exiting to command line'
        #exit to command line
exit
