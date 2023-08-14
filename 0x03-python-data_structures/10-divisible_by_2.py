#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multilist = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            multilist.append(True)
        else:
            multilist.append(False)
    return (multilist)
