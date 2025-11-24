#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 00:52:31 2025

@author: seanfaulkner
"""

import numpy as np

def myLU3(A):
    """ Takes a 3x3 numpy array and computes its
    LU decomposition without partial pivoting
    and assuming that no row swaps are required. """
    if A.shape != (3, 3):
        raise ValueError("Input must be a 3x3 matrix.")
    
    L = np.identity(3)
    U = np.zeros((3, 3))

    # Row 1 of U
    U[0, 0] = A[0, 0]
    U[0, 1] = A[0, 1]
    U[0, 2] = A[0, 2]

    # First column of L
    L[1, 0] = A[1, 0] / U[0, 0]
    L[2, 0] = A[2, 0] / U[0, 0]

    # Row 2 of U
    U[1, 1] = A[1, 1] - L[1, 0] * U[0, 1]
    U[1, 2] = A[1, 2] - L[1, 0] * U[0, 2]

    # L[2,1]
    L[2, 1] = (A[2, 1] - L[2, 0] * U[0, 1]) / U[1, 1]

    # Row 3 of U
    U[2, 2] = A[2, 2] - L[2, 0] * U[0, 2] - L[2, 1] * U[1, 2]

    return L, U


A = np.array([[1.,2.,-1.],[-2.,-5.,3.],[-1.,-3.,0.]])
L, U = myLU3(A)
print(f"Is L in the correct form? {np.allclose(np.triu(L),np.eye(3))}")
print(f"Is U in the correct form? {np.allclose(U,np.triu(U))}")
print(f"Do L and U multiply to A? {np.allclose(L @ U, A)}")