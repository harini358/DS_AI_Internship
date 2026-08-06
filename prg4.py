def table(n):
    print("Multiplication Table of", n)

    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number: "))
table(num)