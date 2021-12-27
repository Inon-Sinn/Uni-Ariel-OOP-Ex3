# Graph Project in course OOP with python!
### About

In this assignment we were given a json file and had using it, to implement a Directed weighted graph using the given Interfaces.
In Addition we were given a list of algorithms that we had to implement and then showcase all of it using GUI.

### Contents
We were given the files GraphInterface and GraphAlgoInterface and we started working from there:

#### GraphInterface - interface for directed weighted graphs

#### GraphAlgoInterface - interface for algorithms that run on graphs

Contains methods for loading files and saving them in a JSON file, computes the shortest path from one node to the other using [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), finds the node that has the shortest distance to its farthest node and plots the graph.

#### DiGraph - implements GraphInterface:

Inside the file we created the DiGraph object and Node object. We represented the edges of the graph by a python dictionary inside the Node class, which contains the destination of the edge (coming out of the node) and its weight. 

#### GraphAlgo - implements GraphALgoInterface:


#### GraphGui - contains methods for running the gui visual

### Additional Visualization
![alt text](https://github.com/Inon-Sinn/Uni-Ariel-OOP-Ex3/blob/master/src/Ex3.png)


###  External Documents:
[docs](https://docs.google.com/document/d/15sTWy_pa6Vg4r7phAC322vZA169V02yezjxxf4b9sJc/edit) <br />
### Contributers:
[Inon Sinn](https://github.com/Inon-Sinn)<br />
[Yan Naigebaver](https://github.com/Yannnyan) <br />
[Yaron Sirota](https://github.com/Yaron-S)
### temp links for devs
[pygame docs](https://www.pygame.org/docs/) <br />
[Ex2 project](https://github.com/Inon-Sinn/Uni-Ariel-OOP-Ex2)

