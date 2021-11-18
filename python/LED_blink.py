
import RPi.GPIO as GPIO #importing the library for controlleing the pins
GPIO.setmode(GPIO.BCM) #change the method of controlling the pins
from time import sleep #importing a function to wait
out = GPIO.output; #shortening commands
out2 = GPIO.OUT;
high = GPIO.HIGH;
low = GPIO.LOW;
GPIO.setup(21, out2) #setting up the pins as outputs
GPIO.setup(24, out2)
while True: #infinite loop
	out(21, high) #turning red on
	out(24, low) #turning blue off
	print("Red on, Blue off") 
	sleep(2) #wait for 2 seconds
	out(21, low) #turning red off
	out(24, high) #turning blue on
	print("Red off, Blue on")
	sleep(2) #wait for 2 seconds
