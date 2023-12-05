#!/usr/bin/python3
def max_integer(my_list=[]):
    large_i = my_list[0]
    for num in my_list:
        if num > large_i:
            large_i = num
    if my_list == "":
        return(None)
    return(large_i)
