#!/usr/bin/python3
"""
Script for adding command line arguments to a JSON file.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


try:
    myList = load_from_json_file("add_item.json")
except FileNotFoundError:
    myList = []

# Append command line arguments to the list
for arg in range(1, len(sys.argv)):
    myList.append(sys.argv[arg])

# Save the updated list to the JSON file
save_to_json_file(myList, "add_item.json")