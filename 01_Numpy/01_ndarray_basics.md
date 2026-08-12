# ndarray

## ndarray

`ndarray` is the core data structure provided by the NumPy library.

`ndarray` stands for **N-dimensional array**, meaning it can represent arrays of any number of dimensions (1D, 2D, 3D, ... N-D).

**Dimension** means the number of axes an array has.

## What is an array?

An array is a collection of elements of the **same data type** stored **contiguously in memory**.

## numpy.array()

numpy.array() is a function used to create a NumPy array from an input object such as a list, tuple, or other array-like object.

syntax :
array_name = numpy.array(...)

eg.
```python
import numpy as np

my_list = [1, 2, 3, 4]       # A list

arr = np.array(my_list)     # Creating ndarray from my_list using np.array()

print(arr)
print(type(arr))
# Output :
# [1 2 3 4]
# <class 'numpy.ndarray'>
```

## 1D Array

A 1D array represents a **vector**.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)

# Output :
# [1 2 3 4]
```

## Why does ndarray exist?

Python already has lists, so why do we need `ndarray`?

### Python Lists

Python lists are very flexible, but that flexibility comes with extra memory and slower performance.

A list:

- Stores references (pointers) to Python objects instead of storing values directly.
- Can contain multiple data types.
- Requires Python to inspect every element during operations.
- Consumes more memory.

For millions of numerical values, these overheads become significant.

### ndarray

NumPy's `ndarray` is designed specifically for numerical computing.

Compared to Python lists:

- Stores elements contiguously in memory.
- Stores only one fixed data type.
- Does not need to inspect the type of every element repeatedly.
- Uses highly optimized C code internally for mathematical operations.
- Uses much less memory and performs operations much faster.

This is why NumPy is widely used in Data Science, Machine Learning, and Scientific Computing.

## 2D Array

A 2D array represents **multiple vectors stacked together**.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)

# Output :
# [[1 2 3]
#  [4 5 6]]
```

## 3D Array

A 3D array represents **multiple matrices stacked together**.

```python
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],

    [
        [5, 6],
        [7, 8]
    ]
])

print(arr)
```

# ndarray Attributes

These attributes describe different properties of an array.

## 1. .ndim

`.ndim` returns the number of dimensions (axes) of an array.

```python
# 1D Array
arr = np.array([1, 2, 3])
print(arr.ndim)

# 2D Array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.ndim)

# Output :
# 1
# 2
```

## 2. .shape

`.shape` returns the size of the array along every axis.

For every axis, `.shape` tells how many elements exist along that axis.

```python
# 1D Array
arr = np.array([1, 2, 3])

print(arr.shape)

# Axis 0 contains 3 elements.

# Output :
# (3,)
```

```python
# 2D Array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)

# Axis 0 -> 2 rows
# Axis 1 -> 3 columns

# Output :
# (2, 3)
```

## 3. .size

`.size` returns the total number of elements stored in the array.

It is equal to the product of all values in `.shape`.

```python
# 1D Array
arr = np.array([1, 2, 3])

print(arr.size)

# Output :
# 3
```

```python
# 2D Array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.size)

# Output :
# 6
```

## 4. .dtype

Since every NumPy array stores only one data type,

`.dtype` tells which data type the array stores.

```python
arr = np.array([1.25, 4.52, 7.81])

print(arr.dtype)

# Output :
# float64
```

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.dtype)

# Output :
# int64
```

### Changing dtype

```python
arr = np.array([1, 2, 3], dtype=np.float32)

print(arr)
print(arr.dtype)

# Output :
# [1. 2. 3.]
# float32
```

# Array Memory Layout Controlling Functions

## 1. `np.asfortranarray()`

`np.asfortranarray()` returns an array with **Fortran-contiguous (column-major) memory layout**.

Syntax :

```python
array_name = np.asfortranarray(existing_array_name)
```

Example :

```python
arr = np.array([
    [1, 2, 3],
    [1, 2, 3]
])
# By default, NumPy creates the array as C-contiguous.

new_arr = np.asfortranarray(arr)
# Creates an array with Fortran-contiguous memory layout.

# Checking the memory layout
print(arr.flags["F_CONTIGUOUS"])
print(new_arr.flags["F_CONTIGUOUS"])

# Output :
# False
# True
```

Here:

- `arr` → C-contiguous by default.
- `new_arr` → Fortran-contiguous.

## 2. `np.ascontiguousarray()`

`np.ascontiguousarray()` returns an array with **C-contiguous (row-major) memory layout**.

We can also optionally specify the dtype of the resulting array.

Syntax :

```python
array_name = np.ascontiguousarray(existing_array_name, dtype=None)
# dtype is optional.
```

### Why does `np.ascontiguousarray()` exist?

Sometimes an array is not stored in **C-contiguous memory layout**, but we need a C-contiguous array.

`np.ascontiguousarray()` checks the existing array first:

- If the array is already C-contiguous, it returns the **same array object**.
- If the array is not C-contiguous, it creates a **new C-contiguous array**.

## Example 1: Existing array is not C-contiguous

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [1, 2, 3]
], order="F")
# Creates the array using Fortran-contiguous memory layout.

new_arr = np.ascontiguousarray(arr)
# Creates a C-contiguous array because arr is not C-contiguous.

# Checking the memory layout
print(arr.flags["C_CONTIGUOUS"])
print(new_arr.flags["C_CONTIGUOUS"])

# Output :
# False
# True
```

