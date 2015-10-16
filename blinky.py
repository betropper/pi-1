

import RPi.GPIO as GPIO
import time as t
import random

pins = [17,27,22,5,6,13,19,26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins,GPIO.OUT)


def on(pin):
	GPIO.output(pin,GPIO.HIGH)


def off(pin):
	GPIO.output(pin,GPIO.LOW)

def alloff(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8):
	off(pin)
	off(pin2)
	off(pin3)
	off(pin4)
	off(pin5)
	off(pin6)
	off(pin7)
	off(pin8)

def allon(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8):
	on(pin)
	on(pin2)
	on(pin3)
	on(pin4)
	on(pin5)
	on(pin6)
	on(pin7)
	on(pin8)

def blink(pin,count=1):
	for n in range(count):
		on(pin)
		t.sleep(.3)
		off(pin)
		t.sleep(.3)

def blinkdown(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8,count=1):
	for n in range (count):
		on(pin)
		t.sleep(.2)
		on(pin2)
		t.sleep(.2)
		off(pin)
		on(pin3)
		t.sleep(.2)
		off(pin2)
		on(pin4)
		t.sleep(.2)
		off(pin3)
		on(pin5)
		t.sleep(.2)
		off(pin4)
		on(pin6)
		t.sleep(.2)
		off(pin5)
		on(pin7)
		t.sleep(.2)
		off(pin6)
		on(pin8)
		t.sleep(.2)
		off(pin7)
		t.sleep(.2)
		off(pin8)

def blinkup(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8,count=1):
	for n in range (count):
		on(pin8)
		t.sleep(.2)
		on(pin7)
		t.sleep(.2)
		off(pin8)
		on(pin6)
		t.sleep(.2)
		off(pin7)
		on(pin5)
		t.sleep(.2)
		off(pin6)
		on(pin4)
		t.sleep(.2)
		off(pin5)
		on(pin3)
		t.sleep(.2)
		off(pin4)
		on(pin2)
		t.sleep(.2)
		off(pin3)
		on(pin)
		t.sleep(.2)
		off(pin2)
		t.sleep(.2)
		off(pin)

def gameshow(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8,count=1):
	print("WELCOME TO THE GAMESHOW OF SHOWS.")
	print("What light number will be lit up? 1 to 8!")
	answer = input("> ")
	numbers = [1,2,3,4,5,6,7,8]
	reveal = random.choice(numbers)
	print("And the answer is...")
	lights = [pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8]
	reveallightup = lights[reveal - 1]
	t.sleep(1)
	for n in range (3):
		on(reveallightup)
		t.sleep(.4)
		off(reveallightup)
		t.sleep(.4)
	if int(answer) == reveal:
		print("YOU WON!")
		for n in range (2):
			allon(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8)
			t.sleep(.4)
			alloff(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8)
			t.sleep(.4)
		blinkdown(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8)
		blinkup(pin,pin2,pin3,pin4,pin5,pin6,pin7,pin8)
	else:
		print("LOSER. TRY AGAIN!")
