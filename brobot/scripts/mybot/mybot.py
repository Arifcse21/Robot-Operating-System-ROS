#!/usr/bin/python

import RPi.GPIO as gpio
import time

class MyBot(object):
	def __init__(self, in1=12, in2=13, ena=6, in3=20, in4=21, enb=26):
		self.IN1 = in1
		self.IN2 = in2
		self.IN3 = in3
		self.IN4 = in4
		self.ENA = ena
		self.ENB = enb
		

		gpio.setmode(gpio.BCM)
		gpio.setwarnings(False)
		gpio.setup(self.IN1, gpio.OUT)
		gpio.setup(self.IN2, gpio.OUT)
		gpio.setup(self.IN3, gpio.OUT)
		gpio.setup(self.IN4, gpio.OUT)
		gpio.setup(self.ENA, gpio.OUT)
		gpio.setup(self.ENB, gpio.OUT)

		self.forward()

		self.PWMA = gpio.PWM(self.ENA, 500)
		self.PWMB = gpio.PWM(self.ENB, 500)
		self.PWMA.start(0)
		self.PWMB.start(0)


	def forward(self):
		gpio.output(self.IN1, gpio.HIGH)
		gpio.output(self.IN2, gpio.LOW)
		gpio.output(self.IN3, gpio.LOW)
		gpio.output(self.IN$, gpio.HIGH)


	def stop(self):
		gpio.output(self.IN1, gpio.LOW)
		gpio.output(self.IN2, gpio.LOW)
		gpio.output(self.IN3, gpio.LOW)
		gpio.output(self.IN4, gpio.LOW)

	
	def backward(self):
		gpio.output(self.IN1, gpio.LOW)
		gpio.output(self.IN2, gpio.HIGH)
		gpio.output(self.IN3, gpio.HIGH)
		gpio.output(self.IN4, gpio.LOW)


	def left(self):
		gpio.output(self.IN1, gpio.LOW)
		gpio.output(self.IN2, gpio.HIGH)
		gpio.output(self.IN3, gpio.LOW)
		gpio.output(self.IN4, gpio.HIGH)


	def right(self):
		gpio.output(self.IN1, gpio.HIGH)
		gpio.output(self.IN2, gpio.LOW)
		gpio.output(self.IN3, gpio.HIGH)
		gpio.output(self.IN4, gpio.LOW)

		
	def setPWMA(self, value):
		self.PWMA.ChangeDutyCycle(value)


	def setPWMB(self, value):
		self.PWMB.ChangeDutyCycle(value)


	def setMotor(self, left, right):
		if((left >=0 ) and (left <=100)):
			gpio.output(self.IN1, gpio.HIGH)
			gpio.output(self.IN2, gpio.LOW)
			self.PWMA.ChangeDutyCycle(left)
		elif((left < 0) and (left >= -100)):
			gpio.output(self.IN1, gpio.LOW)
			gpio.output(self.IN2, gpio.HIGH)
			self.PWMA.ChangeDutyCycle(right)
		if ((right >= 0) and (right <= 100)):
			gpio.output(self.IN3, gpio.LOW)
			gpio.output(self.IN4, gpio.HIGH)
			self.PWMB.ChangeDutyCycle(right)
		elif((right < 0)and (right >= -100)):
			gpio.output(self.IN3, gpio.HIGH)
			gpio.output(self.IN4, gpio.LOW)
			self.ChangeDutyCycle(0 -  right)

		
