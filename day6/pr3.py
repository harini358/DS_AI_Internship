import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.dot(a,b))
print(np.matmul(a,b))
print(a@b)

print(a.T)

print(np.linalg.det(a))

print(np.linalg.inv(a))