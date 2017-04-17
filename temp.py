num_1 = input("enter something: ")

if num_1 > 10:
	print "gt 10"
else:
	print "lz 10"


def formula(a,b):
	if b == 0:
		print "error - divide by zero"
		return "error - unexpected return"
	result = (a+b)/b
	return result

print(formula(float(34),num_1))
