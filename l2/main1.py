import os

import numpy as np
import pandas as pd

from model import Graph

DATA_DIR = 'data'
DATA_CSV = 'network.csv'
OUTPUT_DIR = 'outputs'
OUTPUT_DOT = 'graph.dot'

if __name__ == '__main__':
    df = pd.read_csv(os.path.join(DATA_DIR, DATA_CSV))
    edge_list = df.values

    g = Graph()
    g.addEdgesFromList(edge_list)
    g.saveGraph(os.path.join(OUTPUT_DIR, OUTPUT_DOT))
