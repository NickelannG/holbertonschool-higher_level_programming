#!/usr/bin/python3
"""
8-class_to_json:
    This Module contains the class_to_json function
"""
import json


def class_to_json(obj):
    """
    This function returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    json_dict = obj.__dict__

    return json_dict
