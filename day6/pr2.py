import numpy as np

sales = np.array([
    [100, 150, 200],  
    [120, 160, 180],  
    [90,  140, 210],  
    [110, 170, 190],  
    [130, 155, 220]   
])

print(sales)

print("product wise")
print(np.mean(sales, axis=0))
print(np.median(sales, axis=0))
print(np.var(sales, axis=0))
print(np.std(sales, axis=0))

print("day wise")
print(np.mean(sales, axis=1))
print(np.median(sales, axis=1))
print(np.var(sales, axis=1))
print(np.std(sales, axis=1))

