#!/usr/bin/python3
"""The module to create a json file to add items"""
from pathlib import Path
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = 'add_item.json'
data_file = []
if Path(filename).is_file():
    data_file = load_from_json_file(filename)
else:
    open(filename, 'x')

if len(sys.argv) == 1:
    save_to_json_file(data_file, filename)
else:
    sys.argv.pop(0)
    for i in range(len(sys.argv)):
        data_file.append(sys.argv[i])
    save_to_json_file(data_file, filename)
