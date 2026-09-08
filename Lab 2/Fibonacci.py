def fibonacci_loop(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c

def fibonacci_recursive(n,count):
    count[0] += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1, count) + fibonacci_recursive(n - 2, count)
if __name__=="__main__":
    n = int(input("Enter the number of terms: "))

    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Loop version
        print("\nFibonacci series using loop:")
        fibonacci_loop(n)

        # Recursive version
        print("\n\nFibonacci series using recursion:")

        count = [0]

        for i in range(n):
            print(fibonacci_recursive(i, count), end=" ")

        print("\nNumber of recursive function calls:", count[0])