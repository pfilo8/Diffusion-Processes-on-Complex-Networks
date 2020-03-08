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


def plot_trajectory(x, y):
    plt.figure()
    plt.scatter(x, y)
    plt.show()
