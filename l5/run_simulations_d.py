import logging
import os
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
import networkx as nx

from simulations.sir_on_graph import sir_model_on_network

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

PATH_BASEDIR = Path('results/d')

P = np.linspace(0, 1, 21)
N_STEPS = 1000
GRAPHS = {
    "lattice": {
        "generator": nx.grid_2d_graph,
        "args": {
            "m": 10,
            "n": 10
        }
    },
    "random": {
        "generator": nx.erdos_renyi_graph,
        "args": {
            "n": 100,
            "p": 0.5
        }
    },
    "watts_strogatz": {
        "generator": nx.watts_strogatz_graph,
        "args": {
            "n": 100,
            "k": 4,
            "p": 0.5
        }
    },
    "barabasi_albert":
        {
            "generator": nx.barabasi_albert_graph,
            "args": {
                "n": 100,
                "m": 4
            }
        }
}

PATH_BASEDIR.mkdir(parents=True, exist_ok=True)

for p, graph in product(P, GRAPHS):
    logging.info(f"Current graph: {graph}, current p: {p}")

    current_path = Path(PATH_BASEDIR).joinpath(f"{graph}").joinpath(f"p-{p}")
    current_path.mkdir(parents=True, exist_ok=True)

    for i in range(N_STEPS):
        generator = GRAPHS[graph]['generator']
        args = GRAPHS[graph]['args']
        starting_node = GRAPHS[graph].get('starting_node')

        g = generator(**args)
        results = sir_model_on_network(g, p, starting_node)
        results = pd.DataFrame(results)
        results_path = current_path.joinpath(f'{i}.csv')
        results.to_csv(results_path, index=False)
