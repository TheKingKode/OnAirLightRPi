# Print out welcom to provisioning script.  Do you want to provision this now?

#if yes, ask for IP address
    #ask for netmask
    #ask for router ip
    #ask for DNS1
    #ask for DNS2
        #write out /etc/dhcpcd.conf with new ip info
            #ask do you want to test the ip or reboot in onair mode?
                #if yes, reboot with test script
                #if no, reboot with onair mode 

    #if no ask if you want to activate onair-light mode

        #if yes, set startup script to be onair-light.py

            #if no exit to command line
