#!/usr/bin/python3
for asc in range(97, 123):
    if 'q' not in chr(asc) and 'e' not in chr(asc):
        print("{}".format(chr(asc)), end="")
