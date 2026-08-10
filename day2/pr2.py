print("welcome to shopping cart")
cart=[]
while True:
    item=input("enter cart item:")
    if item.lower()=="done":
        break
    cart.append(item)
print("type:",type(cart))
print("total items:",len(cart))
print("cart:",cart)
tuple=tuple(cart)
print("type:",type(tuple))
print("items:",tuple)
print("checkout")