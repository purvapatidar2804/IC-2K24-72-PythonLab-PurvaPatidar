def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


n = int(input("Enter number of rows: "))
inverted_triangle(n)