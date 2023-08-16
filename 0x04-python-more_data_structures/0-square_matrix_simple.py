#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    now = []
    for i in matrix:
        now.append(list(map(lambda i: i**2, i)))
    return (now)
