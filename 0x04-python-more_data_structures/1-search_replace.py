#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    replace_num = [num if num != search else replace for num in my_list]
    return replace_num
