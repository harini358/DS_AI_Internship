prices = [100, 250, 80, 150, 300]
new_price=[]
for i in prices:
    new_price.append(i+20)
    print("Updated prices:",new_price)


import numpy as np
prices = np.array([100, 250, 80, 150, 300])
updated_prices = prices + 20
print("Updated prices:", updated_prices)