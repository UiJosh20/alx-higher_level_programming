#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    now_d = a_dictionary.copy()
    for i in now_d.keys():
        now_d[i] *= 2
    return now_d
