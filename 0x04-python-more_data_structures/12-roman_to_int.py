#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for r in reversed(roman_string):
        curr_value = digits.get(r, 0)
        total += curr_value if curr_value >= prev_value else -curr_value
        prev_value = curr_value

    return total
