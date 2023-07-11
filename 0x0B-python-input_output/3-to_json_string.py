#!/usr/bin/python3
"""
This module provides functions for JSON serialization.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
