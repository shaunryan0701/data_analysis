import numpy as np
import pandas as pd

sales = [0, 5, 155, 0, 518, 0, 1827, 616, 317, 325]

# Create a Series from the sales data
sales_series = pd.Series(sales, name='Sales')
# Display the Series
print("Sales Series:")
print(sales_series)

print("\nType of sales_series:", type(sales_series))
print("Shape of sales_series:", sales_series.shape)
print("Size of sales_series:", sales_series.size)
print("Data type of sales_series:", sales_series.dtype)
print("Number of dimensions of sales_series:", sales_series.ndim)
print("Index of sales_series:", sales_series.index)
print("Values of sales_series:", sales_series.values)
print("Name of sales_series:", sales_series.name)