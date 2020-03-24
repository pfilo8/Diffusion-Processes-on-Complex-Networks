# Assignment 2

Implementation of the graph data structure is in file `model/Graph.py`. 
It contains all listed methods. 
Graph is build from Vertex which is represented as a seperate class in `model/Vertex.py` file.

Vertex contains `id` and `connectedTo` attributes. 
`Id` represents identifier of specific Vertex.
`connectedTo` represents all neighbours of specific Vertex.
It's a dictionary which values represents weights between nodes.
Other attributes are used only for BFS algorithm.

Script `main1.py` contains task connected to saving graph from assignment list number 1 to dot representation.
Result is saved to `*.dot` file is in `outputs/graph.dot`.

For the task 2 (calculating shortest path) I've used BFS algorithm.
To check implementatio I've used Carate Club dataset.
Script `generate_karate_club_data.py` generates data from networkx library to `*.csv` representation which could use for our graph data structure.
Script generating results is in `main2.py`
Result of the algorithm is in `outputs/karate_club_nn.csv`.
