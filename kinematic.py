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
	print ''
	values = [vi, vf, a, d, t]
	control(values)	

def control(x):
	"""Sends the list to appropriate section to calculate"""
	values = x
	values.append(0)
	if values[0] == '?': # Initial Velocity unknown
		values[5] += 1
	if values[1] == '?': # Final Velocity unknown
		values[5] += 2
	if values[2] == "?": # Acceleration unknown
		values[5] += 4	
	if values[3] == '?': # Distance unknown
		values[5] += 8
	if values[4] == '?': # Time unknown
		values[5] += 16
	
	if values[5] == 0:
		print 'vi = ', x[0] ,'vf = ', x[1] ,'a =  ', x[2] ,'d =  ', x[3] ,'t = ', x[4]
		print 'Finished'

	elif values[5] in (2, 10):
		# CALCULATE final velocity without d
		vf_viat(values)

	elif values[5] == 17:
		# CALCULATE initial velocity without t
		vi_vfda(values)

	elif values[5] == 9:
		# CALCULATE initial velocity without d
		vi_vfat(values)

	elif values[5] in (2, 6):
		# CALCULATE final velocity without a
		vf_vidt(values)

	elif values[5] in (2, 18):
		# CALCULATE final velocity without t
		vf_viad(values)

	elif x[5] in  (4, 12):
		# CALCULATE acceleration
		a_vivft(values)
		
	elif x[5] in  (8, 24):
		# CALCULATE distance
		d_vivfa(values)

	elif x[5] in (1, 3):
		# CALCULATE initial velocity
		vi_adt(values)

	elif x[5] == 20:
		# CALCULATE acceleration without t
		a_vivfd(values)

	elif x[5] == 16:
		# CALCULATE time
		t_vivfa(values)

	else:
		print 'Cannot calculate need more info'

def vf_viat(x):	
	vi = float(x[0])
	a = float(x[2])
	t = float(x[4])
	vf = vi + a * t
	values = [x[0], vf, x[2], x[3], x[4]]
	control(values)

def vf_vidt(x):
	vi = float(x[0])
	d = float(x[3])
	t = float(x[4])
	vf = 2 * ((d / t) - (vi / 2))
	values = [x[0], vf, x[2], x[3], x[4]]
	control(values)

def vf_viad(x):
	vi = float(x[0])
	a = float(x[2])
	d = float(x[3])
	vf = math.sqrt(vi ** 2 + 2 * a * d)
	values = [x[0], vf, x[2], x[3], x[4]]
	control(values)

def a_vivft(x):
	vi = float(x[0])
	t = float(x[4])
	vf = float(x[1])
	a = (vf - vi) / t
	values = [x[0], x[1], a, x[3], x[4]]
	control(values)

def d_vivfa(x):
	vi = float(x[0])
	vf = float(x[1])
	a = float(x[2])
	d = (vf ** 2 - vi ** 2) / (2 * a)
	values = [x[0], x[1], x[2], d, x[4]]
	control(values)

def t_vivfa(x):
	vi = float(x[0])
	a = float(x[2])
	vf = float(x[1])
	t = (vf - vi) / a
	values = [x[0], x[1], x[2], x[3], t]
	control(values)
def vi_adt(x):
	d = float(x[3])
	a = float(x[2])
	t = float(x[4])
	vi = (d / t) - .5 * a * t
	values = [vi, x[1], x[2], x[3], x[4]]
	control(values)

def a_vivfd(x):
	vi = float(x[0])
	vf = float(x[1])
	d = float(x[3])
	a = (vf ** 2 - vi ** 2) / (2 * d)
	values = [x[0], x[1], a, x[3], x[4]]
	control(values)

def vi_vfda(x):
	a = float(x[2])
	vf = float(x[1])
	d = float(x[3])
	vi = math.sqrt((vf ** 2) - (2 * a * d))
	values = [vi, x[1], x[2], x[3], x[4]]
	control(values)

def vi_vfat(x):
	vf = float(x[1])
	a = float(x[2])
	t = float(x[4])
	vi = vf - a * t
	values = [vi, x[1], x[2], x[3], x[4]]
	control(values)
	
intro()	
