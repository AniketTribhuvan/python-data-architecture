# C-Contiguous and Fortran-Contiguous Memory

`C_CONTIGUOUS` and `F_CONTIGUOUS` describe **how the elements of a NumPy array are arranged in memory**.

Suppose we have the following array:

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

The array looks like:

```text
1  2  3
4  5  6
```

But internally, NumPy stores these values in a block of memory.

The question is:

**How are these values actually arranged in memory?**

There are two common memory layouts.

## 1. C-Contiguous Memory (Row-Major Order)

In **C-contiguous** memory, elements are stored row by row.

For the above array, the memory order is:

```text
1 | 2 | 3 | 4 | 5 | 6
```

So NumPy stores:

```text
First row  →  1  2  3
Second row →  4  5  6
```

This is the **default memory layout** when NumPy creates a normal array.

## 2. Fortran-Contiguous Memory (Column-Major Order)

In **Fortran-contiguous** memory, elements are stored column by column.

For the same array, the memory order is:

```text
1 | 4 | 2 | 5 | 3 | 6
```

So NumPy stores:

```text
First column  →  1  4
Second column →  2  5
Third column  →  3  6
```

## Why Does Memory Layout Matter?

Memory layout affects how efficiently NumPy can access elements.

If an operation mainly accesses elements **row-wise**, C-contiguous layout is generally more cache-friendly.

If an operation mainly accesses elements **column-wise**, Fortran-contiguous layout can be more cache-friendly.

This is because nearby elements in memory can usually be accessed more efficiently than elements that are far apart.

> **Important:** C-contiguous does not mean "better" and Fortran-contiguous does not mean "worse". The better layout depends on how the data is accessed.

# Strides

`.strides` tells us **how many bytes NumPy must move in memory to move by one position along each axis**.

Consider the following array:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.int64)
```

The array has:

- 2 dimensions
- `dtype = int64`
- Each `int64` occupies **8 bytes**

Because this is C-contiguous, its memory can be thought of as:

```text
Address    Value
1000       1
1008       2
1016       3
1024       4
1032       5
1040       6
```

The addresses here are only for understanding the concept. NumPy does not necessarily use these exact addresses.

## Stride Along Columns (Axis 1)

Moving from:

```text
1 → 2
```

means moving from address:

```text
1000 → 1008
```

Difference:

```text
8 bytes
```

Therefore:

**Stride along Axis 1 = 8 bytes**

## Stride Along Rows (Axis 0)

Moving from:

```text
1 → 4
```

means moving from:

```text
1000 → 1024
```

Difference:

```text
24 bytes
```

Why?

Each row contains **3 elements**.

Each element occupies **8 bytes**.

Therefore:

```text
3 × 8 = 24 bytes
```

So:

**Stride along Axis 0 = 24 bytes**

## Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.int64)

print(arr.strides)

# Output:
# (24, 8)
```

The output:

```python
(24, 8)
```

means:

- Move **24 bytes** to move one position along Axis 0.
- Move **8 bytes** to move one position along Axis 1.

## Note

Each value inside `.strides` corresponds to **one axis**.

For a 2D array:

```text
First value  → Axis 0 → Row stride
Second value → Axis 1 → Column stride
```

For example:

```python
arr.strides
# (24, 8)
```

means:

```text
Axis 0 → 24 bytes
Axis 1 → 8 bytes
```

> **Important:** Strides are measured in **bytes**, not in number of elements.

# `numpy.round()`

`np.round()` rounds numbers to the nearest value, optionally to a specified number of decimal places.

## Syntax

```python
result = np.round(a, decimals=0)
```

Where:

- `a` → number or array to round
- `decimals` → number of decimal places to keep

## Example

```python
arr = np.array([2.1435, 3.1462, 5.2345])

print(arr)
print(np.round(arr, 2))

# Output:
# [2.1435 3.1462 5.2345]
# [2.14 3.15 5.23]
```

Here:

```python
np.round(arr, 2)
```

means **round to 2 decimal places**.

## Rounding Without Specifying `decimals`

If `decimals` is not specified, it defaults to `0`.

This means NumPy rounds the values to the nearest integer.

It does **not truncate** the decimal part.

```python
arr = np.array([2.1435, 3.1462, 5.2345])

print(arr)

result_array = np.round(arr)

print(result_array)
print(result_array.dtype)

# Output:
# [2.1435 3.1462 5.2345]
# [2. 3. 5.]
# float64
```

Notice that the output is:

```text
[2. 3. 5.]
```

rather than:

```text
[2 3 5]
```

because the original array contains floating-point values, so the result remains a floating-point array.

## NumPy Uses Half-to-Even Rounding

NumPy follows **half-to-even rounding** for exact half values.

This means that when a value is exactly halfway between two numbers, NumPy chooses the **even** number.

