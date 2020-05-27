import logging
import multiprocessing as mp
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
import networkx as nx

from simulations.qvoter_on_graph import qvoter_model_on_graph

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

PATH_BASEDIR = Path('results')

P = [0.5]
Q = [3, 4]
N_STEPS = 100
GRAPHS = {
    "complete": {
        "generator": nx.complete_graph,
        "args": {
            "n": 100
        }
    },
    "barabasi-albert": {
        "generator": nx.barabasi_albert_graph,
        "args": {
            "m": 4,
            "n": 100
        }
    },
    "watts_strogatz-1": {
        "generator": nx.watts_strogatz_graph,
        "args": {
            "n": 100,
            "k": 4,
            "p": 0.01
        }
    },
    "watts_strogatz-2": {
        "generator": nx.watts_strogatz_graph,
        "args": {
            "n": 100,
            "k": 4,
            "p": 0.2
        }
    }
}


def calculate(p, q, graph):
    logging.info(f"Current graph: {graph}, current p: {p}")

    current_path = Path(PATH_BASEDIR).joinpath(f"{graph}").joinpath(f"q-{q}").joinpath(f"p-{p}")
    current_path.mkdir(parents=True, exist_ok=True)

    for i in range(N_STEPS):
        generator = GRAPHS[graph]['generator']
        args = GRAPHS[graph]['args']

        g = generator(**args)
        results = qvoter_model_on_graph(g, p, q)
        results = pd.DataFrame(results)
        results_path = current_path.joinpath(f'{i}.csv')
        results.to_csv(results_path, index=False)


PATH_BASEDIR.mkdir(parents=True, exist_ok=True)

pool = mp.Pool(processes=8)

for p, q, graph in product(P, Q, GRAPHS):
    pool.apply_async(calculate, args=(p, q, graph))

pool.close()
pool.join()
