#!/usr/bin/python3
"""Load a json file"""
import json


def load_from_json_file(filename):
    """Load the json file"""
    with open(filename, 'r') as json_file:
        return json.loads(json_file.read())
