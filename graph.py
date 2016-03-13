""" Graph utility functions """

"""
Graphs are adjacency lists with the vertices numbered from 1 to n, where n is the number of vertices.

Each element v ,in the list indexed at u, is a vertex and it indicates a directed edge from u to v.

"""

import graphviz
import sys
from graphviz_elements import graphviz_node as gz_node
from graphviz_elements import graphviz_edge as gz_edge
from gzutilities import apply_styles

""" 
Function for getting the graph from file.

--------------------------------------------
File format:

n m 
u1 v1 
u2 v2
...
...
um vm

where, 

n-> number of vertices m-> number of edges
ui vi -> indicates a direct edge from ui to vi
----------------------------------------------

Function returns graph,number of vertices,number of edges,nodes(includes the UI properties of each node in graph)

"""

def inp_graph(inp=sys.stdin):

    n, m = map(int, inp.readline().split())

    g = [[] for _ in range(n+1)]

    nodes = [None]
    edges = {}

    # Creating an array of gz_nodes to keep track of each nodes's properties

    for i in xrange(1,n+1):
        nodes.append(gz_node(key = str(i), label = str(i), xlabel = ''));

    # Creating an array of gz_edges to keep track of each edge's properties

    for i in range(m):
        u, v= map(int, inp.readline().split())
        g[u].append(v)
        edges[(u,v)] = gz_edge(fro = u, to = v)

    return g, nodes, edges

""" Function for displaying the graph using Graphviz """
""" Renders image to filename.png """

def disp_graph(graph, nodes, edges, filename="gviz_out"):

    dot = graphviz.Digraph(comment="Tarjan Graph", format='png')

    for n in nodes[1:]:
            dot.node(n.key, **n.UI_properties())

    for e in edges.values():
            dot.edge(str(e.fro), str(e.to), **e.UI_properties())
    dot = apply_styles(dot)
    dot.render(filename,view=False)
