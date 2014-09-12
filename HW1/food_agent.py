#!/usr/bin/python
#CS 156 Intro to AI - 01
#Homework 1, 09/15/2014
#Andres Chorro, Jannette Pham-Le, Justin Tieu

from Queue import PriorityQueue

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
	if type == 2: #Finds Euclidean distance
		return (((ax - gx) ** 2) + ((ay - gy) ** 2)) ** .5
	if type == 3: #Finds specialllsllLLkfsjd
		return -1
	else:
		return -1

"""MAIN ALGORITHM
node = (problem, 0, heuristic(1, map))
frontier = PriorityQueue()
frontier.put(node[1] + node[2], node)
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
	#Need to find possible paths, and iterate through them.
"""



print problem
print heuristic(2, problem)
print get_coords('@', problem)