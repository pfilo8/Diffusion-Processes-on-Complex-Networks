import random
from itertools import combinations, product

from model import Graph


def generate_random_graph(n, p):
    g = Graph()
    for u, v in combinations(range(n), 2):
        if random.random() < p:
            g.addEdge(u, v)
    return g


def generate_connected_graph(n):
    return generate_random_graph(n, 1)


def generate_watts_strogatz(n, k, p):
    g = generate_ring_graph(n, k)
    edges = g.getEdges()
    for u, v in edges:
        if random.random() < p:
            try:
                possible_new_vertex = _list_without_elements(n, u.id, v.id)
                new_vertex = random.choice(possible_new_vertex)
                g.removeEdge(u.id, v.id)
                g.addEdge(u.id, new_vertex)
            except ValueError as e:
                continue
    return g


def generate_ring_graph(n, k):
    g = Graph()
    nodes = list(range(n))
    for j in range(1, k // 2 + 1):
        targets = nodes[j:] + nodes[0:j]  # first j nodes are now last in list
        g.addEdgesFromList(zip(nodes, targets))
    return g


def _list_without_elements(n, *args):
    results = list(range(n))
    for arg in args:
        results.remove(arg)
    return results


def generate_barabasi_albert_graph(n, m):
    g = generate_connected_graph(m)
    for i in range(m + 1, n+1):
        probas = _calculate_probas(g)
        selected_vertex = random.choices(list(probas.keys()), weights=list(probas.values()), k=1)
        g.addEdge(i, selected_vertex[0])
    return g


def _calculate_probas(g):
    degrees = g.getDegrees()
    suma = sum(degrees.values())
    toReturn = {node:degree/suma for node, degree in degrees.items()}
    return toReturn


def generate_2d_lattice(n, m):
    g = Graph()

    for i,j in product(range(n+1), range(m+1)):
        g.addVertex(f'{i},{j}')

    for i,j in product(range(n+1), range(m+1)):
        current_node = f'{i},{j}'
        g.addEdgeIfExists(current_node, f'{i+1},{j}')
        g.addEdgeIfExists(current_node, f'{i-1},{j}')
        g.addEdgeIfExists(current_node, f'{i},{j+1}')
        g.addEdgeIfExists(current_node, f'{i},{j-1}')
    return g
