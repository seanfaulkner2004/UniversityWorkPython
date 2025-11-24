#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:52:08 2024

@author: seanfaulkner
"""

def newton_root_finder(f, f_prime, x0, tolerance, max_iterations):
    """Finds an approximate root of f(x) using the Newton-Raphson method.
    Initial x = x0.
    Returns approximation x when abs(f(x)) < tolerance AND
    abs(change in approximation) < tolerance in max_iterations or less.
    Otherwise raises a RuntimeError.
    """
    x = x0
    i = 0
    is_converged = False
    while (not is_converged) and (i < max_iterations):
        x_new = x-(f(x)/f_prime(x))
        is_converged = abs(f(x_new)) < tolerance and abs(x_new-x) < tolerance                           
        x = x_new
        i += 1
    if not is_converged:
        msg = "Max iterations reached without convergence"
        msg += " in newton_root_finder."
        raise RuntimeError(msg)
    return x

f = lambda x: x**3 + x + 1
f_prime = lambda x: 3 * x**2 + 1
x0 = -1
tol = 0.5e-3
max_iterations = 20
try:
    root = newton_root_finder(f, f_prime, x0, tol, max_iterations)
    print(f"Root found {root:.6f} (6 dps)")
except RuntimeError as err:
    print(err)

def newton_reciprocal(a, x0, tolerance, max_iterations):
    """Calculate the reciprocal of a using Newton's method.
    Initial approximation x0,
    Returns x approx= 1/a when
    abs(change in approximation) < tolerance in max_iterations or less.
    Otherwise raises a RuntimeError.
    """
    x = x0
    i = 0
    is_converged = False
    while (not is_converged) and (i < max_iterations):
        # get x_new from recursion formula shown in tutorial!
        x_new =  x*(2-a*x)       
        is_converged = (abs(x - x_new) < tolerance)
        x = x_new
        i += 1
    if not is_converged:
        msg = "Max iterations reached without convergence"
        msg += " in newton_reciprocal."
        raise RuntimeError(msg)
    return x

a = 17
x0 = 0.1
tol = 0.5e-9
max_iterations = 20
root = newton_reciprocal(a,
                         x0,
                         tol,
                         max_iterations)
print(f"a = {a}")
print(f"Reciprocal = {root:.9f} (9 dps)")