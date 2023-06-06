#!/usr/bin/python3
import random
for ch in range(97, 123):
    if (chr(ch) == 'q' or chr(ch) == 'e'):
        continue
    else:
        print(chr(ch), end="")
