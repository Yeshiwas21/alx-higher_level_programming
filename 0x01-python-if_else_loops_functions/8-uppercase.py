#!/usr/bin/python3
def uppercase(str):
    result = ''
    for ch in str:
        result += chr(ord(ch) & ~32)
    print("{}".format(result))

