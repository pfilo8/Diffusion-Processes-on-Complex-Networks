import random
from itertools import combinations

import networkx as nx


def generate_random_graph(n, p):
    g = nx.Graph()
    for u, v in combinations(range(n)):
        if random.random() < p:
            g.add_edge(u, v)
    return g


def generate_connected_graph(n):
    return generate_random_graph(n, 0)


def generate_watts_strogatz(n, k, p):
    g = generate_ring_graph(n, k)
    edges = g.edges()
    for u, v in edges:
        if random.random() < p:
            possible_new_vertex = _list_without_elements(n, u, v)
            new_vertex = random.choice(possible_new_vertex)
            g.remove_edge(u, v)
            g.add_edge(u, new_vertex)
    return g


def generate_ring_graph(n, k):
    g = nx.Graph()
    nodes = list(range(n))
    for j in range(1, k // 2 + 1):
        targets = nodes[j:] + nodes[0:j]  # first j nodes are now last in list
        g.add_edges_from(zip(nodes, targets))
    return g


def _list_without_elements(n, *args):
    results = list(range(n))
    for arg in args:
        results.remove(arg)
    return results


def generate_barabasi_albert_graph(n, m):
    g = generate_connected_graph(m)
    for i in range(m + 1, n):
        probas = _calculate_probas(g)
        possible_vertex = range(0, i)
        selected_vertex = random.choices(possible_vertex, weights=probas)
        g.add_node(i, selected_vertex)
    return g


def _calculate_probas(g):
    degrees = list(dict(g.degree()).values())
    probas = [val / sum(degrees) for val in degrees]
    return probas
