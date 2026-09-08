def is_palindrome(number):
    rev=0
    sum=0
    original=number
    while number>0:
        rem=number%10
        rev=rev*10+rem
        number=number//10

    if original==rev:
        return True
    else:
        return False

if __name__=="__main__":
    x=int(input("enter the number "))
    if is_palindrome(x):
        print("yes it is palindrfome")

    else:
        print("no its is not a plaindrome")


    text=input("Enter a string")
    reversed_txt=text[::-1]

    if text==reversed_txt:
        print("yes palindrome")
    else:
        print("not palindorme")