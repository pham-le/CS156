#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 3, 10/27/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

import sys

RELATIONS = ['eq', 'ne', 'lt', 'gt']
def constraintsFromFile(filename):
    """
    Takes the lines from the problem file and returns a list of tuples representing the constraints in
    tuple form: (variable1, rel, variable or number).

    :param filename: name of file
    :return: list containing the constraints in the file
    """
    f = open(filename)
    constraints = []
    for line in f:
        if line != '\n':
            c = line.rstrip('\n').split() #c is a list with each word in the line
            if len(c) is not 3:
                print "ERROR: constraints must be 3 words long:"
                print c, "doesn't have 3 words"
                return []
            if c[1] not in RELATIONS:
                print "ERROR: second word must be a relation"
                print c[1], "is not a valid relation"
                return []
            if c[2].isdigit(): #change the third value to int if it is one.
                c[2] = int(c[2])
            constraints.append(tuple(c)) #turns the list to a tuple, add it to the list of constraints
    f.close()
    return constraints

def getInitialDomains(constraints):
    """Given a list of constraints, returns a dictionary that maps variables to lists of integers from 0 to max(D, V), 
    where D is the number of distinct variables and V is the max integer in a constraint."""
    v = 0 #represents highest integer value in any constraint
    variableSet = set() #set of variables in the problem
    for c in constraints:
        variableSet.add(c[0])
        if type(c[2]) is int:
            v = max(v, c[2])
        else:
            variableSet.add(c[2])
    d = len(variableSet)
    global_domain = range(max(d, v))
    domains = {}
    for variable in variableSet:
        domains[variable] = global_domain
    return domains


if len(sys.argv) is 3:
    problem_filename = sys.argv[1]
    use_forward_check_flag = sys.argv[2]
else:
    print "Invalid input. Please use the format:"
    print "python csp_solver.py problem_filename use_forward_check_flag"

# test to print the fucking file
constraints = constraintsFromFile(problem_filename)
domains = getInitialDomains(constraints)
print domains

# for line in readFile(problem_filename):
#     print "".join(line)