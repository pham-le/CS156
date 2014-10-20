#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 3, 10/27/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

import sys


def constraintsFromFile(filename):
    """
    Appends all lines in a file into a list.

    :param filename: name of file
    :return: list containing all lines in the file
    """
    f = open(filename)
    constraints = []
    for line in f:
        if line != '\n':
            c = line.rstrip('\n').split() #c is a list with each word in the line
            if c[2].isdigit(): #change the third value to int if it is one.
                c[2] = int(c[2])
            constraints.append(tuple(c)) #turns the list to a tuple, add it to the list
    f.close()
    return constraints

def getInitialDomain(constraints):
    """Given a list of constraints, returns a list of integers from 0 to max(D, V), 
    where D is the number of distinct variables and V is the max integer in a constaint"""
    d = 0
    v = 0
    #for c in constraints


if len(sys.argv) == 3:
    problem_filename = sys.argv[1]
    use_forward_check_flag = sys.argv[2]
else:
    print "Invalid input. Please use the format:"
    print "python csp_solver.py problem_filename use_forward_check_flag"

# test to print the fucking file
print constraintsFromFile(problem_filename)

# for line in readFile(problem_filename):
#     print "".join(line)