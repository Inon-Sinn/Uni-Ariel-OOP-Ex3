# Graph Project in course OOP with python!
### About

In this assignment we were given a json file and had using it, to implement a Directed weighted graph using the given Interfaces.
In Addition we were given a list of algorithms that we had to implement and then showcase all of it using GUI.

### Contents
We were given the files GraphInterface and GraphAlgoInterface and we started working from there:
#### GraphInterface - interface for directed weighted graphs:
v_size: returns the number of vertices in this graph
e_size: returns the number of edges in this graph
get_all_v: returns all the nodes in the Graph
all_in_edges_of_node: returns all the nodes connected to (into) given node
all_out_edges_of_node: returns all the nodes connected to (out of) given node
get_mc: returns the current version of this graph
add_edge: adds an edge to the graph
add_node: adds a node to the graph
remove_node: removes node from graph
remove_edge: removes edge from graph
#### GraphAlgoInterface - interface for algorithms that run on graphs:
get_graph: returns the directed graph on which the algorithm works on
load_from_json: loads a graph from a json file
save_to_json: saves the graph in JSON format to a file
shortest_path: returns the shortest path from one node to another using Dijkstra's Algorithm
TSP: finds the shortest path that visits all the nodes in the list
centerPoint: finds the node that has the shortest distance to it's farthest node
plot_graph: plots the graph
#### DiGraph - implements GraphInterface:
Inside the file we created the DiGraph object and Node object. We represented the edges of the graph by a python dictionary inside the Node class, which contains the destination of the edge (coming out of the node) and its weight. 
#### GraphAlgo - implements GraphALgoInterface:
Contains methods for loading files and saving them in a JSON file, computes the shortest path from one node to the other using Dijkstra's algorithm, finds the node that has the shortest distance to its farthest node and 
#### | GraphGui | contains methods for running the gui visual

### How to run


### Additional Visualization
-----------------


###  External Documents:
[docs](https://docs.google.com/document/d/15sTWy_pa6Vg4r7phAC322vZA169V02yezjxxf4b9sJc/edit) <br />
### Contributers:
[Innon]()<br />
[Yan](https://github.com/Yannnyan) <br />
[Yaron]()
### temp links for devs
[pygame docs](https://www.pygame.org/docs/) <br />
[Ex2 project](https://github.com/Inon-Sinn/Uni-Ariel-OOP-Ex2)

