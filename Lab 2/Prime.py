def is_prime(number):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count+=1

    if count>2:
        return False
    else:
       return True

if __name__=="__main__":
    n=int(input("enter the number to check it is prime ort not "))
    if n<0:
        print("please enter a non negative number")
    elif n==0:
        print("enter number greater than 0")
    else:
        if is_prime(n):
            print("yes it is a prime number")
        else:
            print("no it is not a prime number")

    start=int(input("enter the starting number  "))
    end=int(input("enter the last number  "))

    if start<0 and end<0:
        print("please enter non negative number")

    elif start>end:
        print("starting number should be less or equal to ending")

    else:
        for i in range(start,end+1):
            if is_prime(i):
                print(i,end=" ")

