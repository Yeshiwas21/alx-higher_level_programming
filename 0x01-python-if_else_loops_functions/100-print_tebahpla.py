#!/usr/bin/python3
for i in range(90, 64, -1):
     print("{}{}".format(chr(i + 32), chr(i)), end='')

    if i == 65:
        break
