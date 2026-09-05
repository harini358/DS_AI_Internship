prices = [100, 250, 80, 150, 300]

updated_prices = []

for price in prices:
    updated_prices.append(price + 20)

print("Updated prices:", updated_prices)

import numpy as np

prices = np.array([100, 250, 80, 150, 300])

updated_prices = prices + 20

print("Updated prices:", updated_prices)