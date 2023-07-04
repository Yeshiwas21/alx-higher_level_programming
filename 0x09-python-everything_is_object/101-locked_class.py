#!/usr/bin/python3
"""class LockedClass"""


class LockedClass:
    """Prevents attribute creation"""
    __slots__ = ['first_name']
