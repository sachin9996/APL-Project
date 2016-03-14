# Visualisation of Tarjan's Algorithm

CONTENTS OF THIS FILE
---------------------------------------------------------------------------------------
   
 * Introduction
 * Required Modules
 * Details of Other files in the folder
 * Execution
 * Contributors
 
 INTRODUCTION
 --------------------------------------------------------------------------------------
 
This project takes a directed graph as input, and produces a partition of the graph's vertices into the graph's strongly connected components using Tarjan's Algorithm. Each vertex of the graph appears in exactly one of the strongly connected components. Any vertex that is not on a directed cycle forms a strongly connected component all by itself:for instance, a vertex whose in-degree or out-degree is 0, or any vertex of an acyclic graph. 
 	
BASIC DESCRIPTION OF TARJAN'S ALGORITHM:

 	A depth-first search begins from an arbitrary start node (and subsequent depth-first searches are conducted on any nodes that have not yet been found). As usual with depth-first search, the search visits every node of the graph exactly once, declining to revisit any node that has already been explored. Thus, the collection of search trees is a spanning forest of the graph. The strongly connected components will be recovered as certain subtrees of this forest. The roots of these subtrees are called the "roots" of the strongly connected components. Any node of a strongly connected component might serve as the root, if it happens to be the first node of the component that is discovered by the search.
 	 
The output shows step by step animation of visiting each node, isolating the strongly connected components by visiting the nodes and shows the final output at the end.Nodes having the same color belong to the same component.

The running time of the algorithm is O(|V|+|E|), linear in both the number of edges and vertices of the graph.
 	
REQUIRED MODULES
--------------------------------------------------------------------------------------

Optional: Opencv to be installed for the library cv2 by typing the following command in the terminal : sudo apt-get install python-opencv

The library matplotlib is used if cv2 is not available.

The following external python modules/libraries are required to execute the program:

 	1.graphviz
 	2.matplotlib
 	3.random
 	4.functools
 	5.sys

DETAILS OF OTHER FILES IN THE FOLDER
---------------------------------------------------------------------------------------

animation.py:

It serves as a custom animation file for the program. It reads the graph images generated by tarjan.py and starts an animation sequence which displays the images in sequence at a fixed frame rate. It also has a function for slideshow viewing.
			
aux_data.py:

This is a file that has a class that can be expanded for storing more information that just the key at each node of the graph. It currently has only one string that is set to "test data" by default. Since an object of this class is included in every node of the graph, this ensures modularity of the code since the class can be populated with anything.

graph.py:

This file is for creating a graph from the given input and displaying it in the form of an image.It accepts input in the following format:

n m 
u1 v1 
u2 v2
...
...
um vm

where, 

n-> number of vertices m-> number of edges
ui vi -> indicates a direct edge from ui to vi
		
graphviz_elements.py:

It defines the classes for basic elements of the graph- edges and nodes with various information like label,colour,data,style,direction etc.
					
gzutilities.py:

It defines the style class for each node and edge. It defines some important functions required for the programs- adding nodes to the graph and applying UI styles to the graph.
			   
main.py:

This is the main function for the project. It calls other functions present in other modules. It takes input from the input file given as command line argument (default is standard input) and applies tarjan's algorithm on it and displays the final animated sequence showing the step-by-step working of the algorithm on the input graph.
		
random_graph.py:

Usage: python random_graph.py n <optional,default=10> m <optional,default=18> filename <optional,default=test_graph1>

n - number of vertices m - number of edges filename - file to write into

It generates a random graph with the given number of vertices and edges (given as command-line arguements) and writes it into 'filename' which can be then be used as a input file to the program. The default number of edges and nodes are 18 and 10 respectively. 

tarjan.py:

This file contains the program for running tarjan's algorithm on a graph. It generates graph images while visiting each new node with appropriate colours required for the animation.
		  
EXECUTION
---------------------------------------------------------------------------------------

The program should be executed in command line by the following command: python main.py input_file <optional,default=sys.stdin>
	
It takes the input graph specified through input file, given as command-line argument, and applies Tarjan's algorithm on it and displays the final result as a step by step animation of the working of the algorithm which finaly produces the graph with isolated strongly connected components. After this it goes into a slideshow mode where the user can navigate through the individual images using the arrow keys.


CONTRIBUTORS
--------------------------------------------------------------------------------------

Sachin Sridhar
Roll no:CS14B057

Girish Raguvir J
Roll no:CS14B059

K.R.Prabu
Roll no:CS14B048

--------------------------------------------------------------------------------------

THE END
 
		 
