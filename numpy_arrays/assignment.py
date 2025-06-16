import numpy as np

my_list = [x * 10 for x in range(1, 11)]

my_array = np.array(my_list)

print("My array:", my_array)
print("Type of my array:", type(my_array))
print("Shape of my array:", my_array.shape)
print("Size of my array:", my_array.size)
print("Data type of my array:", my_array.dtype)
print("Number of dimensions of my array:", my_array.ndim)