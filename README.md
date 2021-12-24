# Oop3
_____________________________
## Najeeb Abdalla & Yehudit Brickner
__________________________


In this project we had to recreate the project Oop2 in python
<br>Here is a link to Oop2 https://github.com/Yehudit-Brickner/OOP2 this project was done in Java.

In this project we have 5 classes:
<br>node, edges, DiGraph, GraphAlgo and main
______________________________________________________
#### node
the node has a (x,y,z) coordinance Id, Tag and Dictionaries.

#### edges
the edge is made up of 2 nodes-src and dest and a weight.

#### DiGraph 
the DiGraph has 2 dictionaries, 1 for the nodes the other for the edges, it also has a mode counter.
<br>In this class we have functions for adding and removing nodes and edges and functions to get the data.

#### GraphAlgo
the GraphAlgo contains a DiGraph.
<br> this class has all the algorithms that we needed to implement
we needed to implement: get_graph, load_from_json, save_to_json, shortest_path, centerPoint, TSP, plot_graph
<br> to implement these function we were told to create a function for Dijsktras algorithm.
<br> here is a link explaing the algorithm https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
<br> we also created the functions isConnected and flipGraph to check if there is a center oint in the graph.

#### main
this class was given to us to make syre that we implemented all the functions
    
---------------------------
### running time of the functions
<br>

|   	      |shortestpath|center      |tsp (group of 5) |tsp (group of 20)|load    |      save|  
|:-----------:|:----------:|:----------:|:-------------:  |:---------------:|:------:|:--------:|
| 10 Nodes    | 1 ms       |1 ms        |     2ms         | ---            |  2 ms  |  2 ms    |             
| 100 Nodes   |  2 ms      |   1 ms     |1 ms (list not connected)|2 ms (list not connected)|  5 ms  |   5 ms    |
| 1000 Nodes  |87 ms       |1 min 33 sec|   630 ms        |2 sec 124 ms     |  235 ms|  235 ms  |
| 10000 Nodes |4 sec 748 ms|  ---    |22 sec 313ms     |1 min 29 sec     |2 sec 105 ms|2 sec 105 ms|
| 100000 Nodes|53 se 324 ms|   ---     |   ---    |   ---       |53 sec 324 ms|53 sec 324 ms|


---------------------------------
### uml of the classses
![uml](https://github.com/najeebWorld/Oop3/blob/main/uml.png)
