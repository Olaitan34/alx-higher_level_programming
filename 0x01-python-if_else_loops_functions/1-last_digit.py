#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)
last = abs(number) % 10  # Getting the last digit using modulus

if number < 0:
    if last == 0:
        print("Last digit of {} is {} and is 0".format(number, abs(last)))
    elif last > 5:
        print("Last digit of {} is -{} and \
is less than 6 and not 0".format(number, abs(last)))
    else:
        print("Last digit of {} is -{} and \
is less than 6 and not 0".format(number, abs(last)))
else:
    if last == 0:
        print("Last digit of {} is {} and is 0".format(number, last))
    elif last > 5:
        print("Last digit of {} is {} and \
is greater than 5".format(number, last))
    else:
        print("Last digit of {} is {} and \
is less than 6 and not 0".format(number, last))
