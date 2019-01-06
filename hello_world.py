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
