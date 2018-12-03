"""
util.py
Description: Contains utilities
"""

"""
checks that a name is a string
TODO check for no duplicate names
"""
def check_validity_of_name(name):
    if not isinstance(name, str):
            raise TypeError("Name is not a string")