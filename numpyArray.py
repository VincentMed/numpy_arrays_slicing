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
myArray = np.arange(21).reshape(3,7)

# test
print(np.arange(21).reshape(3,7))

# row 2 of A
row_two = myArray[1]
print(row_two)

# print the above reversed
rev = myArray[1]
print(rev[::-1])

# sub matrix, bottom right 2x2
two_by_two = myArray[1, 5:7], myArray[2, 5:7]
print(two_by_two)

# bottom left 2x2 array
bottom_left_array = myArray[1, 0:2], myArray[2, 0:2]
print(bottom_left_array)

#  3x3 sub-array in the middle of A
three_by_three = myArray[0, 2:5], myArray[1, 2:5], myArray[2, 2:5]
print(three_by_three)
