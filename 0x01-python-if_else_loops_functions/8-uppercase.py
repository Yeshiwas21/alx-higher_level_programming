#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        result += chr(ord(char) & ~32)
    print(result)

