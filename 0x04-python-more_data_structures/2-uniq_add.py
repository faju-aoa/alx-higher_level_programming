#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    add_uniq =0
    for numbers in my_list:
      if numbers not in unique:
        unique.append(numbers)
    for i in range(0, len(unique)):
      add_uniq+= unique[i]
    return add_uniq
