#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 3, 10/27/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

import sys
import copy


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
    :return: a dictionary of domains for each variable
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

def getNeighbors(constraints):
    """
    A dict of {var:[var,...]} that for each variable lists the other variables that participate in constraints.
    :param constraints: list of original constraints
    :return: a dictionary of neighbors for each variable
    """
    neighbors = {}
    for variable in domains.keys():
        vars = set()
        for c in constraints:
            if c[0] == variable and type(c[2]) is not int: #this does not work.. example SA does not get all its neighbors
                vars.add(c[2])
            elif c[2] == variable: #this works
                vars.add(c[0])
        neighbors[variable] = list(vars)
    return neighbors

def nodeConsistent(A, a):
    for c in constraints:
        if type(c[2]) is int:
            if c[1] == "eq" and a != c[2]:
                return False
            if c[1] == "ne" and a == c[2]:
                return False
            if c[1] == "lt" and a >= c[2]:
                return False
            if c[1] == "gt" and a <= c[2]:
                return False
    return True

# constraints method experimental for now.
def arcConsistent(A, a, B, b):
    """
    Returns true if neighbors A, B satisfy the constraint when they have values A=a, B=b.
    :param A: name of Neighbor A
    :param a: value of Neighbor A
    :param B: name of Neighbor B
    :param b: value of Neighbor B
    :return: true if assignment satisfies the constraints
    """
    for c in constraints:
        if c[0] == A and c[2] == B:
            if c[1] == "eq" and a != b:
                return False
            if c[1] == "ne" and a == b:
                return False
            if c[1] == "lt" and a >= b:
                return False
            if c[1] == "gt" and a <= b:
                return False
    return True


def backtrackingSearch():  # returns a solution, or a failure
    return backtrack({})


def backtrack(assignment):  # returns a solution, or failure
    if len(assignment) is len(domains):  # all variables are assigned
        return assignment

    """ this gets the first unassigned variable, in case my MRV code doesn't work"""
    # var = ''  #do must implement MRV and degree heuristics
    # for variable in domains.keys():
    #     if variable not in assignment.keys():
    #         var = variable
    #         break

    """implementing MRV"""
    mrv_list = [] #list of variables tied for the minimum remaining values
    var = ('', 10000000) #represents the var with minimum size so far, and its size (var, len(domain))
    for variable in domains.keys():
        if variable not in assignment.keys():
            temp = (variable, len(domains[variable]))
            if temp[1] == var[1]:
                mrv_list.append(temp[0])
            if temp[1] < var[1]:
                mrv_list = []
                var = temp
                mrv_list.append(var[0])
    print mrv_list

    """implementing degree heuristic to break MRV ties"""
    var = (mrv_list[0], len(neighbors[mrv_list[0]])) #start with first value as minimum neighbor length
    for variable in mrv_list:
        if len(neighbors[variable]) > var[1]:
            var = (variable, len(neighbors[variable]))

    var = var[0]


    #do ORDERING.. least-constraining-value heuristic
    orderedDomain = []
    for value in domains[var]:  #no ordering for now
        if isConsistent(var, value, assignment):
            assignment[var] = value
            #forward checking
            result = backtrack(assignment)
            if result != "NO SOLUTION":
                return result
        if var in assignment.keys():
            del assignment[var]
    return "NO SOLUTION"

def isConsistent(var, val, assignment):
    """
    Checks if a potential assignment is consistent.
    :param var: Variable name
    :param val: Value to be assigned
    :return: True if consistent, False if inconsistent
    """
    #check unary constraints
    if not nodeConsistent(var, val):
        return False

    #checks binary constraints
    for var2 in domains.keys():
        if var2 in assignment and var != var2:
            if not arcConsistent(var, val, var2, assignment[var2]) or not arcConsistent(var2, assignment[var2], var, val):
                return False
    return True

def AC_3(domain): #returns false if an inconsistency is found, true otherwise
    return

def revise(domain, X_i, X_j): #returns true iff we revise the domain of X_i
    revised = False
    for x in domain[X_i]:
        for y in domain[X_j]:
            #check both ways???
            if not constraintFunction(X_i, x, X_j, y) and not constraintFunction(X_j, y, X_i, x):
                domain[X_i].remove(x)
                revised = True
    return revised


if len(sys.argv) is 3:
    problem_filename = sys.argv[1]
    use_forward_check_flag = sys.argv[2]
else:
    print "Invalid input. Please use the format:"
    print "python csp_solver.py problem_filename use_forward_check_flag"

constraints = constraintsFromFile(problem_filename)  # list of tuples in the form: (var, rel, var or num)
domains = getInitialDomains(constraints)  # map from variables to domain
neighbors = getNeighbors(constraints)


# ##------Test Statements Below THIS LINE-------###
print domains
print "Keys:", domains.keys()
print "Neighbors:", neighbors
print backtrackingSearch()