# Import necessary libraries
import numpy as np
import pandas as pd

# Create a 1-dimensional NumPy array
a1d = np.array([1, 2, 3])

# Create a 2-dimensional NumPy array
a2d = np.array([[1,2,3],[4,5,6]])

# Create a 3-dimensional NumPy array
a3d = np.array([[[1.1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])

# Print information about the arrays
print(f'a1d = {a1d}')
print(f'a2d = {a2d}')
print(f'a3d = {a3d}')
print(f'a1d shape = {a1d.shape}')
print(f'a2d shape = {a2d.shape}')
print(f'a3d shape = {a3d.shape}')
print(f'a1d dimension = {a1d.ndim}')
print(f'a2d dimension = {a2d.ndim}')
print(f'a3d dimension = {a3d.ndim}')
print(f'a1d type = {a1d.dtype}')
print(f'a2d type = {a2d.dtype}')
print(f'a3d type = {a3d.dtype}')
print(f'a1d size = {a1d.size}')
print(f'a2d size = {a2d.size}')
print(f'a3d size = {a3d.size}')

# Create a DataFrame from a2d
df = pd.DataFrame(a2d)
print(f'df = {df}')

# Create a 4x3 array of ones
ones = np.ones((4,3))

# Create a 3x4 array of zeros
zeros = np.zeros((3,4))

# Generate an array with values from 0 to 10 (exclusive) with a step of 2
print(f'arange = {np.arange(0,10,2)}')

# Generate a random matrix of size 3x5 with values from 0 to 9
np.random.seed(seed = 0)
random_matrix = np.random.randint(0,10,size=(3,5))

# Print the sum of elements in the random matrix
print(f'random matrix = {random_matrix}')
print(f'random matrix sum = {random_matrix.sum()}')

# Accessing elements in a3d
print(f'a3d[0] = {a3d[0]}')
print(f'a3d[:2] = {a3d[:2]}')
print(f'a3d[:2,:1] = {a3d[:2,:1]}')
print(f'a3d[:2,:1,:2] = {a3d[:2,:1,:2]}')
