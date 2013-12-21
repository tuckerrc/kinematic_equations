#! /usr/bin/env python

<<<<<<< HEAD
import math

def intro():
	print "Welcome to Tucker's Kinematic equations calculator"
	print "Please enter the values (? = unknown)"
	vi = raw_input("Initial Velocity: ")
	vf = raw_input("Final Velocity: ")
	a = raw_input("Acceleration: ")
	d = raw_input("Distance: ")
	t = raw_input("Time: ")
	function = 0
	print type(function)
	if vi == '?':
		function += 1
	if vf == '?':
		function += 2
	if a == "?":
		function += 4	
	if d == '?':
		function += 8
	if t == '?':
		function += 16
	print vi ,' ', vf ,' ', a ,' ', d ,' ', t ,' ', function
	x = [vi, vf, a, d, t, function]
	print variables	
=======
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
>>>>>>> 880e02fe0c345599cefe958a35ad85b97979c622
	
intro()	
