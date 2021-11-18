
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from time import sleep
out = GPIO.output;
out2 = GPIO.OUT;
high = GPIO.HIGH;
low = GPIO.LOW;
GPIO.setup(21, out2)
GPIO.setup(24, out2)
while True:
	out(21, high)
	out(24, low)
	print("Red on, Blue off")
	sleep(2)
	out(21, low)
	out(24, high)
	print("Red off, Blue on")
	sleep(2)
