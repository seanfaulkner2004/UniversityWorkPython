"""PLOT VALUES"""

import math
import matplotlib.pyplot as plt

def generate_x_values(start, end, num_values):
    """welfjnsklderfglkhjkj"""
    new_list = []
    increase = (end-start)/(num_values-1)
    for num in range(0,num_values):
        x_value = start + (increase * num)
        new_list.append(x_value)
    return new_list

def generate_y_values(x_values):
    """sdrg,jsdfkbhj"""
    new_list = []
    for x in x_values:
        y_value = 1/math.sqrt(2*math.pi)
        y_value = y_value*math.exp(-(x*x)/2)
        new_list.append(y_value)
    return new_list

def main():
    """lsdfglsdhjfb"""
    x_values = generate_x_values(-4.0, 4.0, 400)
    y_values = generate_y_values(x_values)
    axes = plt.axes()
    axes.plot(x_values, y_values)
    axes.grid(True)
    axes.set_title("A normal distribution, f(x), with mean = 0, variance = 1")
    axes.set_xlabel("x")
    axes.set_ylabel("f(x)")
    plt.show()


main()