```python
arr = np.array([2.5, 5.5, 9.5])

print(arr)

result_array = np.round(arr)

print(result_array)

# Output:
# [2.5 5.5 9.5]
# [ 2.  6. 10.]
```

Why?

```text
2.5 → 2
```

`2` is even.

```text
5.5 → 6
```

`6` is even.

```text
9.5 → 10
```

`10` is even.

So:

> **Half values are rounded toward the nearest even number.**

This is also called **banker's rounding**.

# NumPy's Integer Overflow Behavior

NumPy integer dtypes have a **fixed range of values**.

For example, `int8` has the range:

```text
-128 to 127
```

What happens if we go beyond this range?

```python
import numpy as np

arr = np.array([127], dtype=np.int8)

print(arr + 1)

# Output:
# [-128]
```

Normally:

```text
127 + 1 = 128
```

But `128` cannot be represented by `int8`.

For NumPy's fixed-width integer arithmetic, the result wraps around:

```text
127 + 1 → -128
```

Values can similarly wrap around at the other end of the range.

> **Important:** Be aware of the dtype's range when working with NumPy integer arrays, especially when performing arithmetic on large values.

# Explicit dtype Casting with `astype()`

**Casting** means converting data from one datatype to another.

In NumPy, `.astype()` creates an array with a specified dtype.

## Syntax

```python
new_array = array.astype(new_dtype)
```

## Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.dtype)

new_array = arr.astype(np.int32)

print(new_array)
print(new_array.dtype)

# Output:
# int64
# [[1 2 3]
#  [4 5 6]]
# int32
```

Here:

```python
arr.astype(np.int32)
```

creates an array whose dtype is `int32`.

The original array is not changed.

> **Note:** `.astype()` is a **method** of a NumPy array.

## Converting Integer to String

We can also convert numeric values to strings.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.dtype)

new_array = arr.astype(np.str_)

print(new_array)
print(new_array.dtype)

# Output:
# int64
# [['1' '2' '3']
#  ['4' '5' '6']]
# <U21
```

The dtype:

```text
<U21
```

means NumPy is storing Unicode strings with a maximum length of 21 characters for this dtype.

## Float to Integer

When converting floating-point values to integers, the fractional part is discarded.

It does **not round to the nearest integer**.

```python
arr = np.array([2.32, 3.74, 5.55])

new_array = arr.astype(dtype=np.int32)

print(new_array)

# Output:
# [2 3 5]
```

For example:

```text
2.32 → 2
3.74 → 3
5.55 → 5
```

If we want rounding first, we can use `np.round()`:

```python
new_array2 = np.round(arr).astype(dtype=np.int32)

print(new_array2)

# Output:
# [2 4 6]
```

Here:

```text
np.round(arr)
```

runs first, and then:

```text
.astype(np.int32)
```

converts the rounded values to integers.

# `copy` Parameter

`copy` controls whether `.astype()` should create a separate array when possible.

```python
array.astype(dtype, copy=True)
```

If `copy=True`, NumPy creates a separate array.

If:

```python
copy=False
```

NumPy avoids making a copy **when possible**.

## `copy=True`

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.dtype)  # int64

new_array = arr.astype(dtype=np.int16, copy=True)

# copy=True means create a separate array.
print(new_array is arr)
print(new_array.dtype)

# Output:
# False
# int16
```

`new_array` is a separate array object.

## `copy=False`

Suppose the dtype is already the same:

```python
new_array2 = arr.astype(dtype=np.int64, copy=False)

print(new_array2.dtype)
print(new_array2 is arr)

# Output:
# int64
# True
```

Here, `arr` is already `int64`.

Therefore, NumPy does not need to create a new array.

So:

```python
new_array2 is arr
```

is:

```text
True
```

Both variables refer to the **same array object**.

## What If Conversion Is Necessary?

Even with:

```python
copy=False
```

NumPy may create a new array if the requested dtype is different.

```python
new_array3 = arr.astype(dtype=np.int32, copy=False)

print(new_array3.dtype)
print(new_array3 is arr)

# Output:
# int32
# False
```

Why?

The original array is:

```text
int64
```

but we requested:

```text
int32
```

The data must be represented using a different dtype, so a new array is required.

> **Important:** `copy=False` means **"avoid copying if possible"**, not **"never create a copy."**

# Verifying Contiguity with `.flags`

Earlier we studied C-contiguous and Fortran-contiguous memory layouts.

`.flags` provides information about an array's memory layout and other properties.

## Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.flags)

# Output:
#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : False
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False
```

Currently, our main focus is:

```text
C_CONTIGUOUS
F_CONTIGUOUS
```

In this example:

```text
C_CONTIGUOUS : True
F_CONTIGUOUS : False
```

This means the array has a C-contiguous memory layout.

Some other useful flags are:

```text
OWNDATA   → Does this array own its underlying data?
WRITEABLE → Can the array's data be modified?
```

