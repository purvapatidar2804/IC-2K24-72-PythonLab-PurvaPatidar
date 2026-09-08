def hollow_diamond(n):
    for i in range(n):
        if i <= n // 2:
            spaces = n // 2 - i
        else:
            spaces = i - n // 2

        print(" " * spaces, end="")

        if i == 0 or i == n - 1:
            print("*")
        else:
            inner_spaces = n - 2 * spaces - 2
            print("*" + " " * inner_spaces + "*")


n = int(input("Enter an odd number: "))

if n > 0 and n % 2 != 0:
    hollow_diamond(n)
else:
    print("Please enter a positive odd number.")