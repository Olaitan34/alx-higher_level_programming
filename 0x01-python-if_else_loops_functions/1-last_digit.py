#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)
last = abs(number) % 10  # Getting the last digit using modulus

if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
if last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
if 0 < last < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last))

