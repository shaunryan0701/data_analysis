import numpy as np

ones_array = np.ones((4,2))
print("Array of ones:", ones_array)

zeroes_array = np.zeros((3,3))
print("Array of zeroes:", zeroes_array)

example = np.arange(1, 9, 2)
print("Example array:", example)

example_reshaped = example.reshape(3, 2)
print("Reshaped example array:", example_reshaped)