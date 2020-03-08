import os
import random

import matplotlib.pyplot as plt

N = 10
OUTPUT_DIR = os.path.join('outputs', 'tmp')
OUTPUT_NAME = '{i}.png'


def random_step():
    return random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])


def generate_plot(x, y, path):
    plt.figure()
    plt.plot([x], [y], 'ro')
    plt.xlim([-20, 20])
    plt.ylim([-20, 20])
    plt.savefig(path)


x = 0
y = 0

for i in range(N):
    x_step, y_step = random_step()
    x += x_step
    y += y_step
    generate_plot(x, y, os.path.join(OUTPUT_DIR, OUTPUT_NAME.format(i=i)))
