def is_armstrong(number):
    sum=0
    original=number
    while number>0:
        rem=number%10
        sum=sum+(rem**3)
        number=number//10

    if original==sum:
        return True
    else:
        return False


if __name__=="__main__":
    x=int(input("entr the number to check whether it is armstrong or not "))
    if x<0:
        print("Please enter a non negative number")
    else:
        print(is_armstrong(x))

    start = int(input("\nEnter starting value: "))
    end = int(input("Enter ending value: "))

    if start < 0 or end < 0:
        print("Please enter non-negative values.")
    elif start > end:
        print("Starting value must be less than or equal to ending value.")
    else:
        print("Armstrong numbers between", start, "and", end, "are:")

    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number, end=" ")

    print()
    