#! /usr/bin/env python


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
	print x	
	
intro()	
