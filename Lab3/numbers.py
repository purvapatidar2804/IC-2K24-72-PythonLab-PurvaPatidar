def number_pattern(n):
    size = 2 * n - 1

    for i in range(size):
        for j in range(size):
            value = max(abs(i - (n - 1)), abs(j - (n - 1))) + 1
            print(value, end=" ")
        print()


n = int(input("Enter the number: "))
number_pattern(n)