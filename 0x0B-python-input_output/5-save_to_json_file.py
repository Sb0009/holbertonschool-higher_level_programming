#!/usr/bin/python3
"""Save to jason file"""
import json


def save_to_json_file(my_obj, filename):
    """save in json from an object"""
    with open(filename, 'w+') as json_file:
        json.dump(my_obj, json_file)
