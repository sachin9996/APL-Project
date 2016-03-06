""" Graph utility functions """

"""
Graphs are adjacency lists with the vertices numbered from 1 to n, where n is the number of vertices.

Each element v ,in the list indexed at u, is a vertex and it indicates a directed edge from u to v.

"""

import graphviz
import sys
from graphviz_node import graphviz_node as gz_node
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

    g= [[] for _ in range(n+1)]
    nodes=[]

    # Creating an array of gz_nodes to keep track of each nodes's UI properties

    for i in xrange(1,n+1):
        x=gz_node(str(i),str(i),'');
        nodes.append((x.id,x.properties()))

    # print nodes

    for i in range(m):
        u, v= map(int, inp.readline().split())
        g[u].append(v)

    return g, n, m, nodes

""" Function for displaying the graph using Graphviz """
""" Renders image to filename.png """

def disp_graph(graph,nodes,filename="gviz_out"):

    dot = graphviz.Digraph(comment="Tarjan Graph", format='png')

    n = len(graph)

    for k in nodes:
            dot.node(k[0], **k[1])

    for i in xrange(1,n):
        for j in graph[i]:
                dot.edge(str(i), str(j))
    dot = apply_styles(dot)
    dot.render(filename,view=True)
