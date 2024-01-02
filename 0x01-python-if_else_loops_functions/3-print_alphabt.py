#!/usr/bin/python3
for asc in range(97, 123):
   if not'q' in chr(asc) and not 'e' in chr(asc):
       print("{}".format(chr(asc)), end="")
