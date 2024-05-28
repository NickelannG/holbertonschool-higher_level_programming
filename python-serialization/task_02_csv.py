#!/usr/bin/python3
"""
task_02_csv:
    This module contains the convert_csv_to_json function.
"""
import csv
import json


def convert_csv_to_json(csvFilePath):
    """
    This function converts a CSV file to a JSON file.

    Parameters:
        - csvFilePath: The filename of the CSV file to convert.

    Returns:
        - True if the conversion was successful, otherwise False.
    """
    try:
        data = []
        with open(csvFilePath, "r") as csvf:
            csvreader = csv.DictReader(csvf)

            for row in csvreader:
                data.append(row)

        with open("data.json" "w") as jsonf:
            json.dump(data, jsonf)

        return True

    except FileNotFoundError:
        return False
