#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        [print("{:d}".format(my_list[j]), end="") for j in range(x)if isinstance(my_list[j], int)]
        for i in my_list[0:x]:
            if isinstance(i, int):
                count += 1
    except(TypeError, ValueError):
        pass
    print()
    return count
