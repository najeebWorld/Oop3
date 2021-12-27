# Oop3
_____________________________
## Najeeb Abdalla & Yehudit Brickner
__________________________


In this project we had to recreate the project Oop2 in python
<br>Here is a link to Oop2 https://github.com/Yehudit-Brickner/OOP2 this project was done in Java.
the main object of both of these project was to create a graph, and implement algorithms for the graph, and than make aGUI so that uo can see the graph.

______________________________________________________
# how to run the project

First you will need to make sure that you have python downloaded on your computer.
<br>If it isnt downloaded here is the link to download:
<br>python: https://www.python.org/downloads/
<br>Now that you have everything installed, download the project or clone this project.
<br>open up the project in pycharm or another python IDE's and run the main.
<br>in the main you can load other json files - just make sure to o=put the while oathif the file isnt part of the project)
<br> you can also change the values that you are looking for (example change the shortest path in line 77/79/81/83 to find the distance between other nodes)

___________________
## About this project:
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

