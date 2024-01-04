#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if chr(ord(i)) >= 97 and chr(ord(i)) <= 122:
            i -= 32
            print("{}".format(i), end="")
        print()
