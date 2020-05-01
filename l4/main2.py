import os

import numpy as np
import matplotlib.pyplot as plt


def random_step():
    angle = 2 * np.pi * np.random.random()
    return np.cos(angle), np.sin(angle)


def generate_trajectory(n):
    values = np.array([random_step() for _ in range(n)])
    x = np.cumsum(values[:, 0])
    y = np.cumsum(values[:, 1])
    return x, y


def animate_trajectory(x, y):
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
        
    xlims = [min(x), max(x)]
    ylims = [min(y), max(y)]
        
    for idx, iks, igrek in zip(range(len(x)), x, y):
        plt.figure()
        plt.grid()
        
        plt.scatter([iks], [igrek])
        plt.xlim(xlims)
        plt.ylim(ylims)
        
        filepath = os.path.join('tmp', f'{idx}.png')
        plt.savefig(filepath)
                               