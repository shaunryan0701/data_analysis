import numpy as np

my_list = np.arange(10, 101, 10).reshape(5, 2)

print("My array:", my_list)

rng = np.random.default_rng(2022)

random_array = rng.random(9).reshape(3, 3)
print("Random array:", random_array)

print("First 2 rows:", random_array[:2, :])

print("First Column", random_array[:, 0])

print("Second number in the third row", random_array[2, 1])