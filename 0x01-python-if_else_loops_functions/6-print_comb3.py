#!/usr/bin/python3
for l in range(1, 9):
    for p in range(1+1, 10):
        if l == 8 and p == 9 :
            print("89")
        else:
            print("{}{}".format(l, p), end=", ")
