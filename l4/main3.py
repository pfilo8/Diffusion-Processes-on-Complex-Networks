import random

import numpy as np
import networkx as nx


def __get_neighbors(node):
    return list(node.keys())


def random_walk_on_graph(g, source_node, target_node, max_steps=1000):
    current_node = g[source_node]
    target_node = g[target_node]

    for i in range(max_steps):
        neighbors = __get_neighbors(current_node)
        current_node = g[random.choice(neighbors)]
        if current_node == target_node:
            return i
    return np.nan


def list_without_elements(n, *args):
    results = list(range(n))
    for arg in args:
        results.remove(arg)
    return results
