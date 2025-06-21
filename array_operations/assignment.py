import numpy as np

prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])
random_array = np.random.default_rng(2022).random(9).reshape(3, 3)

print("Prices:", prices)
print("Random array:", random_array)

# Add shipping fee

prices_with_shipping = prices + 5
print("Prices with shipping:", prices_with_shipping)

# Apply a discount
discounts = random_array[:2, :].reshape(6)
print("Discounts:", discounts)

final_prices = prices_with_shipping * (1 - discounts)
print("Final prices after discount:", final_prices.round(2))