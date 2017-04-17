# exceptions example

a = input("first: ")
b = input("second: ")

try:
	print a/b
except ZeroDivisionError:
	print "error - zero division"

# how to raise/simulate exception
raise ZeroDivisionError
