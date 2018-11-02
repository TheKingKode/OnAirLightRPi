#import libraries for GPIO pins and utils etc
import RPi.GPIO as GPIO
import time
import psutil
import subprocess

#var for listing processes
process = psutil.pids()

#setmode for GPIO pin numbering
GPIO.setmode(GPIO.BOARD)

#GPIO setup for pin 16
GPIO.setup(16,GPIO.IN)

#use TRY to create FINALLY action
try:
	#while OFF AIR - indefinite loop
	while True:
		if GPIO.input(16) == 0:
			#test to see if fbi (image viewer) is running
			#if not, run it
			'''
			for id in process:
				proc = psutil.Process(id)
				if proc.name() == "fbi":
					subprocess.call('sudo kill $(pgrep fbi)', shell=True)
#					time.sleep(.1)

				else:
#					subprocess.call('sudo fbi -a --noverbose -T 1 /home/pi/onair.16.9.jpg', shell=True)
					time.sleep(.1)

			#test to see if OMXPlayer (video player) is running
			#if not, run the loop
				if proc.name() == "omxplayer":
					time.sleep(.1)

				else:
					subprocess.call('sudo omxplayer -o local --loop /home/pi/video.mp4', shell=True)
					time.sleep(.1)
			'''
		#while ON AIR
		if GPIO.input(16) == 1:
			#test to see if fbi (image viewer) is running
			#if not, run it
			'''
			for id in process:
				proc = psutil.Process(id)
				if proc.name() == "fbi":
					time.sleep(.1)

				else:
					subprocess.call('sudo fbi -a --noverbose -T 1 /home/pi/onair.16.9.jpg', shell=True)
					time.sleep(.1)

			#test to see if OMXPlayer is running
			#if it IS running, KILL it
				if proc.name() == "omxplayer":
					subprocess.call('sudo kill $(pgrep omxplayer)', shell=True)
					time.sleep(.1)

				else:
					time.sleep(.1)
			'''
finally:
#cleanup GPIO pins
	GPIO.cleanup()
