#!/usr/bin/python3
def no_c(my_string):
    rem_string = [i for i in my_string if "c" not in i and "C" not in i]
    j_string = "".join(rem_string)
    return j_string
