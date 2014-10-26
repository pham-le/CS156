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
    Takes the lines from the problem file and returns a list of tuples representing the constraints in tuple form:
    (variable1, rel, variable or number).
    :param filename: name of file
    :return: list containing the constraints in the file
    """
    f = open(filename)
    constraints = []
    for line in f:
        if line != '\n':
            c = line.rstrip('\n').split()  # c is a list with each word in the line
            if len(c) is not 3:
                print "ERROR: constraints must be 3 words long:"
                print c, "doesn't have 3 words"
                return []
            if c[1] not in ['eq', 'ne', 'lt', 'gt']:
                print "ERROR: second word must be a relation"
                print c[1], "is not a valid relation"
                return []
            if c[2].isdigit():  # change the third value to int if it is one.
                c[2] = int(c[2])
            constraints.append(tuple(c))  # turns the list to a tuple, add it to the list of constraints
    f.close()
    return constraints


def getInitialDomains(constraints):
    """
    Given a list of constraints, returns a dictionary that maps variables to lists of integers from 0 to max(D, V),
    where D is the number of distinct variables and V is the max integer in a constraint.
    :param constraints: list of original constraints
    :return: a dictionary
    """
    v = 0  # represents highest integer value in any constraint
    variableSet = set()  # set of variables in the problem
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


# constraints method experimental for now.
def constraintFunction(A, a, B, b):
    """
    Returns true if neighbors A, B satisfy the constraint when they have values A=a, B=b.
    :param A: name of Neighbor A
    :param a: value of Neighbor A
    :param B: name of Neighbor B
    :param b: value of Neighbor B
    :return: true if assignment satisfies the constraints
    """
    for c in constraints:
        if c[0] == A:
            if type(c[2]) is int:
                if c[1] == "eq":
                    if a != c[2]:
                        return False
                elif c[1] == "ne":
                    if a == c[2]:
                        return False
                elif c[1] == "lt":
                    if a >= c[2]:
                        return False
                elif c[1] == "gt":
                    if a <= c[2]:
                        return False
            elif c[2] == B:
                if c[1] == "eq":
                    if a != b:
                        return False
                if c[1] == "ne":
                    if a == b:
                        return False
                if c[1] == "lt":
                    if a >= b:
                        return False
                if c[1] == "gt":
                    if a <= b:
                        return False
    return True


def Backtracking_Search(csp):  # returns a solution, or a failure
    return Backtrack({}, csp)


def Backtrack(assignment, csp):  # returns a solution, or failure
    if len(assignment) is len(domains):  # all variables are assigned
        return assignment

    """ this gets the first unassigned variable, in case my MRV code doesn't work"""
    # var = ''  #do must implement MRV and degree heuristics
    # for variable in domains.keys():
    # if variable not in assignment.keys():
    # var = variable
    #         break

    """implementing MRV"""
    MRV, curr = ('', 10000000)  #(var name, number of values in the domain)
    for variable in domains.keys():
        if variable not in assignment.keys():
            curr = (variable, len(domains[variable]))
        if MRV[1] > curr[1]:
            MRV = curr
    var = MRV[1]

    #do ORDERING.. must implement the least-constraining-value heuristic == value that rules out the fewest choices for the neighboring variables in the constraint graph
    orderedDomain = []
    for value in domains[var]:  #no ordering for now
        #check if value consistent with assignment here
        assignment[var] = value
        inferences = False  #do forward checking here.. AC3
        #INFERENCES: return empty assignment or use forward checking (if allowed)

    return "NO SOLUTION"


if len(sys.argv) is 3:
    problem_filename = sys.argv[1]
    use_forward_check_flag = sys.argv[2]
else:
    print "Invalid input. Please use the format:"
    print "python csp_solver.py problem_filename use_forward_check_flag"

constraints = constraintsFromFile(problem_filename)  # list of tuples in the form: (var, rel, var or num)
domains = getInitialDomains(constraints)  # map from variables to domain
assignment = {}  # map from one variable to one value (the result)

# ##------Test Statements Below THIS LINE-------###
print domains
print "Keys:", domains.keys()
print constraintFunction('NT', 2, 'Q', 7)