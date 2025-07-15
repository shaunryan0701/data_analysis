import numpy as np

products = np.array(['apple', 'banana', 'rare tomato', 'date', 'gourmet ice cream', 'cola'])

prices = np.array([1.99, 0.99, 30.49, 2.99, 25.99, 1.90])

expensive_products = np.where(prices > 25, products, None)
fancy_feast_special = np.where(prices > 25, products, np.where(products == 'cola', products, None))

print("Expensive products:", expensive_products[expensive_products != None])
print("Fancy feast special:", fancy_feast_special[fancy_feast_special != None])
