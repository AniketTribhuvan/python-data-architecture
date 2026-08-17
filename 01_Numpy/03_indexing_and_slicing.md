# Slicing

## Basic Slicing

In Python, we studied slicing.

NumPy also supports slicing in a similar way.

General syntax:

```python
result = array_name[start:stop:step]
```

Where:

- `start` → starting index
- `stop` → stopping index, **not included**
- `step` → how many positions to move at a time

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

result_arr = arr[1:4]

print(result_arr)
# [2 3 4]

print(arr[::2])
# [1 3 5]

print(arr[::-1])
# [5 4 3 2 1]
```

The same slicing rules we learned in Python apply here.

# Slicing Multiple Dimensions

NumPy allows us to slice multiple dimensions simultaneously.

General syntax:

```python
result = array_name[start:stop:step, start:stop:step, ...]
```

Each `start:stop:step` represents slicing for one dimension.

For a 2D array:

```python
result = array_name[start:stop:step, start:stop:step]
```

For a 3D array:

```python
result = array_name[start:stop:step, start:stop:step, start:stop:step]
```

## Example

```python
arr = np.array([
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50]
])

# Second row, all columns stepping by 2.
print(arr[1:, ::2])

# Output:
# [[10 30 50]]

# Second row, first column only.
print(arr[1:, :1])

# Output:
# [[10]]
```

Another example:

```python
arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Second and third rows, first 2 columns only.
print(arr1[1:, :2])

# Output:
# [[ 5  6]
#  [ 9 10]]
```

For a 2D array:

```text
arr[rows, columns]
```

So:

```python
arr[1:, :2]
```

means:

```text
1:  → select rows from index 1 onward
:2  → select columns before index 2
```

# Important: Basic Slicing Creates a View

Basic slicing usually creates a **view**, not an independent copy of the data.

A view is a different array object that refers to the **same underlying data** as the original array.

Therefore, changing the view can also change the original array.

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr)
# [10 20 30 40 50]

view = arr[1:4]

print(view)
# [20 30 40]

view[0] = 999

print(view)
# [999  30  40]

print(arr)
# [ 10 999  30  40  50]
```

Why did `arr` change?

`view` refers to the same underlying data as `arr`.

```text
arr:
[10, 20, 30, 40, 50]
      ↑   ↑   ↑
      └── view ──┘
```

So:

```python
view[0] = 999
```

changes the corresponding element in the original array.

> **Important:** A view is a separate array object, but it can share the same underlying data with another array.

# Comparison Operators (`>`, `<`, `==`, `!=`)

NumPy comparison operators perform **element-wise comparisons** and produce a Boolean array.

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

result = arr > 25

print(result)

# Output:
# [False False  True  True  True]
```

NumPy compares every element individually:

```text
10 > 25 → False
20 > 25 → False
30 > 25 → True
40 > 25 → True
50 > 25 → True
```

The result is a Boolean array with the same shape as the original array.

Other comparison operators can also be used:

```python
arr == 30
arr != 30
arr > 30
arr < 30
arr >= 30
arr <= 30
```

For example:

```python
arr = np.array([10, 20, 30])

print(arr == 20)

# Output:
# [False  True False]
```

# Boolean Masking

We just studied how comparison operators create Boolean arrays.

We can use these Boolean arrays to **filter elements** from a NumPy array.

This is called **Boolean masking**.

A Boolean mask contains:

```text
True  → select the element
False → do not select the element
```

## Example

```python
arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25

print(mask)
# [False False  True  True  True]

result_array = arr[mask]

print(result_array)
# [30 40 50]
```

The mask is:

```text
[False False True True True]
```

NumPy selects the elements where the mask contains `True`:

```text
10 → False → not selected
20 → False → not selected
30 → True  → selected
40 → True  → selected
50 → True  → selected
```

We can also write the same operation directly:

```python
result_array = arr[arr > 25]

print(result_array)

# Output:
# [30 40 50]
```

Here:

```python
arr > 25
```

first creates a Boolean array.

Then:

```python
arr[...]
```

uses that Boolean array as a mask.

# Combining Conditions

We can combine multiple conditions when creating a Boolean mask.

NumPy commonly uses:

```text
&  → element-wise AND
|  → element-wise OR
~  → element-wise NOT
```

## AND (`&`)

```python
arr = np.array([10, 20, 30, 40, 50])

