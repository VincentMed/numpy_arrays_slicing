# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:33:46 2022

@author: Vincent Medrano
"""
'''
Use numpy.array to define a 3-by-7 array, A.
In array location (i,j), row i, column j,  put the number i*j
Use slicing to produce and print:

1)  row 2 of A

2) row 2 of A in reverse order

3) the sub-matrix consisting or the bottom right 2x2 sub-array 

4) the sub-array consisting of the bottom left 2x2 sub-array

5) the 3x3 sub-array in the middle of A
'''

import numpy as np

# create an array with 3 rows and 7 columns.
A = np.arange(21).reshape(3,7)

# test
print(np.arange(21).reshape(3,7))

# row 2 of A
row_two = A[1]
print(row_two)

# print the above reversed
rev = A[1]
print(rev[::-1])

# sub matrix, bottom right 2x2
two_by_two = A[1, 5:7]
two_by_two_b = A[2, 5:7]
print(two_by_two)
print(two_by_two_b)


# bottom left 2x2 array
bottom_left_array = A[1, 0:2]
bottom_left_array_b = A[2, 0:2]
print(bottom_left_array)
print(bottom_left_array_b)

#  3x3 sub-array in the middle of A
three_by_three = A[:,2:5]
print(three_by_three)