Here:

- `arr` → Fortran-contiguous.
- `new_arr` → C-contiguous.
- Since `arr` is not C-contiguous, NumPy creates a new array.

## Example 2: Existing array is already C-contiguous

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [1, 2, 3]
])
# NumPy creates arrays as C-contiguous by default.

new_arr = np.ascontiguousarray(arr)
# arr is already C-contiguous.
# Therefore, NumPy returns the same array object.

# Checking the memory layout
print(arr.flags["C_CONTIGUOUS"])
print(new_arr.flags["C_CONTIGUOUS"])

# Checking whether both variables refer to the same object
print(new_arr is arr)

# Output :
# True
# True
# True
```

Here:

- `arr` → C-contiguous.
- `new_arr` → C-contiguous.
- `new_arr is arr` → `True`, so both variables refer to the same array object.

## What if we request a different dtype?

If the existing array is C-contiguous but we request a different dtype, NumPy creates a new array with the requested dtype.

```python
new_arr2 = np.ascontiguousarray(arr, dtype=np.int32)

print(new_arr2.flags["C_CONTIGUOUS"])
print(new_arr2 is arr)
print(new_arr2.dtype)

# Output :
# True
# False
# int32
```

Here:

- `arr` → Original C-contiguous array.
- `new_arr2` → New C-contiguous array.
- `new_arr2 is arr` → `False`, because a new array was created.
- `new_arr2.dtype` → `int32`, because we requested `dtype=np.int32`.

## Important Note

`np.ascontiguousarray()` does **not always create a copy**.

If the existing array is already C-contiguous and the requested dtype does not require a conversion, NumPy can return the existing array itself.

If the array is not C-contiguous or the dtype needs to be changed, NumPy creates a new array.

# .shape vs len() vs .size

These three can look similar, but they give different information.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)
print(len(arr))
print(arr.size)

# Output :
# (2, 3)
# 2
# 6
```

## 1. `.shape`

`.shape` returns the size of the array along **each dimension**.

For this array:

```python
arr.shape
```

returns:

```python
(2, 3)
```

This means:

- Axis 0 → 2 elements (rows)
- Axis 1 → 3 elements (columns)

## 2. `len()`

`len()` returns the size of the **first dimension (Axis 0)**.

```python
len(arr)
```

returns:

```python
2
```

Because the array has 2 rows.

## 3. `.size`

`.size` returns the **total number of elements** in the array.

```python
arr.size
```

returns:

```python
6
```

Because:

```text
2 rows × 3 columns = 6 elements
```

## Quick Difference

```text
.shape → Size of every dimension
len()  → Size of the first dimension
.size  → Total number of elements
```

# Functions for Creating Arrays

## 1. `np.zeros()`

`np.zeros()` is a function which returns an `ndarray` containing all elements as `0`.

By default, the dtype is `float64`.

Syntax :

```python
array_name = np.zeros(shape)
```

Example :

```python
arr = np.zeros((2, 3))

print(arr)
print(arr.dtype)

# Output :
# [[0. 0. 0.]
#  [0. 0. 0.]]
# float64
```

### Setting dtype

We can use the `dtype` parameter to specify the data type.

```python
arr = np.zeros((2, 3), dtype=np.int32)

print(arr)
print(arr.dtype)

# Output :
# [[0 0 0]
#  [0 0 0]]
# int32
```

## 2. `np.ones()`

`np.ones()` is similar to `np.zeros()`.

It returns an `ndarray` containing all elements as `1`.

By default, the dtype is `float64`.

Syntax :

```python
array_name = np.ones(shape)
```

Example :

```python
arr = np.ones((2, 3))

print(arr)
print(arr.dtype)

# Output :
# [[1. 1. 1.]
#  [1. 1. 1.]]
# float64
```

### Setting dtype

```python
arr = np.ones((2, 3), dtype=np.int32)

print(arr)
print(arr.dtype)

# Output :
# [[1 1 1]
#  [1 1 1]]
# int32
```

## 3. `np.full()`

`np.full()` returns an `ndarray` where every element contains the specified value.

The dtype is automatically selected based on the value unless we specify it using `dtype`.

Syntax :

```python
array_name = np.full(shape, value)
```

Example :

```python
arr = np.full((2, 3), 7, dtype=np.int16)

print(arr)
print(arr.dtype)

# Output :
# [[7 7 7]
#  [7 7 7]]
# int16
```

Here:

```python
np.full((2, 3), 7)
```

means:

- `(2, 3)` → Create an array with 2 rows and 3 columns.
- `7` → Fill every element with `7`.

## 4. `np.empty()`

`np.empty()` creates an array **without initializing its elements to a specific value**.

The array contains whatever values happen to already exist in the allocated memory.

Therefore, the values returned by `np.empty()` are **arbitrary** and should not be treated as meaningful data.

Syntax :

```python
array_name = np.empty(shape)
```

Example :

```python
arr = np.empty((2, 3))

print(arr)

# Output :
# Values may be different each time.
# Example :
# [[1.25013738e+243 7.48956328e+247 5.91870742e-061]
#  [2.24424990e+137 1.00666276e+176 2.23716929e-312]]
```

### Why use `np.empty()`?

`np.empty()` can be useful when we already know that we are going to fill every element later.

It avoids the extra step of initializing every element with `0` or `1`.