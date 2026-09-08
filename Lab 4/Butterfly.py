def butterfly(n):
    for i in range(1, n + 1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)

    
    for i in range(n - 1, 0, -1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)


n = int(input("Enter number of rows: "))

if n > 0:
    butterfly(n)
else:
    print("Please enter a positive number.")