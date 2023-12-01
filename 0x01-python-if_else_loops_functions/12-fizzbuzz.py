#!/usr/bin/python3
def fizzbuzz():
    number = range(1, 101)
    for i in number:
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz ", end="")
        if (i % 3) == 0:
            print("Fizz ", end="")
        elif(i % 5) == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
