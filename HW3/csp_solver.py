#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 3, 10/27/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

import sys


def readFile(filename):
    """
    Appends all lines in a file into a list.

    :param filename: name of file
    :return: list containing all lines in the file
    """
    f = open(filename)
    variables = []
    for line in f:
        if line != '\n':
            variables.append(line[:-1])
    f.close()
    return variables


if len(sys.argv) == 3:
    problem_filename = sys.argv[1]
    use_forward_check_flag = sys.argv[2]
else:
    print "Invalid input. Please use the format:"
    print "python csp_solver.py problem_filename use_forward_check_flag"

# test to print the fucking file
print readFile(problem_filename)
# for line in readFile(problem_filename):
#     print "".join(line)