result = arr[(arr > 20) & (arr < 50)]

print(result)

# Output:
# [30 40]
```

This means:

```text
arr > 20
AND
arr < 50
```

Only values satisfying **both** conditions are selected.

## OR (`|`)

```python
print(arr[(arr < 20) | (arr > 40)])

# Output:
# [10 50]
```

This selects values that satisfy **either** condition.

## NOT (`~`)

```python
print(arr[~(arr < 30)])

# Output:
# [30 40 50]
```

`~` flips the Boolean values:

```text
True  → False
False → True
```

So:

```python
arr < 30
```

produces:

```text
[True, True, False, False, False]
```

After:

```python
~(arr < 30)
```

it becomes:

```text
[False, False, True, True, True]
```

Then NumPy selects the `True` values.

## Why `&`, `|`, and `~` Instead of `and`, `or`, and `not`?

Python's:

```python
and
or
not
```

are designed for working with individual Boolean values.

NumPy comparisons usually produce **arrays of Boolean values**.

For example:

```python
arr > 20
```

produces:

```text
[False, False, True, True, True]
```

Therefore, NumPy uses element-wise logical operators:

```text
& → element-wise AND
| → element-wise OR
~ → element-wise NOT
```

> **Important:** Do not use Python's `and`, `or`, and `not` for combining NumPy Boolean arrays.

## Why Parentheses?

Each comparison should normally be placed inside parentheses when using `&` or `|`.

Correct:

```python
arr[(arr > 20) & (arr < 50)]
```

Incorrect:

```python
arr[arr > 20 & arr < 50]
```

The parentheses make each comparison happen separately before the element-wise logical operation.

# Fancy Indexing

In basic slicing, we specify a range of indices.

In **fancy indexing**, we provide an array or list of specific indices that we want to select.

General syntax:

```python
result = array_name[[index1, index2, ...]]
```

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[[0, 3, 4]])

# Output:
# [10 40 50]
```

Here:

```text
Index 0 → 10
Index 3 → 40
Index 4 → 50
```

So the result is:

```text
[10 40 50]
```

## Advantages of Fancy Indexing

### 1. Fancy Indexing Can Reorder Elements

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[[4, 0, 2]])

# Output:
# [50 10 30]
```

The indices are:

```text
4 → 50
0 → 10
2 → 30
```

So the resulting order is based on the order of the indices we provide.

### 2. Fancy Indexing Allows Duplicate Indices

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[[4, 0, 2, 4, 4]])

# Output:
# [50 10 30 50 50]
```

Index `4` was provided three times, so its value appears three times.

## Important: Fancy Indexing Creates a Copy

Basic slicing generally creates a **view**.

Fancy indexing creates a **copy** of the selected data.

For example:

```python
arr = np.array([10, 20, 30, 40, 50])

fancy_arr = arr[[1, 4]]

print(fancy_arr)

# Output:
# [20 50]
```

Changing `fancy_arr` does not change `arr`:

```python
fancy_arr[0] = 999

print(fancy_arr)
# [999  50]

print(arr)
# [10 20 30 40 50]
```

The original array remains unchanged because fancy indexing created a copy.

# Fancy Indexing in 2D Arrays

Fancy indexing can also be used to select specific rows from a 2D array.

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[[0, 2]])

# Output:
# [[10 20 30]
#  [70 80 90]]
```

Here:

```text
0 → first row
2 → third row
```

So NumPy returns those two rows.

# `.base`

`.base` is an attribute that can help us determine whether an array is **sharing its underlying data with another array**.

It is especially useful when studying **views and copies**.

## Checking a View

```python
arr = np.array([10, 20, 30, 40, 50])

view = arr[1:4]     # Basic slicing

print(view.base)

# Output:
# [10 20 30 40 50]

print(view.base is arr)

# Output:
# True
```

Because basic slicing created a view, `view` shares data with `arr`.

Therefore:

```python
view.base is arr
```

returns:

```text
True
```

## Checking Fancy Indexing

```python
fancy_arr = arr[[1, 4]]

