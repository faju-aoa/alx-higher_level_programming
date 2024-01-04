#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if chr(ord(i)) >= 65 and chr(ord(i)) <= 90:
            print("{}".format(i), end="")
        print()
