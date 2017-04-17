# class example

class vehicle:
	wheels = 4
	def __init__(this):
		print "vehicle"

class car(vehicle): # inheritance
	def __init__(this):
		this.speed = 10 # var added to object
	def calcV(this,x): # first param is self object, always exists i any class function
		return 4*x+10

ecar = car() # calls constructor and creats class objects
print ecar.speed
print ecar.calcV(20)
print ecar.wheels

