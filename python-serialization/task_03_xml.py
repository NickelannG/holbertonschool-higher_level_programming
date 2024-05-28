#!/usr/bin/python3
"""
task_03_xml:
    This module contains the serialize_to_xml and deserialize_from_xml
    functions.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This function serializes a Python dictionary into XML

    Parameters:
        - dictionary: the Python dictionary to convert.
        - filename: the name of the file that will contain the XML
        converted dictionary.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  # Creating child elements
        child.text = str(value)

    tree = ET.ElementTree(root)  # Creating ElementTree object

    tree.write(filename)  # Writing to XML file


def deserialize_from_xml(filename):
    """
    This function deserializes XML data.

    Parameters:
        - filename: The name of the file that contains the XML data to be
        deserialized.

    Returns:
        - Python_dict: the Python dictionary after deserialization.
    """
    tree = ET.parse(filename)  # Parse through XML file
    root = tree.getroot()

    python_dict = {}

    for child in root:
        python_dict[child.tag] = child.text
    return python_dict
