#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        max_int = my_list[0]
        for alma in range(len(my_list)):
            if my_list[alma] > max_int:
                max_int = my_list[alma]
        return (max_int)
