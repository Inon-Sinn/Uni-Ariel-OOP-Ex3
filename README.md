# Graph Project in course OOP with python!

### About

In this assignment we were given a json file and had using it, to implement a Directed weighted graph using the given Interfaces.
In Addition we were given a list of algorithms that we had to implement and then showcase all of it using GUI.

## Implemented Algorithms

for Information about the implemented algorithms: center, tsp, shortestPath, click here:</br>
[Implemented Algorithms](https://github.com/Inon-Sinn/Uni-Ariel-OOP-Ex3/wiki/Algorithms/_edit)

## Interfaces and Classes

|Interfaces| Descripition |
| ---------- | --------- |
| GraphInterfave | interface for a Directed Weighted Graph|
| GraphAlgoInterface  |  an Interface with the algorithms written above |


|Classes| Descripition |
| ---------- | --------- |
| GraphInterfave | interface for a Directed Weighted Graph |
| GraphAlgoInterface  |  an Interface with the algorithms that can ve used on a Graph |

### UML

[alt text](https://github.com/Inon-Sinn/Uni-Ariel-OOP-Ex3/blob/master/src/Ex3.png)
 
## Runtime of the Algorithms: Python VS Java

__Python:__
| NodeSize | Center  | TSP (5 nodes)| shortestPath | LoadJson | SaveJson |
| ---------- | --------- |--------- | --------- |--------- | --------- |
| A0     |2 ms |3 ms  |0 ms  |0 ms  |3 ms   |
| A1     |4 ms |2 ms  |1 ms  |1 ms  |3 ms   |
| A2     |12 ms|3 ms  |0 ms  |1 ms  |7 ms   |
| A3     |38 ms|11 ms |2 ms  |1 ms  |7 ms   |
| A4     |19 ms|4 ms  |2 ms  |1 ms  |3 ms   |
| A5     |36 ms|8 ms  |2 ms  |1 ms  |5 ms   |
| 1000   |33 s |313 ms|58 ms |38 ms |196 ms |
| 10000  |     |4 s   |573 s |421 ms|2 s    |
| 100000 |     |      |15.1 s|10.5 s|45 s   |

#### Java:
| NodeSize| center |TSP (5 nodes)|shortestPath|LoadJson|SaveJson|
| ---------- | --------- |--------- | --------- |--------- | --------- |
| G1      |5.57 ms          |7 ms    |0.245 ms|157 ms|320 ms|
| G2      |11.75 ms         |4.25 ms |0.155 ms|41 ms |11 ms|
| G3      |10.5 ms          |20.5 ms |0.435 ms|13 ms |26 ms|
| 1,000   |6s               |176 ms  |8.53 ms |240 ms|210 ms|
| 10,000  |aprox: 56.23 min |3.6 s   |337.4 ms|892 ms|581 ms|
| 100,000 |approx 52 days   |80 min  |45 s    |6.8 s |9.2 s|

<h1>GUI</h1>

<h2>GUI Instructional:</h2>
<h3>Mouse Interaction: </h5>
<p style="#2ac02a">When clicking Coordinates of the screen will be updated and displayed. This will replace "Coordinates:" 's place. If a node is clicked then its color will change to yellow.</p>
<h3>Buttons:</h4>
<h4>Add Edge:</h4> <p style="#2ac02a">Select two nodes with your mouse and click Add Edge. The first node is the source, and the second is the destination.</p>
<h4>Add Node:</h4> <p style="#2ac02a">click on the screen and then click Add Node to add a new node to the graph.</p>
<h4>Clean:</h4> <p style="#2ac02a">removes all the colors displayed.</p>
<h4>Center:</h4> <p style="#2ac02a">Click on Center to see the Center node of the graph (The node with the least maximal distance to all other nodes).</p>
<h4>ShortestPath:</h4> <p style="#2ac02a">Click on two nodes and then click on shortestPath to see the path with minimal distance to travel between source node to destination node.</p>
<h4>TSP:</h4> <p style="#2ac02a">Click on finite number of nodes, and then click TSP. This will present a path that visits all the given nodes at least once.</p>

### How to run the GUI
To Run the Gui directly from the Terminal enter the command python ``` Ex3.py <json file name> ``` , the json file will have to be in the data directory.<br/>
Example: ```python Ex3.py A5.json```

### Additional Visualization
![gui Description](https://github.com/Inon-Sinn/Uni-Ariel-OOP-Ex3/blob/master/Pictures/A2JsonGui.PNG)


<h1>Fin</h1> <p></p>
</br>

<h4>External Documents:</h4></br>
<a href="https://docs.google.com/document/d/15sTWy_pa6Vg4r7phAC322vZA169V02yezjxxf4b9sJc/edit">[docs]</a> <br />
<h4> Contributers:</h4></br>
<a href="https://github.com/Inon-Sinn">[Inon Sinn]</a><br />
<a href="https://github.com/Yannnyan">[Yan Naigebaver]</a><br />
<a href="https://github.com/Yaron-S">[Yaron Sirota]</a><br />
<br />
<h4> temp links for devs</h4></br>
![pygame docs](https://www.pygame.org/docs/) <br />
![Ex2 project](https://github.com/Inon-Sinn/Uni-Ariel-OOP-Ex2)


