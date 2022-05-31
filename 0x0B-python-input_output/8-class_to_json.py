#!/usr/bin/python3
"""became class to json"""


def class_to_json(obj):
    """Take attributes of the obj to a dict (json)"""
    attrs = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and
             not attr.startswith("__")]
    dict_obj = {}
    for item in attrs:
        dict_obj[item] = getattr(obj, item)
    return dict_obj
