#!/usr/bin/python3
def uper(c):
        if ord(c) >= 97 and ord(c) <= 122:
            return (ord(c) - 32)
        else:
            return ord(c)

def uppercase(s):
    str_new = ""
    for c in s:
        str_new += "%c" % uper(c)
        print("{:s}".format(str_new))
