# NumPy

## Overview

This folder focuses on learning the fundamentals of **NumPy**, the core library for numerical computing in Python.

These concepts form the foundation of efficient data manipulation and scientific computing. Understanding how NumPy stores and processes data is essential before moving to libraries like Pandas, Polars, and eventually machine learning frameworks such as PyTorch.

## Topics Covered

- N-dimensional arrays (ndarrays)
- data types (dtypes)
- C-contiguous vs. Fortran-contiguous memory
- strides
- explicit dtype casting (`astype`)
- array contiguity (`.flags`)
- memory optimization
- indexing
- slicing
- boolean masking
- fancy indexing
- views vs. copies
- reshaping (`reshape`)
- transposing
- broadcasting

## Skills Developed

- Creating and working with NumPy arrays
- Understanding how arrays are stored in memory
- Optimizing memory usage using appropriate dtypes
- Selecting and filtering data without loops
- Reshaping and transforming arrays efficiently
- Distinguishing between views and copies
- Applying broadcasting for efficient computations

## Key Takeaways

- NumPy arrays provide fast and memory-efficient numerical computing.
- Understanding memory layout helps write more optimized code.
- Choosing the correct dtype can significantly reduce memory usage.
- Views avoid unnecessary memory copies, while copies create new data.
- Broadcasting allows operations on arrays with different shapes without writing loops.

## 🗂️ Project Structure

```text
01_NumPy/
  README.md                                  # Folder overview of NumPy concepts
  NOTES.md                                   # Notes and concepts related to NumPy

  01_ndarray_basics.md                          # Creating ndarrays, dtypes, shape, size, and memory layout
  02_dtype_and_memory.md                        # Dtype casting, contiguity, and memory optimization
  03_indexing_and_slicing.md                    # Indexing, slicing, boolean masking, and fancy indexing
  04_array_manipulation.py                      # Reshaping, transposing, views, and copies
  05_broadcasting.py                            # Broadcasting rules and shape compatibility
```

**Note** : Before executing any example from .md file. Always write following in code at first line :
```python
import numpy as np
```