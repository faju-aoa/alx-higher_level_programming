#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if chr(ord(str)) >= 65 and chr(ord(str)) <= 90:
            print("{}".format(str), end="")
        print()
