import numpy as np

# Print the numpy version and the configuration (★☆☆)
print(np.__version__)
# np.show_config()

# Create a null vector of size 10 (★☆☆)
z = np.zeros(10)
print(z)

# Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
z = np.zeros(10)
z[4] = 1
print(z)

# Create a vector with values ranging from 10 to 49 (★☆☆)
z = np.arange(10, 50)
print(z)

# Reverse a vector (first element becomes last) (★☆☆)
z = np.arange(50)
z = z[::-1]
print(z)

# Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
z = np.arange(9).reshape(3, 3)
print(z)

# Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
nz = np.nonzero([1, 2, 0, 0, 4, 1])
print(nz)

# Create a 3x3 identity matrix (★☆☆)
z = np.eye(3)
print(z)

# Create a 3x3x3 array with random values (★☆☆)
z = np.random.random((3, 3, 3))
print(z)

# Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
z = np.random.random((10, 10))
zmin, zmax = z.min(), z.max()
print(zmin, zmax)

# Create a random vector of size 30 and find the mean value (★☆☆)
z = np.random.rand(30)
print(z)
m = z.mean()
print(m)

# Create a 2d array with 1 on the border and 0 inside (★☆☆)
z = np.ones((10, 10))
z[1:-1, 1:-1] = 0
print(z)

# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
z = np.diag(1 + np.arange(0, 4), k=-1)
print(z)

# Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
z = np.zeros((8, 8))
z[1::2, ::2] = 1
z[::2, 1::2] = 1
print(z)

# Normalize a 5x5 random matrix (★☆☆)
Z = np.random.random((5, 5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)

# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
z = np.dot(np.ones((5, 3)), np.ones((3, 2)))
print(z)

# Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
z = np.arange(11)
z[(3 < z) & (z <= 8)] *= -1
print(z)

#
