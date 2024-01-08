#!/usr/bin/python3
def no_c(my_string):
    li = list(my_string)
    d = [i for i in li]
    if "c" in d:
        d.remove("c")
    if "C" in d:
        d.remove("C")
    c = "".join(d)
    return c
