import numpy as np
import matplotlib.pyplot as plt

def plot_flowrate(filename):
    """dskfjvadsfkjbvadkjh"""
    ys = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=2)
    xs = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=1)
    tick_labels = np.arange(1, 32, 5)
    tick_distance = np.linspace(100, 3100, 7)
    axes = plt.axes()
    axes.plot(xs,ys)
    axes.grid(True)
    axes.set_title(filename)
    axes.set_xlabel('day')
    axes.set_ylabel('m3/s')
    axes.set_xticks(tick_distance)
    axes.set_xticklabels(tick_labels)
    plt.show()