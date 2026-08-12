import pandas as pd
import numpy  as np
x=[1,2,3,4]#list
y=pd.Series(x)
print(y)

x=np.array([2,4,6])#numpy array
y=pd.Series(x)
print(y.to_string())

#dictionary
x={"math":80,"science":85,"english":90}
y=pd.Series(x)
print(y[['math','science']])
print(y[y>80])#selection
print(y.index[2],":",y.iloc[2])#indexing

s1=pd.Series([10,20,30,40])
s2=pd.Series([10,20,30],index=['a','b','c'])
print(s1)
print(s2)

marks=[80,90,75]
x=pd.Series(marks,index=["math","science","hindi"])
print(x)
print(x.index.tolist())

marks=pd.Series([85,90,78],index=['math','physics','chemistry'])
print(marks['math'])
print(marks[['math','chemistry']])

scores=pd.Series([45,67,89,34,90])
passed=scores[scores>60]
print(passed)#boolean

#handling missing data
data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(0))

names=pd.Series(['Alice','bob','CHARLIE'])
print(names.str.lower())
print(names.str.contains('a'))