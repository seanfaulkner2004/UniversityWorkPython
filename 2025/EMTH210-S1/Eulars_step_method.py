"""Eular's step method"""

import numpy as np
import matplotlib.pyplot as plt

def euler_step(dydt, t0, y0, h):
    """One step of Euler's method.
    DE function dydt(t, y), initial t = t0, initial y = y0, step size = h.
    Return y1 = y0 + h*f(t0,y0) at end of step.
    """
    dydt_value = dydt(t0, y0)
    y1 = y0 + (h*dydt_value) 
    
    return y1


def eulers_method_n_steps_t_final(dydt, t0, y0, tf, n_steps):
    """Do n_steps steps of Euler's method from t0 to tf.
    DE function dydt(t, y), initial t = t0, initial y = y0,
    to final t tf, n_steps steps.
    Return numpy arrays of t and y values.
    """
    t_values = np.linspace(t0, tf, n_steps+1 )
    y_values = np.zeros(n_steps + 1)
    h = (tf - t0) / n_steps
    y_values[0] = y0
    y = y0
    for i_step in range(n_steps):
        t = t_values[i_step]
        y = euler_step(dydt, t, y, h)
        y_values[i_step+1] = y
        
    return t_values, y_values

def solve_DE():
    """Perform several iterations of Euler's method
    and return the Euler's Method solution.
    """

    # DE Function
    dydt = lambda t, y: (3*y/t**2)-(y/5)

    # Initial conditions
    t0 = 1
    y0 = 4

    # number of steps and final t
    n_steps = 25
    t_final = 6

    # Eulers method
    t_values, y_values = eulers_method_n_steps_t_final(dydt,
                                                       t0,
                                                       y0,
                                                       t_final,
                                                       n_steps)

    return t_values, y_values

def plot_DE():
    """srgjbrwehjbgvsdfhb"""
    t_values, y_values = solve_DE()
    axes = plt.axes()
    axes.plot(t_values,y_values,linestyle='',color='darkblue',marker='o')
    axes.grid(True)
    axes.set_xlabel('t')
    axes.set_ylabel('y')
    axes.set_title("Solution to a DE by Euler's method")
    plt.show()
    
def eulers_method_n_steps_list_t_final(dydt,t0,y0,t_final,n_step_values):
    """ljherjshb"""
    results = []
    for n_steps in n_step_values:
        t_values, y_values = eulers_method_n_steps_t_final(dydt,
                                                           t0,
                                                           y0,
                                                           t_final,
                                                           n_steps)
        results.append(y_values[-1])
    return results