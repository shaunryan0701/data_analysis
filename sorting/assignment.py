import numpy as np

prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])

print(prices)

prices.sort()

high_prices = prices[-3:]
print("High prices:", high_prices)

# Output the mean of the prices
mean_price = np.mean(high_prices)
min_price = np.min(high_prices)
max_price = np.max(high_prices)
median_price = np.median(high_prices)
print("Mean price:", mean_price)
print("Min price:", min_price)
print("Max price:", max_price)
print("Median price:", median_price)