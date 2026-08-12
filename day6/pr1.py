import numpy as np
marks=np.array([[60,70,80],[70,80,90],[70,80,60]])
print(marks)

print(np.mean(marks))
print(marks.shape)
result=np.mean(marks,axis=1)
print(result)
print(result.shape)
results=np.mean(marks,axis=0)
print(results)

print(np.median(marks,axis=1))
print(np.median(marks,axis=0))

print(np.std(marks))

print(np.var(marks))