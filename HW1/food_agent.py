#!/usr/bin/python
#CS 156 Intro to AI - 01
#Homework 1, 09/15/2014
#Andres Chorro, Jannette Pham-Le, Justin Tieu

from Queue import PriorityQueue

class Node:
	def __init__(self, state, path_cost, h_cost, agent):
		self.state = state
		self.path_cost = path_cost
		self.h_cost = h_cost
		self.agent = agent

f = open("map.txt")
problem = f.readlines() #stores each line of the map as an element of the list
f.close()

#Gets the coordinates of a symbol.
def get_coords(c, map):
	y = 0
	for line in map:
		x = line.find(c)
		if x != -1: #found the symbol
			return (x, y)
		y = y + 1
	return (-1, -1) #symbol not found

gx, gy = get_coords('%', problem)

#Gets the specified heurist cost of the map:
#1 = Manhattan, 2 = Euclidean, 3 = Special Heuristic
def heuristic(map, type=1):
	agent = get_coords('@', map)
	ax, ay = agent
	if type == 1: #Finds Manhattan distance
		return abs(ax - gx) + abs(ay - gy)
	elif type == 2: #Finds Euclidean distance
		return (((ax - gx) ** 2) + ((ay - gy) ** 2)) ** .5
	elif type == 3: #Finds chess distance
		return max(abs(ax - gx), abs(ay - gy))
	else:
		return -1

def findMoves(node):
	x = node.agent[0]
	y = node.agent[1]
	children = []

	#check north
	if (y - 1) >= 0 and problem[y-1][x] in '.%':
		children.append((x,y-1))
		# children.append(Node(problem, node.path_cost + 1, heuristic()))
	#check east
	if (x+1) <= len(problem[0]) and problem[y][x+1] in '.%':
		children.append((x+1,y))
	#check south
	if (y + 1) <= len(problem) and problem[y+1][x] in '.%':
		children.append((x,y+1))
	#check west
	if (x-1) >= 0 and problem[y][x-1] in '.%':
		children.append((x-1,y))
	return children

def updateState(node, location):
	#agent has moved 
	node.state[node.agent[1]][node.agent[0]].replace('@', '.')
	#move agent to new location
	node.state[location[1]][location[0]].replace('.','@')
	return node.state

"""MAIN ALGORITHM
node = Node(problem, 0, heuristic(problem, 1), get_coords('@', problem))
frontier = PriorityQueue()
frontier.put(node.path_cost + node.h_cost, node)
explored = set()
while True:
	if frontier.empty():
		print "unsolvable"
		return #Failure, finish later
	node = frontier.get()
	if node[2] == 0: #goal-check
		print "solvable"
		return #Success
	explored.add(node)
	for move in findMoves(node):
		newState = updateState(node.map, node, move)
		child = Node(newState, node.path_cost + 1, heuristic(newState, 1), move)
"""


node = Node(problem, 0, heuristic(problem, 1), get_coords('@', problem))
print 'state:', node.state
print 'heuristic cost:', node.h_cost
print 'agent location:', node.agent
for move in findMoves(node):
	newState = updateState(node, move)
	child = Node(newState, node.path_cost + 1, heuristic(newState, 1), move)
