#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = sorted(a_dictionary)
    for key in sort_dic:
        print("{:s}: {}".format(key, a_dictionary[key]))
