def diamond(n):
    # Upper half
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(spaces + stars)

    # Lower half
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(spaces + stars)


n = int(input("Enter number of rows: "))
diamond(n)