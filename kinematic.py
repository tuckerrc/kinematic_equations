#! /usr/bin/env python


import math

def intro():
	"""Intro to the script and asks for the variables."""
	print "Welcome to Tucker's Kinematic equations calculator"
	print "Please enter the values (? = unknown)"
	vi = raw_input("Initial Velocity: ")
	vf = raw_input("Final Velocity: ")
	a = raw_input("Acceleration: ")
	d = raw_input("Distance: ")
	t = raw_input("Time: ")
	print 'vi = ', vi ,'vf = ', vf ,'a =  ', a ,'d =  ', d ,'t = ', t
	values = [vi, vf, a, d, t]
	control(values)	

def control(x):
	"""Sends the list to appropriate section to calculate"""
	values = x
	values.append(0)
	if values[0] == '?':
		valuex[5] += 1
	if values[1] == '?':
		values[5] += 2
	if values[2] == "?":
		values[5] += 4	
	if values[3] == '?':
		values[5] += 8
	if values[4] == '?':
		values[5] += 16
	
	if values[5] == 0:
		print 'vi = ', x[0] ,'vf = ', x[1] ,'a =  ', x[2] ,'d =  ', x[3] ,'t = ', x[4]
		print 'Finished'
	elif values[5] in (2, 3, 6, 10, 18):
		vf_viat(values)
	elif x[5] in  (4, 5, 12, 20):
		print 'Calculate acceleration'
	elif x[5] in  (8, 9, 24):
		print 'Calculate distance'
	elif x[5] in (1, 17):
		print 'Calculate initial velocity'
	elif x[5] in (16):
		print 'Calculate time'
	else:
		print 'Cannot calculate need more info'
def vf_viat(x):	
	vi = float(x[0])
	a = float(x[2])
	t = float(x[4])
	vf = vi + a * t
	values = [x[0], vf, x[2], x[3], x[4]]
	control(values)
	
intro()	
