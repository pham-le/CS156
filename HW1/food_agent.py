#!/usr/bin/python
#CS 156 Intro to AI - 01
#Homework 1, 09/15/2014
#Andres Chorro		- 007340983
#Jannette Pham-Le	- 007855120
#Justin Tieu		- 007789678


from Queue import PriorityQueue
import copy, sys

#Stores a node
#state: the list of list of characters representing the current state of the map
#path_cost: the cost from the initial state to this space
#h_cost: the hueristic cost from this point to the goal
#agent: the coordinates of the agent
class Node:
	def __init__(self, state, path_cost, h_cost, agent):
		self.state = state
		self.path_cost = path_cost
		self.h_cost = h_cost
		self.agent = agent

#Creates a list of lists of characters representing the problem map.
def initializeMap(filename):
	f = open(filename)
	problem = []
	for line in f:
	    char = list(line)
	    if line[len(line) - 1] == '\n':
	        char.pop() #remove newline if it's there
	    problem.append(char)
	f.close()
	return problem

#Gets the coordinates of a symbol.
def get_coords(c, map):
    y = 0
    for line in map:
        if c in line:
            x = line.index(c)
            if x != -1:  #found the symbol
                return (x, y)
        y = y + 1
    return (-1, -1)  #symbol not found

#print a map to console
def print_map(map):
	for line in map:
		print ''.join(line)

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

def find_moves(node):
	x = node.agent[0]
	y = node.agent[1]
	children = []

	#check north
	if (y - 1) >= 0 and node.state[y-1][x] in '.%':
		children.append((x,y-1))
	#check east
	if (x + 1) <= len(node.state[y]) - 1 and node.state[y][x+1] in '.%':
		children.append((x+1,y))
	#check south
	if (y + 1) <= len(node.state) - 1 and node.state[y+1][x] in '.%':
		children.append((x,y+1))
	#check west
	if (x - 1) >= 0 and node.state[y][x-1] in '.%':
		children.append((x-1,y))
	return children

#returns the node's state map, but with the agent moved to location parameter.
def update_map(node, location):
	ax, ay = node.agent
	lx, ly = location
	new_map = copy.deepcopy(node.state)

	#agent has moved, insert empty space ('.')
	new_map[ay][ax] = '.'
	#move agent to new location
	new_map[ly][lx] = '@'
	return new_map

#MAIN ALGORITHM
def a_star(input_h_type):
	node = Node(problem, 0, heuristic(problem, input_h_type), get_coords('@', problem))
	frontier = PriorityQueue()
	frontier.put((node.path_cost + node.h_cost, node)) #add tupple
	explored = set()
	node_map = {} #maps nodes to nodes, used to reconstruct path
	while True:
		if frontier.empty():
			print "The maze is unsolvable:"
			print_map(problem)
			return
		node = frontier.get()[1]
		if node.h_cost == 0: #goal-check
			print "Initial:" #Success
			i = 0
			for n in get_path_list(node_map, node): #print each node in solution path
				if i > 0:
					print
					print "Step %d:" % i
				print_map(n.state)
				i = i + 1
			print('Problem Solved! I had some noodles!')
			return
		explored.add(node.agent) #list of coordinates that have been explored
		for move in find_moves(node):
			new_state = update_map(node, move)
			child = Node(new_state, node.path_cost + 1, heuristic(new_state, input_h_type), move)

			#child is not in frontier or explored.  Put child in frontier.
			if (((child.h_cost + child.path_cost, child) not in frontier.queue) 
				and (child.agent not in explored)):
				frontier.put((child.path_cost + child.h_cost, child))
				node_map[child] = node

			#child is in frontier, with higher cost.  Replace with cheaper child.
			else:
				for node_tuple in frontier.queue:
					if (((node_tuple[1].agent) == child.agent)
						and node_tuple[0] > child.path_cost + child.h_cost):
						frontier.queue.remove(node_tuple)
						frontier.put((child.path_cost + child.h_cost, child))
						node_map[child] = node

def get_path_list(node_map, current):
	if current in node_map:
		partial = get_path_list(node_map, node_map[current])
		return partial + [current]
	else:
		return [current]


input_file = ""
input_h_type = -1
for arg in sys.argv:
	if('.txt' in arg):
		input_file = arg
	elif('manhattan' == arg):
		input_h_type = 1
	elif('euclidean' == arg):
		input_h_type = 2
	elif('made_up' == arg):
		input_h_type = 3

problem = initializeMap(input_file)
gx, gy = get_coords('%', problem)
a_star(input_h_type)