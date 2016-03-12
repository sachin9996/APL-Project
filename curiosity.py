import matplotlib.pyplot as plt
from graph import inp_graph,disp_graph
import tarjan
import random_graph
from random import randrange as r

x = []
y = []
sample_size = 1

for i in range(5,2000):
	l = 0
	for j in range(sample_size):
		random_graph.generate(i, i)
		test_graph = open('test_graph1', 'r')
		graph, nodes, edges = inp_graph(inp = test_graph)
		l += len(tarjan.tarjan_SCC(graph))
	l = l*1.0/sample_size
	print i, l
	x.append(i)
	y.append(l)

plt.scatter(x, y)
plt.show()

