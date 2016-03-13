from graph import inp_graph,disp_graph
import tarjan
from animation import start_animation

graph, nodes, edges = inp_graph()
disp_graph(graph, nodes, edges, 'Pictures/0')

n = tarjan.tarjan_SCC(graph, nodes, edges)

start_animation(n,'Pictures',0.5)

