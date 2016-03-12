from graph import inp_graph,disp_graph
import tarjan

test_graph = open('test_graph1', 'r')
graph, nodes, edges = inp_graph(inp = test_graph)
disp_graph(graph, nodes, edges, '1')

cc = tarjan.tarjan_SCC(graph)
scc_graph, scc_nodes, scc_edges = tarjan.color_code_edges(graph, nodes, edges, cc)
disp_graph(scc_graph, scc_nodes, scc_edges, '2')

print scc_graph
print cc