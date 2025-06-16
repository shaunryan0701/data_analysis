import numpy as np

sales = [[0, 5, 155, 0, 518], [0, 1827, 616, 317, 325]]

sales_array = np.array(sales)
print("Sales array:", sales_array)
print(type(sales_array))

print("Sales array shape:", sales_array.shape)
print("Sales array size:", sales_array.size)
print("Sales array dtype:", sales_array.dtype)
print("Sales array ndim:", sales_array.ndim)