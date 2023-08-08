#!/usr/bin/python3
def uppercase(str):
    for char in str:
        uppercase_char = chr(ord(char) - 32) if ord('a') <= ord(char) <= ord('Z') else char
        print(uppercase_char, end="")
        print()
