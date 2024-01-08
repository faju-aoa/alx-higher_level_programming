#!/usr/bin/python3
def no_c(my_string):
    l_str = list(my_string)
    d = [i for i in l_str]
    if "C" not in d:
        d.remove("c")
    if "C" in d:
        d.remove("C")
    c = "".join(d)
    return c
