#!/usr/bin/python3
"""
7-add_item:
    This module contains a script that adds all arguments to a python
    list, and saves them to a JSON file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
objects = load_from_json_file("add_item.json")
objects.extend(args)

save_to_json_file(objects, "add_item.json")
