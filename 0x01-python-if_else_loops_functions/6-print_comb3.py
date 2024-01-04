#!/usr/bin/python3
for l in range(0, 9):
    for p in range(l+1, 10):
        if l == 8:
            print("{}{}".format(l, p))
        else:
            print("{}{}".format(l, p), end=", ")
