import os
import pandas as pd
import networkx as nx

g = nx.karate_club_graph()

pd.DataFrame(g.edges, columns=['Source', 'Target']).to_csv(os.path.join('data', 'karate.csv'), index=False)
