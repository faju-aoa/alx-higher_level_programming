def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    h = my_list[0]
    for i in my_list:
        if i > h:
            h = i
    return (h)
