#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_output = []
    for num in my_list:
        if num % 2 == 0:
            list_output.append(True)
        else:
            list_output.append(False)
    return list_output
