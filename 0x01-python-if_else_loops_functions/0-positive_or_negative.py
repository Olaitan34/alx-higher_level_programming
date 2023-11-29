#!/usr/bin/python3
import random
number = random.randint(-10,10)
if number > 0:
	print(number.format("is positive"))
elif number == 0:
	print(number.format("is zero"))
else:
	print(number.format("is negative"))
	
