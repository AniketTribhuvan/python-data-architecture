"""Vectorization & Axis-Wise Aggregations."""

import numpy as np


# Create a 3x4 array of random integers.

rng = np.random.default_rng()

arr = rng.integers(
    1,
    10,
    size=(3, 4),
    dtype=np.int32
)

print(arr)


# Axis-Wise Aggregations

# Aggregation operations can be performed in two forms:
#
# 1. Method form:
#    arr.mean()
#
# 2. Function form:
#    np.mean(arr)
#
# Both can perform the same aggregation operation.


# axis=0

arr_mean1 = arr.mean(axis=0)

assert arr_mean1.shape == (4,), \
    "Error: axis=0 must collapse dimension 0"

# Shape:
#
# Original array:
# (3, 4)
#
# axis=0 means we collapse the rows.
#
# (3, 4) -> (4,)
#
# NumPy calculates a separate mean for each column.
#
# Example:
#
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [2, 4, 6, 8]]
#
# axis=0:
#
# Column 1 -> mean of [1, 5, 2]
# Column 2 -> mean of [2, 6, 4]
# Column 3 -> mean of [3, 7, 6]
# Column 4 -> mean of [4, 8, 8]
#
# The result contains one value for each column.


# axis=1

arr_mean2 = arr.mean(axis=1)

assert arr_mean2.shape == (3,), \
    "Error: axis=1 must collapse dimension 1"

# axis=1 means we collapse the columns.
#
# (3, 4) -> (3,)
#
# NumPy calculates a separate mean for each row.
#
# Example:
#
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [2, 4, 6, 8]]
#
# axis=1:
#
# Row 1 -> mean of [1, 2, 3, 4]
# Row 2 -> mean of [5, 6, 7, 8]
# Row 3 -> mean of [2, 4, 6, 8]
#
# The result contains one value for each row.


# No-Axis Behaviour

arr_mean = arr.mean()

# When axis is not specified, NumPy collapses all dimensions.
#
# (3, 4) -> scalar
#
# All elements of the array are used to calculate one overall mean.

assert isinstance(arr_mean, (float, np.floating)), \
    "Error: No axis must return a scalar"


# Common Aggregations & Mathematical Functions


# 1. sum()
#
# sum() adds all elements of the array.

arr_sum = arr.sum()

print(arr_sum)


# 2. std()
#
# std() calculates standard deviation.
#
# ddof = "delta degrees of freedom".
#
# Default:
# ddof=0
#
# For population standard deviation:
# ddof=0
#
# For sample standard deviation:
# ddof=1

arr_std1 = arr.std(ddof=1)
arr_std2 = arr.std()

assert arr_std1 > arr_std2, \
    "arr_std1 must be greater than arr_std2 if arr_std1 has ddof=1"


# 3. sqrt()
#
# sqrt() calculates the square root of each element.
#
# It is an element-wise operation.

arr = np.arange(1, 6)

arr_sqrt = np.sqrt(arr)

print(arr_sqrt)
# [1.         1.41421356 1.73205081 2.         2.23606798]


# 4. exp()
#
# exp(x) calculates e^x for each element.
#
# e is Euler's number (~2.71828).

arr_exp = np.exp(arr)

print(arr_exp)


# 5. log()
#
# np.log() calculates the natural logarithm (base e).
#
# np.log10() can be used when base-10 logarithm is required.

log_e = np.log(arr)

print(log_e)


# 6. abs()
#
# abs() returns the absolute value of each element.

arr = np.array([-2, -3, -4])
arr_abs = np.abs(arr)
print(arr_abs)