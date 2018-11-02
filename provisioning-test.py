#Welcome to test script. You have rebooted in test mode

#Ask are the ip settings correct? Y/N

#if IP settings response is Y
    #ask if you would like to reboot in ONAIR LIGHT mode?
        #If Y set startup-script to ONAIR LIGHT mode.
            #Say rebooting now
            #wait 2 secs and reboot 

        #If N say exiting to command line
        #Exit to command line
#if IP settings response is N
    #ask if you would like to set up IP now
        #if Y exit and start provisioning script
        #if N say exiting to command line
            #exit to command line
