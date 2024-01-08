#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bo = my_list[:]
    for num, i in enumerate(my_list):
        if i % 2 == 0:
            bo[num] = True
        else:
            bo[num] = False
    return(bo)
