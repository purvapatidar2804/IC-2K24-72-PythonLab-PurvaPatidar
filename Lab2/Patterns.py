def star_pattern(n):
    print("\n Right Triangle of Stars: ")

    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()

def number_pattern(n):
    print("\n Numbers patterns: ")

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def pyramid_patterns(n):
    print("Pyramid Patterns: ")
    for i in range(1, n + 1):

        for j in range(n - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()

def print_patterns(n):
    if n<=0:
        print("please enter a +ve number")
    else:
        star_pattern(n)
        number_pattern(n)
        pyramid_patterns(n)

if __name__=="__main__":
    n=int(input("enter the number of rows:"))
    print_patterns(n)
