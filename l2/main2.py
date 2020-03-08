import os

import numpy as np
import pandas as pd

from model import Graph

DATA_DIR = 'data'
DATA_CSV = 'karate.csv'
OUTPUT_DIR = 'outputs'
OUTPUT_CSV = 'karate_club_nn.csv'

if __name__ == '__main__':
    df = pd.read_csv(os.path.join(DATA_DIR, DATA_CSV))
    edge_list = df.values

    g = Graph()
    g.addEdgesFromList(edge_list)
    results = g.getShortestPath(7)
    results = pd.DataFrame(results.items(), columns=['id', 'distance'])
    results.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_CSV), index=False)
