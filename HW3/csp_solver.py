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
    """
    Checks if a temporary assignment for a variable satisfies all unary constraints.
    :param A: name of variable
    :param a: value
    :return: true if assignment satisfies unary constraints
    """
    for c in constraints:
        if type(c[2]) == int and c[0] == A:
            if c[1] == "eq" and a != c[2]:
                return False
            if c[1] == "ne" and a == c[2]:
                return False
            if c[1] == "lt" and a >= c[2]:
                return False
            if c[1] == "gt" and a <= c[2]:
                return False
    return True


def arcConsistent(A, a, B, b):
    """
    Checks if temporary assignments for two neighbors satisfy all binary constraints.
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


def backtrackingSearch():
    """
    Chooses values for one variable at a time and backtracks when a variable has no legal values left to assign.
    :return: a solution or failure
    """
    return backtrack({})


def backtrack(assignment):  # returns a solution, or failure
    """
    Keeps only a single representation of a state and alters that representation, if possible.
    :param assignment:
    :return: a solution or failure
    """
    if len(assignment) is len(domains):  # all variables are assigned
        return assignment

    """ this gets the first unassigned variable"""
    # var = ''  #do must implement MRV and degree heuristics
    # for variable in domains.keys():
    #     if variable not in assignment.keys():
    #         var = variable
    #         break

    """implementing MRV heuristic"""
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

    """degree heuristic to break ties"""
    if len(mrv_list) > 1:
        var = (mrv_list[0], 0) #start with first value as minimum neighbor length
        for variable in mrv_list:
            count = len(neighbors[variable])
            for neighbor in neighbors[variable]:
                if neighbor in assignment.keys(): #checks if neighbor is already assigned, minus 1 if true
                    count -= 1
            temp = (variable, count) #temp variable.. (variable name, number of unassigned neighbors)
            if temp[1] > var[1]: #checks which has a smaller amount of unassigned neighbors
                var = temp
    var = var[0]

    """least constraining value heuristic:
    Pick the value that rules out the fewest choices for the neighboring variables in the constraint graph."""
    orderedDomain = []
    for value in domains[var]:  #no ordering for now
        if isConsistent(var, value, assignment):
            assignment[var] = value
            old_domains = copy.deepcopy(domains[var])
            domains[var] = [value]
            #forward checking
            if use_forward_check_flag is 1:
                if(AC_3()):
                    result = backtrack(assignment)
                    if result != "NO SOLUTION":
                        return result
            #no forward checking
            else: 
                result = backtrack(assignment)
                if result != "NO SOLUTION":
                        return result
            print "domain of var before reversion", var, domains[var]
            domains[var] = old_domains
            print "domain of var after reversion", var, domains[var]
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

def AC_3():
    """
    Checks if every variable is arc consistent.
    :return: False if an inconsistency is found, True otherwise
    """
    queue = []
    for var in domains.keys(): #all arcs in the csp
        for neighbor in neighbors[var]:
            queue.append((var, neighbor))
    while queue != []:
        (X_i, X_j) = queue.pop()
        if revise(X_i, X_j):
            if len(domains[X_i]) is 0:
                return False
            for X_k in neighbors[X_i]:
                if (X_k != X_j):
                    queue.append((X_k, X_i)) # since X_i's domains change might affect X_k
    return True

def revise(X_i, X_j):
    """
    Revises the domain if, given two variables, they are arc consistent with each other,
    :param X_i: Variable 1
    :param X_j: Variable 2
    :return: True if and only if we revise the domain of X_i
    """
    revised = False
    for x in domains[X_i]:
        if all(not arcConsistent(X_i, x, X_j, y) for y in domains[X_j]): #and (not arcConsistent(X_j, y, X_i, x))) for y in domains[X_j]):
            print "removing domain entry!"
            domains[X_i].remove(x)
            revised = True
    return revised

def node_consistency():
    """Simple node-consistency algorithm to esure all domains are consistent with unary constraints"""
    for c in constraints:
        if type(c[2]) == int:
            if c[1] == "eq":
                domains[c[0]] = [c[2]]
            elif c[1] == "ne":
                domains[c[0]].remove(c[2])
            elif c[1] == "lt":
                for i in domains[c[0]]:
                    if i >= c[2]:
                        domains[c[0]].remove(i)
            elif c[1] == "gt":
                for i in domains[c[0]]:
                    if i <= c[2]:
                        domains[c[0]].remove(i)


if len(sys.argv) is 3:
    problem_filename = sys.argv[1]
    use_forward_check_flag = int(sys.argv[2])
else:
    print "Invalid input. Please use the format:"
    print "python csp_solver.py problem_filename use_forward_check_flag"

constraints = constraintsFromFile(problem_filename)  # list of tuples in the form: (var, rel, var or num)
domains = getInitialDomains(constraints) # map from variables to domain
neighbors = getNeighbors(constraints)
node_consistency()


# ##------Test Statements Below THIS LINE-------###

print sorted(backtrackingSearch())
