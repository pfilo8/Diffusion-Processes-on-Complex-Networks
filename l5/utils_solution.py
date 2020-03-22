import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def execute_experiment(model, y0, t, args, plot=True):
    solution = odeint(model, y0, t, args=args)
    return solution
        
        
def generate_plot(t, solution, labels, show=True):
    plt.figure(figsize = (10, 6))
    
    for i in range(solution.shape[1]):
        plt.plot(t, solution[:, i], label=labels[i])
    
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    if show:
        plt.show()
    
    
def plot_phase_plane(ax, f, u_range, v_range, args=(), n_grid=100):
    u = np.linspace(u_range[0], u_range[1], n_grid)
    v = np.linspace(v_range[0], v_range[1], n_grid)
    uu, vv = np.meshgrid(u, v)

    # Compute derivatives
    u_vel = np.empty_like(uu)
    v_vel = np.empty_like(vv)
    for i in range(uu.shape[0]):
        for j in range(uu.shape[1]):
            u_vel[i,j], v_vel[i,j] = f(np.array([uu[i,j], vv[i,j]]), None, *args)

    speed = np.sqrt(u_vel**2 + v_vel**2)
    lw = 0.5 + 2.5 * speed / speed.max()

    ax.streamplot(uu, vv, u_vel, v_vel, linewidth=lw, arrowsize=1.2, density=1, color='thistle')

    return ax
