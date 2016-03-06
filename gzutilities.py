import graphviz as gv
import functools

graph = functools.partial(gv.Graph, format='png')
digraph = functools.partial(gv.Digraph, format='png')


""" Style attributes for the graph can be assigned here and can then be set using the apply_styles() function"""

style = {
    'graph': {
        'label': '',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#3F3F3F',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'circle',
        'fontcolor': 'black',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'style': 'bold',
        'color': 'black',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}

""" Concise function for adding nodes to the graph """
""" nodes-> array of tuples or just the array of vertex ids of the nodes"""
""" If array of tuples,then the first element indicates the id of the node and the second indicates the attributes 
of the node such as label,color etc """


def add_nodes(graph, nodes):

    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

""" To apply UI styles to the graph """

def apply_styles(graph, styles=style):

    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph