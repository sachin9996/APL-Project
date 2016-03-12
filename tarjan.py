import random
from graph import disp_graph

index = None
count = None
stack = None
filename = None
connected_comps = None
color = None
traversal_color = '0 1 1'

r = lambda a, b:random.randrange(a, b)*1.0/1000

def tarjan_SCC(graph, nodes, edges):
	N = len(graph) - 1
	global filename, connected_comps, index, count, color, stack
	color = str(r(300,1000)) + ' ' + str(r(800,1000)) + ' ' + str(r(800,1000))
	#color = '0.5 0.999 0.999'
	connected_comps = []
	stack = []
	index = 1 
	count = 0
	filename = 1
	for i in range (1, N+1):
		if nodes[i].index == 0:
			_find_SCC(graph, nodes, edges, i)

def _find_SCC(graph, nodes, edges, v):
	global index, count, color, filename
	nodes[v].index = index # Assign a unique number to each index (visiting order)
	nodes[v].lowest_link = index
	index = index + 1
	stack.append(v)	# Push the node onto the stack
	nodes[v].is_onstack = True
	nodes[v].color = traversal_color
	disp_graph(graph, nodes, edges, 'Pictures/'+str(filename))
	filename += 1

	for w in graph[v]:
		if nodes[w].index == 0: # If the node has not been visited yet
			nodes[w].color = traversal_color
			edges[v, w].color = traversal_color
			edges[v, w].style = 'dashed'
			_find_SCC(graph, nodes, edges, w) # Recurse on that node
			nodes[v].lowest_link = min(nodes[v].lowest_link, nodes[w].lowest_link) # Since any node accessible from w is accessible from v

		elif nodes[w].is_onstack == True: # If node has already been visited
			nodes[v].lowest_link = min(nodes[w].lowest_link, nodes[w].index) # Update nodes[v].lowest_link
			nodes[w].color = traversal_color
			edges[v, w].color = traversal_color
			edges[v, w].style = 'dashed'
			disp_graph(graph, nodes, edges, 'Pictures/'+str(filename))
			filename += 1	 

	if nodes[v].lowest_link == nodes[v].index: # Signals that we have found one SCC
		temp = -1
		connected_comps.append([]) # Add a new connected component to the output
		while temp != v: 
			temp = stack.pop() # Pop the nodes from the stack and add them to output
			nodes[temp].is_onstack = False
			connected_comps[count].append(temp)
			nodes[temp].component = count
			nodes[temp].color = color
		for u in connected_comps[count]:
			for v in graph[u]:
				if nodes[v].component == count:
					edges[(u,v)].color = color
					edges[(u,v)].style = 'solid'
				else:
					edges[(u,v)].color = 'black'
					edges[(u,v)].style = 'dotted'
		color = str(r(3,1000)) + ' ' + str(r(8,1000)) + ' ' + str(r(8,1000))
		count = count + 1
		disp_graph(graph, nodes, edges, 'Pictures/'+str(filename))
		filename += 1	
	return