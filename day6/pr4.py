import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))
print("Shape:", np.dot(A, B).shape)

print("A * B:\n", A * B)
print("Shape:", (A * B).shape)


print("B dot A:\n", np.dot(B, A))
print("B * A:\n", B * A)