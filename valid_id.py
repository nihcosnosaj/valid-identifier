#!/usr/bin/env python3
"""
Determines whether an identifier is valid or not based on CLI input
"""

import argparse 
import keyword
import string


def GetArguments():
    """Get command line arguments to test for validity."""
    parser = argparse.ArgumentParser(description="Identify valid identifiers.")
    parser.add_argument('--name', type=str, required=True, help='a string to test for validity')

    args = parser.parse_args()
    
    return args.name 

def IsValidIdentifier(name):
    """Takes a string as a parameter and returns whether or not it is a valid
    Python identifier, and if it isn't, it also returns the reason. 
    """

    if name in keyword.kwlist:
        return (False, f"{name} -> Not Valid: this is a keyword!")

    if not name[0].isalpha() and not name[0] == '_':
        return (False, "Not Valid: the first symbol must be alphabetic or '_'.")

    for char in name:
        if not char.isalnum() and not char == '_':
            return (False, f"Not Valid: '{char}' is not allowed.")

    return (True, "Valid!")



def Tests():
    DATA = ('x', '_x', '2x', 'x,y', 'yield', 'is_this_good')
    for test in DATA:
        print(IsValidIdentifier(test))


if __name__ == "__main__":
    print(IsValidIdentifier(GetArguments()))
