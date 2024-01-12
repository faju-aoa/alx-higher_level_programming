def common_elements(set_1, set_2):
    if not set_1:
        return set_1
    if not set_2:
        return set_2
    common_ele = set_1 & set_2
    return common_ele
