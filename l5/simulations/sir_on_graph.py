import random
import networkx as nx

STATUS = 'status'

INFECTED = 'infected'
SUSCEPTIBLE = 'susceptible'
RECOVERED = 'recovered'


def sir_model_on_network(G, p, starting_node=None, max_iters=10000):
    init_susceptible(G)
    init_infected(G, starting_node)

    i = 0
    history = [get_status(G)]
    to_recover = []

    while any_infected(G) and i < max_iters:
        if to_recover:
            set_recovered(G, to_recover)

        infected_nodes = get_infected(G)
        to_infect = []
        for node in infected_nodes:
            for neighbor in get_susceptible_neighbors(G, node):
                if random.random() < p:
                    to_infect.append(neighbor)
        to_recover = get_infected(G)
        set_infected(G, to_infect)

        history.append(get_status(G))
        i += 1
    return history


def init_susceptible(G):
    nx.set_node_attributes(G, SUSCEPTIBLE, name=STATUS)


def init_infected(G, starting_node):
    first_infected_node = starting_node if starting_node else random.choice(list(G.nodes()))
    set_infected(G, [first_infected_node])


def any_infected(G):
    return INFECTED in nx.get_node_attributes(G, STATUS).values()


def get_infected(G):
    return [k for k, v in nx.get_node_attributes(G, STATUS).items() if v == INFECTED]


def get_susceptible_neighbors(G, node):
    return [v for v in G.neighbors(node) if G.nodes[v][STATUS] == SUSCEPTIBLE]


def get_status(G):
    return nx.get_node_attributes(G, STATUS)


def set_infected(G, infected_list):
    infected_nodes = {u: {STATUS: INFECTED} for u in infected_list}
    nx.set_node_attributes(G, infected_nodes)


def set_recovered(G, recovered_list):
    recovered_nodes = {u: {STATUS: RECOVERED} for u in recovered_list}
    nx.set_node_attributes(G, recovered_nodes)
