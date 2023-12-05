#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for counter, number in enumerate(my_list):
        if number % 2 == 0:
            new_list[counter] = True
        else:
            new_list[counter] = False
    return(new_list)