print(fancy_arr.base)

# Output:
# None
```

Fancy indexing created a copy.

Therefore, `fancy_arr` does not have `arr` as its `.base`.

```text
fancy_arr.base → None
```

> **Important:** `.base is None` generally means the array does not report another array as the owner of its data. It does not simply mean "this array is definitely a copy" in every possible NumPy situation.

For basic view/copy examples, `.base` is a useful way to inspect whether an array is sharing data with another array.

# `np.random`

`np.random` is NumPy's module for generating random numbers.

We will use random number generation in practice problems and later in Machine Learning.

# `np.random.default_rng()`

`np.random.default_rng()` creates a NumPy **Random Number Generator (RNG)** object.

Preferred approach:

```python
rng = np.random.default_rng()
```

Now `rng` is a random number generator object that can be used to generate random values.

For example:

```python
rng = np.random.default_rng()

print(rng)
```

The important point is that we use the `rng` object to generate random numbers instead of repeatedly calling older random-generation functions.

# `rng.integers()`

`rng.integers()` generates random integers.

## Syntax

```python
rng.integers(low, high=None, size=None, dtype=np.int64)
```

The commonly used parameters are:

- `low` → lower bound
- `high` → upper bound, **not included**
- `size` → shape of the output
- `dtype` → datatype of the generated integers

## Example

```python
rng = np.random.default_rng()

arr = rng.integers(1, 10, size=(2, 3))

print(arr)

# Example output:
# [[9 8 3]
#  [1 2 5]]
```

The exact numbers will normally be different each time because no seed was specified.

The important part is the shape:

```python
size=(2, 3)
```

This creates a:

```text
2 × 3
```

2D array.

Also notice:

```python
rng.integers(1, 10)
```

generates values from:

```text
1 to 9
```

because `high=10` is excluded.

# Reproducibility with `seed`

Random numbers are useful, but sometimes we need to generate the **same random values again**.

This is called **reproducibility**.

We can initialize the generator with a seed:

```python
rng = np.random.default_rng(seed=...)
```

## Why Use a Seed?

Generators initialized with the **same seed** produce the same sequence of random numbers.

Example:

```python
rng1 = np.random.default_rng(seed=7)

arr1 = rng1.integers(1, 10, size=(2, 3))


rng2 = np.random.default_rng(seed=7)

arr2 = rng2.integers(1, 10, size=(2, 3))


# np.array_equal() checks whether both arrays
# contain the same values and have the same shape.
print(np.array_equal(arr1, arr2))

# Output:
# True
```

Both generators start from the same initial state because they use:

```text
seed = 7
```

Therefore, they produce the same sequence.

> **Important:** A seed does not make numbers truly random in a mathematical sense. It makes the pseudo-random sequence **reproducible**.

# Practice

## Q: Instantiate a 10×10 Matrix of Random Integers; Extract All Odd Numbers Using a Boolean Mask and Use Fancy Indexing to Extract Rows `[0, 3, 7]` and Confirm the Result Is a Copy, Not a View.

```python
import numpy as np

rng = np.random.default_rng()

arr = rng.integers(10, 100, size=(10, 10))

# Boolean masking:
# arr % 2 == 1 creates a Boolean mask for odd numbers.
odd_numbers_array = arr[arr % 2 == 1]

print(odd_numbers_array)


# Fancy indexing:
# Select rows 0, 3, and 7.
fancy_array = arr[[0, 3, 7]]

print(fancy_array)


# Check whether fancy_array shares its data with another array.
print(fancy_array.base)

# Output:
# None
```

`fancy_array.base` is `None`, which shows that this fancy-indexing result does not use `arr` as its underlying array.

Therefore, in this case, fancy indexing created a **copy**, not a view.

We can also verify the behavior directly:

```python
fancy_array[0, 0] = 999

print(fancy_array[0, 0])
# 999

print(arr[0, 0])
# Original value remains unchanged
```

This demonstrates the important difference:

```text
Basic slicing   → View
Fancy indexing  → Copy
Boolean masking → Copy
```