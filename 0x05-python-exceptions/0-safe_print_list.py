#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if isinstance(my_list, list):
        count = 0
        try:
            [print(i, end="") for i in my_list[0:x]]
            print()
            for i in my_list[0:x]:
                count += 1
            return count
        except IndexError:
            print("error")
