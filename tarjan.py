import random

index = 1
count = 0
stack = []
connected_comps = []

def tarjan_SCC(adj_list):
	N = len(adj_list) - 1
	global indices, lowest_link, is_onstack
	global connected_comps, index, count
	connected_comps = []
	stack = [] #Must reinitialize these things if called repeatedly
	index = 1 
	count = 0
	indices = [0]*(N+1) # Order in which nodes are visited
	is_onstack = [False]*(N+1) # Boolean array to check whether a node is on the stack or not
	lowest_link = [0]*(N+1) # Lowest index that is accessible from a given node

	for i in range (1, N+1):
		if indices[i] == 0:
			find_SCC(adj_list, i)
	return connected_comps

def find_SCC(adj_list, v):
	global index, count
	indices[v] = index # Assign a unique number to each index (visiting order)
	lowest_link[v] = index
	index = index + 1
	stack.append(v)	# Push the node onto the stack
	is_onstack[v] = True

	for w in adj_list[v]:
		if indices[w] == 0: # If the node has not been visited yet
			find_SCC(adj_list, w) # Recurse on that node
			lowest_link[v] = min(lowest_link[v], lowest_link[w]) # Since any node accessible from w is accessible from v
		elif is_onstack[w] == True: # If node has already been visited
			lowest_link[v] = min(lowest_link[w], indices[w]) # Update lowest_link[v]

	if lowest_link[v] == indices[v]: # Signals that we have found one SCC
		temp = -1
		connected_comps.append([]) # Add a new connected component to the output
		while temp != v: 
			temp = stack.pop() # Pop the nodes from the stack and add them to output
			is_onstack[temp] = False
			connected_comps[count].append(temp) 
		count = count + 1
	
	return

def color_code_edges(adj_list, nodes, edges, connected_comps):
	r = lambda:random.randrange(255)
	n = len(connected_comps)
	color_list = ['#%02X%02X%02X' % (r(), r(), r()) for i in range(n)] #Generating random colours
	for i in range(n):
		for j in connected_comps[i]:
			nodes[j].component = i #Assigning a node a component
			nodes[j].color = color_list[i] #Assigning a node a colour

	for m in edges:
		#Edge between 2 edges of a component
		if nodes[m.fro].component == nodes[m.to].component:
			m.color = color_list[nodes[m.fro].component] 
			m.style = 'solid'

		#Other edge
		else:
			m.color = 'black'
			m.style = 'dashed'

	return adj_list, nodes, edges

indices = []
lowest_link = []
is_onstack = []