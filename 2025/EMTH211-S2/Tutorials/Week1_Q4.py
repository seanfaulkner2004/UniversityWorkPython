import numpy as np

def rowSwapFunction(matrix, index):
    """Swaps rows round innit bruv"""
    current_row = index
    current_column = index
    while current_row < 3:
        if abs(matrix[current_row, current_column]) > abs(matrix[index,index]):
            temp = matrix[index].copy()
            matrix[index] = matrix[current_row]
            matrix[current_row] = temp
        current_row+=1
    return matrix

def rowReductionFunction(matrix, index):
    """Does row redcution, wagwan shawty"""
    pivot = matrix[index,index]
    current_row = index+1
    while current_row < 3:
        current_column = 0
        scalar = matrix[current_row,index]/pivot
        while current_column < 3:
            temp = matrix[current_row,current_column]
            matrix[current_row,current_column] = temp - (scalar*matrix[index,current_column])
            current_column+=1
        current_row+=1
    return matrix

def myRowEchelon(matrix, matrix_size):
    """Takes a 3x3 matrix and uses Gaussian elimination
       to find its row-reduced form."""
    for i in matrix_size:
        matrix = rowSwapFunction(matrix,i)
        matrix = rowReductionFunction(matrix,i)
    return matrix

def myRowEchelon3(matrix):
    """Takes a 3x3 matrix and uses Gaussian elimination
       to find its row-reduced form."""
    matrix = rowReductionFunction(matrix,0)
    matrix = rowReductionFunction(matrix, 1)
    return matrix

U = myRowEchelon3(np.array([[2., -1. , 1.],[-2., 3., -1.],[4., -15., 7.]]))
print(np.allclose(U,np.array([[2., -1., 1.],[0., 2., 0.],[0., 0., 5.]])))