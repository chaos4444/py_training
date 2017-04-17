# ========
# begin

#num_1 = input("enter something: ")
num_1=1 #tmp
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

# ========
# loops

print(formula(float(34),num_1))
#cut = input ("specify cut index: ")
cut=1 #tmp
index = 0

while index < cut:
	print "index: " + str(index)
	index += 1


#cut = input ("specify cut index: ")

for index in range (0,cut):
	print "index: " + str(index)
	index += 1

# ========
# lists

list = [11,23,443,22,11333]

print list[0]
print list[-1] #negative starts from left
print list
print len(list)
print list[0:2]
print list[1:2]

list.append(90)
print list
print len(list)

list.pop(2)
print list
print len(list)

def sumv(a):
	result = 0
	for x in a:
		result = result+x
	return result

def avgv(a):
	return sumv(a)/len(a)

print sumv(list)
print avgv(list)

# ========
# dictionaries

dict = {"user1":"pass1","user2":"pass2","user3":"pass3","userpp":"qwerty"}
print dict
print dict["user1"]
print "\n"

for x in dict:
	print x

def exists_in_dict(d,key):
	result = False
	for x in d:
		if x == key:
			result = True
	return result

exitv = True #tmp False
while not exitv :
	inp =  raw_input("Enter user name: ")
#	if exists_in_dict(dict,inp):
	if inp in dict:
		print "Tricky one :-). The password for the " + inp + " is: " + dict[inp]
	else:
		print " Yyyy... WTF? o.O"
		if inp == 'q':
			print "exiting"
			break
print "\n# modules" 
# ========
# modules

import random as rnd
# or:
from random import randint
#or for all modules from random:
# from random import *

print rnd.randint(1,100000)
print randint(0,2)

# import own modules
# module1.py has to exist in working dir
import module1 as m1

aa = [1,2,3,4,5,6,7,8,9]

print m1.sumvm(aa)

m1.pvm(aa)

