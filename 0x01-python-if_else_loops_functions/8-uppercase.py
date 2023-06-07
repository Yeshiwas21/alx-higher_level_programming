#!/usr/bin/python3
def uppercase(str):
    for chr in str:
        if ord(chr) > 96 and ord(chr) < 123:
            c = chr(ord(chr) - 32)
        print("{}".format(chr), end="")
    print("")

