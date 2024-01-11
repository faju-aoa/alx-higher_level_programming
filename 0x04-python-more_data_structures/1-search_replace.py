#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = list(my_list)
    copy_list[search-1] = replace
    return copy_list
