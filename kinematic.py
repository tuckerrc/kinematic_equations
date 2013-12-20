#! /usr/bin/env python
def intro():
	print "vf = vi + a * t"
	print "d = vi * t + .5 * a * t^2"
	print "vf^2 = vi^2 + 2 * a * d"
	print "d = ((vi +vf) / 2) * t \n"
intro()

def velocityFinal():
	"""Prints final velocity when given vi, a, and t."""
	print "vf = vi + a * t"
	vi = int(raw_input("Value for initial velocity: "))
	a = int(raw_input("Value for acceleration: "))
	t = int(raw_input("Value for time: "))
	
	vf = vi + a * t
	print "final velocity is: ",
	print  vf
	print ""
#velocityFinal()

def distance():
	"""Calculates distance if given vi, t, and a."""
	print "d = vi * t + .5 * a * t^2"
	vi = int(raw_input("Value for initial velocity: "))
	a = int(raw_input("Value for acceleration: "))
	t = int(raw_input("Value for time: "))
	
	d = vi * t + .5 * a * t ** 2
	print "Distance is: ",
	print d
#distance()

def distance2():
	""""Calculates distance when given vi, vf, and t.""""
	print "d = ((vi +vf) / 2) * t"
	vi = int(raw_input("Value for initial velocity: "))
	t = int(raw_input("Value for time: "))
	vf = int(raw_input("Value for final velocity: "))
	
	d = ((vi + vf) / 2) * t
	print "Distance = ",
	print d
distance2()
