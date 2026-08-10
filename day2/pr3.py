nums=[]
while True:
    n=input("enter numbers:")
    if n.lower()=="done":
        break
    nums.append(int(n))
print("minimum numbers:",min(nums))
print("maximum numbers:",max(nums))
print("sum of numbers:",sum(nums))
print("avg of numbers:",sum(nums)/len(nums))
print("total length:",len(nums))
print("sorted:",sorted(nums))