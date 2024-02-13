#!/usr/bin/python3
"""
This script adds command line arguments to a list and saves it to a JSON file.
"""

import json
import sys
from os import path


def save_to_json_file(my_obj, filename):
    """
    Save the given object to a JSON file.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    Load an object from a JSON file.
    """
    result = []
    if path.exists(filename):
        with open(filename, "r") as f:
            result = json.load(f)
    return result


def add_arguments_to_list(arguments_list, filename):
    """
    Add command line arguments to the list and save to a JSON file.
    """
    arguments_list.extend(sys.argv[1:])

    save_to_json_file(arguments_list, filename)


if __name__ == "__main__":
    my_list = load_from_json_file("add_item.json")

    add_arguments_to_list(my_list, "add_item.json")

    print(f"Arguments added to the list and saved to add_item.json: {my_list}")
