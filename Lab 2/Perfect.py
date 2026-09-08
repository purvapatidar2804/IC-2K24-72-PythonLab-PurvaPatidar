def is_perfect(number):
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum+=i

    if sum==number:
        return True
    else:
        return False

if __name__=="__main__":
    x=int(input("enter the numbers to check it is perfect number or not"))
    if x<0 or x==0:
        print("enter number greater tha 0")
    else:
        if is_perfect(x):
            print("yes",x,"is a perfect number")
        else:
            print("no",x,"is not a perfect nnumber")

    limit = int(input("\nEnter the limit: "))

    if limit <= 0:
        print("Please enter a number greater than 0.")
    else:
        print("Perfect numbers up to", limit, "are:")

        for i in range(1, limit + 1):
            if is_perfect(i):
                print(i, end=" ")

        print()