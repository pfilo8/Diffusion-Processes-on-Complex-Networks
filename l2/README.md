# Assignment 2

Implementation of the graph data structure is in file `model/Graph.py`. 
It contains all listed methods. 
Graph is build from Vertex which is represented as a seperate class in `model/Vertex.py` file.

Vertex contains `id` and `connectedTo` attributes. 
`Id` represents identifier of specific Vertex.
`connectedTo` represents all neighbours of specific Vertex.
It's a dictionary which values represents weights between nodes.
Other attributes are used only for BFS algorithm.

Results of previous graph saved to `*.dot` file is in `outputs/graph.dot`.

For the task 2 (calculating shortest path) I've used BFS algorithm.
To check implementatio I've used Carate Club dataset.
Result of the algorithm is in `outputs/karate_club_nn.csv`.
