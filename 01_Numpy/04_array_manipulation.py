import numpy as np


# Reshape: Creates an array with a specific shape.

arr = np.arange(100, dtype=np.int32)

# -1 tells NumPy to calculate the number of columns automatically.
matrix_10x10 = arr.reshape((10, -1), copy=False)

print(matrix_10x10.shape)
# (10, 10)


# Checking whether matrix_10x10 is the same array object as arr.
print(matrix_10x10 is arr)
# False


# Confirming that matrix_10x10 is a view of arr using .base.
print(matrix_10x10.base is arr)
# True


# Proving that matrix_10x10 and arr share the same underlying data
# by modifying the first element of matrix_10x10.
matrix_10x10[0, 0] = 99

print(arr[0])
# 99


# Verifying again using .base.
# .base should not be None because matrix_10x10 is a view.
print(matrix_10x10.base is not None)
# True


# .ravel() and .flatten() convert an N-dimensional array into a 1D array.
#
# .ravel() prefers to return a view whenever possible.
# .flatten() always returns a copy.


ravel_matrix = matrix_10x10.ravel()

print(ravel_matrix.base is arr)
# True
# ravel_matrix ultimately shares data with arr.


flatten_matrix = matrix_10x10.flatten()

print(flatten_matrix.base is arr)
# False
# flatten() creates a separate copy.


# Transpose: Converts rows into columns and columns into rows.
#
# .T is a convenient way to transpose an array.
# np.transpose() can also be used, especially when working with
# higher-dimensional arrays.

transpose_matrix = matrix_10x10.T

# Checking whether transpose_matrix owns its own data.
#
# OWNDATA = False means it does not own the underlying data.
print(transpose_matrix.flags['OWNDATA'])
# False