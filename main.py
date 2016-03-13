from graph import inp_graph,disp_graph
import tarjan
from animation import start_animation
import sys

#input from file specified as command line arguement

if(len(sys.argv)==2):
	test_graph = open(sys.argv[1] ,'r')
else:
	test_graph= sys.stdin

graph, nodes, edges = inp_graph(test_graph)
disp_graph(graph, nodes, edges, 'Pictures/0')

n = tarjan.tarjan_SCC(graph, nodes, edges)

start_animation(n,'Pictures',0.5)