## Important Flags

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.flags.c_contiguous)
print(arr.flags['C_CONTIGUOUS'])

# Output:
# True
# True

print(arr.flags.f_contiguous)
print(arr.flags['F_CONTIGUOUS'])

# Output:
# False
# False
```

Both forms check the same flag.

# Creating a Fortran/F-Contiguous Array

## Using the `order` Parameter

We can create a Fortran-contiguous array using the `order` parameter.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
], order="F")

print(arr.flags.c_contiguous)

# Output:
# False

print(arr.flags.f_contiguous)

# Output:
# True
```

Here:

```python
order="F"
```

tells NumPy to use **Fortran-style memory layout**.

The array is still displayed normally:

```text
[[1 2 3]
 [4 5 6]]
```

The difference is how its elements are arranged in memory.

# Memory Cost of dtype Choices

Every dtype occupies a fixed number of bytes per element.

| dtype | Bytes per element |
| --- | ---: |
| `int8` | 1 |
| `int16` | 2 |
| `int32` | 4 |
| `int64` | 8 |
| `float32` | 4 |
| `float64` | 8 |
| `bool` | 1 |

For example:

```text
int8   → 1 byte
int32  → 4 bytes
int64  → 8 bytes
```

Therefore, dtype choice affects the memory required by an array.

For very large arrays, choosing an appropriate dtype can make a significant difference in memory usage.

# `.itemsize`

`.itemsize` tells us **how many bytes each element of an array occupies**.

## Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.dtype)
print(arr.itemsize)

# Output:
# int64
# 8
```

The dtype is:

```text
int64
```

and each element occupies:

```text
8 bytes
```

Therefore:

```python
arr.itemsize
```

returns:

```text
8
```

> **Important:** `.itemsize` is the size of **one element**, not the total size of the array.

# `numpy.dtype.itemsize`

We can also find the item size directly from a dtype without creating an array.

```python
import numpy as np

print(np.dtype(np.float64).itemsize)

# Output:
# 8
```

This tells us that one `float64` element occupies 8 bytes.

# Total Memory `.nbytes`

`.nbytes` tells us the total number of bytes occupied by an array's elements.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.dtype)
print(arr.nbytes)

# Output:
# int64
# 48
```

There are:

```text
6 elements
```

and each element occupies:

```text
8 bytes
```

Therefore:

```text
Total memory = number of elements × bytes per element

             = 6 × 8

             = 48 bytes
```

So:

```python
arr.nbytes
```

returns:

```text
48
```

> **Important:** `.nbytes` refers to the memory occupied by the array's data elements. It does not represent every byte of Python/NumPy object overhead.

# `np.arange()`

`np.arange()` stands for **array range**.

`np.arange()` creates a **1D NumPy array** containing values from a starting point up to, but **not including**, the stopping point.

It is similar to Python's built-in `range()`.

## Syntax

```python
np.arange(start, stop, step)
```

Where:

- `start` → starting value
- `stop` → stopping value, **not included**
- `step` → difference between consecutive values

## Example

```python
import numpy as np

print(np.arange(10))
print(np.arange(1, 10))
print(np.arange(1, 10, 2))

# Output:
# [0 1 2 3 4 5 6 7 8 9]
# [1 2 3 4 5 6 7 8 9]
# [1 3 5 7 9]
```

### `np.arange(10)`

When only one argument is provided, it is treated as `stop`.

```python
np.arange(10)
```

is equivalent to:

```python
np.arange(0, 10, 1)
```

So the result is:

```text
[0 1 2 3 4 5 6 7 8 9]
```

Notice that `10` is not included.

### `np.arange(1, 10)`

```python
np.arange(1, 10)
```

starts at `1` and stops before `10`.

Result:

```text
[1 2 3 4 5 6 7 8 9]
```

### `np.arange(1, 10, 2)`

Here the step is `2`.

```python
np.arange(1, 10, 2)
```

Result:

```text
[1 3 5 7 9]
```

> **Important:** `np.arange()` always produces a **1D array**. It does not directly create a 2D array.

# Practice

## Q: Write a Function That Converts a Nested Python List into a Strictly C-Contiguous Array

```python
import numpy as np


def list_to_array(data):
    """Returns a C-contiguous NumPy array."""
    return np.ascontiguousarray(data)


my_list = [
    [1, 2, 3],
    [4, 5, 6]
]

array = list_to_array(my_list)

print(array)
print(type(array))

# Output:
# [[1 2 3]
#  [4 5 6]]
# <class 'numpy.ndarray'>
```

`np.ascontiguousarray()` ensures that the returned array is **C-contiguous**.

We can verify it using `.flags`:

```python
print(array.flags.c_contiguous)

# Output:
# True
```

This is useful when we specifically need a C-contiguous array for efficient memory access or when working with code that expects C-style contiguous data.