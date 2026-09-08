from Armstrong import is_armstrong
from Prime import is_prime
from Perfect import is_perfect
from Palindrome import is_palindrome
from Fibonacci import fibonacci_loop
from Patterns import print_patterns

x=True
while x==True:
    print("\n===== MENU =====")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")

    choice=input("enter the choice  ")

    if choice=="1":
        n = int(input("Enter a number: "))

        if n < 0:
            print("Please enter a non-negative number.")

        elif is_armstrong(n):
            print("Yes, it is an Armstrong number.")
        else:
            print("No, it is not an Armstrong number.")

    elif choice == "2":

            n = int(input("Enter a number: "))

            if n < 2:
                print("Please enter a number greater than 1.")
            elif is_prime(n):
                print("Yes, it is a prime number.")
            else:
                print("No, it is not a prime number.")

    elif choice == "3":

            n = int(input("Enter a number: "))

            if n <= 0:
                print("Please enter a positive number.")
            elif is_perfect(n):
                print("Yes, it is a perfect number.")
            else:
                print("No, it is not a perfect number.")

    elif choice == "4":

            n = int(input("Enter a number: "))

            if n < 0:
                print("Please enter a non-negative number.")
            elif is_palindrome(n):
                print("Yes, it is a palindrome.")
            else:
                print("No, it is not a palindrome.")

    elif choice == "5":

            n = int(input("Enter the number of terms: "))

            if n <= 0:
                print("Please enter a positive number.")
            else:
                print("Fibonacci Series:")
                fibonacci_loop(n)

    elif choice == "6":

            n = int(input("Enter the number of rows: "))

            if n <= 0:
                print("Please enter a positive number.")
            else:
                print_patterns(n)

    elif choice == "7":

            print("Thank you for using the application!")
            x=False

    else:
        print("Invalid choice")