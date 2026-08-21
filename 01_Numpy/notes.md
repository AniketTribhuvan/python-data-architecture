# NumPy

NumPy (Numerical Python) is the fundamental library for numerical computing in Python.

It provides a powerful **N-dimensional array** object along with many mathematical functions that operate efficiently on those arrays.

Unlike Python lists, NumPy arrays are stored in **contiguous memory**, making them much faster and more memory-efficient.

Many popular libraries like **Pandas**, **SciPy**, **Scikit-learn**, and **PyTorch** are built on ideas introduced by NumPy.

---

# N-Dimensional Arrays (ndarray)

## What is an ndarray?

An **ndarray** (N-dimensional array) is NumPy's core data structure.

It stores multiple values of the same data type inside a contiguous block of memory.

Unlike Python lists, NumPy arrays are designed for fast mathematical operations.

Syntax:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
```

Example:

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr)
print(type(arr))
```

Output:

```python
[10 20 30]
<class 'numpy.ndarray'>
```

---

## Dimensions

NumPy arrays can have one or more dimensions.

### 1D Array

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr.ndim)
```

Output:

```python
1
```

---

### 2D Array

```python
import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr.ndim)
```

Output:

```python
2
```

---

### 3D Array

```python
import numpy as np

arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(arr.ndim)
```

Output:

```python
3
```

---

## Shape

`shape` tells us the size of each dimension.

Example:

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)
```

Output:

```python
(2, 3)
```

This means:

- 2 rows
- 3 columns

---

## Size

`size` returns the total number of elements.

Example:

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.size)
```

Output:

```python
6
```

---

## Memory Usage

`nbytes` returns the total memory occupied by the array.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4], dtype=np.int32)

print(arr.nbytes)
```

Output:

```python
16
```

Since each `int32` occupies 4 bytes:

```
4 × 4 = 16 bytes
```

---

# Data Types (dtypes)

## What is a dtype?

A **dtype** specifies the type of data stored inside a NumPy array.

Every element inside a NumPy array has the same dtype.

Common dtypes:

- int8
- int16
- int32
- int64
- float32
- float64
- bool
- complex64

Example:

```python
import numpy as np

arr = np.array([1, 2, 3], dtype=np.float32)

print(arr.dtype)
```

Output:

```python
float32
```

---

## Why are dtypes Important?

Choosing the correct dtype helps:

- Reduce memory usage
- Improve performance
- Process larger datasets

For example,

Using `float32` instead of `float64` cuts memory usage almost in half.

---

# Memory Layout

## Contiguous Memory

Unlike Python lists, NumPy stores array elements in one continuous block of memory.

Example:

```
Python List

[10]   [20]   [30]
 ↓      ↓      ↓
Different memory locations

----------------------------

NumPy Array

10 | 20 | 30

Single continuous memory block
```

This is one of the main reasons why NumPy is much faster.

---

## C-Contiguous Memory

In C-contiguous arrays, rows are stored continuously.

Example:

```
[[1 2 3]
 [4 5 6]]

Memory:

1 2 3 4 5 6
```

Check:

```python
print(arr.flags["C_CONTIGUOUS"])
```

---

## Fortran-Contiguous Memory

In Fortran-contiguous arrays, columns are stored continuously.

Example:

```
[[1 2 3]
 [4 5 6]]

Memory:

1 4 2 5 3 6
```

Check:

```python
print(arr.flags["F_CONTIGUOUS"])
```

---

# Strides

## What are Strides?

Strides tell NumPy how many **bytes** it must move in memory to reach the next element in each dimension.

Example:

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.int32)

print(arr.strides)
```

Output:

```python
(12, 4)
```

Meaning:

- Move 12 bytes to reach the next row.
- Move 4 bytes to reach the next column.

---

# Explicit Dtype Casting (`astype`)

Sometimes we need to convert an array into another dtype.

Syntax:

```python
new_array = arr.astype(np.float32)
```

Example:

```python
import numpy as np

arr = np.array([1, 2, 3], dtype=np.int64)

new_arr = arr.astype(np.float32)

print(new_arr.dtype)
```

Output:

```python
float32
```

---

# Array Contiguity (`.flags`)

The `.flags` attribute provides information about how an array is stored.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr.flags)
```

To check C-contiguity:

```python
print(arr.flags["C_CONTIGUOUS"])
```

---

# Memory Optimization

Memory optimization means reducing the amount of RAM used without changing the actual data.

Some common techniques:

- Choosing smaller dtypes
- Avoiding unnecessary copies
- Using views whenever possible

---

# Indexing

Indexing accesses individual elements.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30])

print(arr[1])
```

Output:

```python
20
```

---

# Slicing

Slicing extracts a portion of an array.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
```

Output:

```python
[20 30 40]
```

---

# Boolean Masking

Boolean masking filters elements based on conditions.

Example:

```python
import numpy as np

arr = np.array([10, 15, 20, 25])

print(arr[arr > 15])
```

Output:

```python
[20 25]
```

---

# Fancy Indexing

Fancy indexing uses lists or arrays of indices.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr[[0, 2]])
```

Output:

```python
[10 30]
```

Unlike slicing, fancy indexing creates a copy.

---

# Views vs Copies

## View

A view shares the same memory as the original array.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3])

view = arr[:]

view[0] = 100

print(arr)
```

Output:

```python
[100   2   3]
```

Both arrays refer to the same data.

---

## Copy

A copy creates completely new memory.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3])

copy = arr.copy()

copy[0] = 100

print(arr)
```

Output:

```python
[1 2 3]
```

The original array remains unchanged.

---

# Reshaping (`reshape`)

`reshape()` changes the dimensions without changing the data.

Example:

```python
import numpy as np

arr = np.arange(9)

matrix = arr.reshape(3, 3)

print(matrix)
```

Output:

```python
[[0 1 2]
 [3 4 5]
 [6 7 8]]
```

---

# Transposing

Transposing swaps rows and columns.

Example:

```python
import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr.T)
```

Output:

```python
[[1 3]
 [2 4]]
```

---

# Broadcasting

## What is Broadcasting?

Broadcasting allows NumPy to perform operations on arrays with different shapes without copying data.

Example:

```python
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print(matrix + vector)
```

Output:

```python
[[11 22 33]
 [14 25 36]]
```

NumPy automatically stretches the smaller array.

---

# Matrix Multiplication (`@`)

The `@` operator performs matrix multiplication.

Example:

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A @ B)
```

---

# Dot Product (`np.dot`)

`np.dot()` calculates the dot product.

Example:

```python
import numpy as np

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

print(np.dot(a, b))
```

Output:

```python
32
```

---

# Axis-wise Aggregations

NumPy can calculate statistics across specific axes.

Example:

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.sum(axis=0))
print(arr.sum(axis=1))
```

Output:

```python
[5 7 9]

[6 15]
```

---

# Vectorized Operations

Vectorization means performing operations on the entire array at once instead of writing Python loops.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr * 10)
```

Output:

```python
[10 20 30]
```

Vectorized code is:

- Faster
- Cleaner
- More memory-efficient