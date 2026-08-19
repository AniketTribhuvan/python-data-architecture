"""
Broadcasting Rules & Compatibility Checks
Focus: Trailing-dimension alignment, dimension expansion (1s padding), and ValueError handling.
"""

# Broadcasting allows NumPy to perform operations on arrays
# with different shapes without manually reshaping them.


# Broadcasting rules:
#
# Rule 1 — Dimensions are compared from right to left.
#
# Rule 2 — Two dimensions are compatible if:
#           - They are equal, OR
#           - One of them is 1.
#
# Rule 3 — If one array has fewer dimensions,
#          the missing dimensions are treated as 1.


import numpy as np


# Example 1: Broadcasting a 1D array with a 2D array.

arr = np.arange(4)
# Shape: (4,)

arr_2 = np.full((5, 4), 7)
# Shape: (5, 4)

# Compare shapes from right to left:
#
# arr:    (1, 4)
# arr_2:  (5, 4)
#          ↑  ↑
#
# 4 == 4  → Compatible
# Missing dimension of arr is treated as 1.
#
# Therefore, broadcasting is possible.

broadcast_arr = arr + arr_2

print(broadcast_arr.shape)
# (5, 4)


# Example 2: Broadcasting failure.

arr_3 = np.arange(1, 6)
# Shape: (5,)

arr_4 = np.full((3, 4), 8)
# Shape: (3, 4)

try:
    broadcast_arr2 = arr_3 + arr_4

except ValueError as err:
    print(err)


# Example 3: Scalar Broadcasting

arr = np.array([1, 2, 3, 4, 5])

# A scalar can be broadcast to an array of any shape.
# NumPy effectively applies 10 to every element.

scalar_broadcast_arr = arr + 10

print(scalar_broadcast_arr)
# [11 12 13 14 15]