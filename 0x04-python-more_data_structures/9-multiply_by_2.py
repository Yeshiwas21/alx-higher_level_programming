#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_dict = {}
    for key, value in a_dictionary.items():
        multi_dict[key] = value * 2
    return multi_dict
