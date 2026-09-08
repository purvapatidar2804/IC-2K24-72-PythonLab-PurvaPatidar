# Lab 2 - Python Programs

## 1.Arsmtrong Numbers

### Aim:
To check whether a given number is an Armstrong number and to print all Armstrong numbers within a given range.

### Logic:
The program extracts each digit using arithmetic modulous operator and calculates the sum of its cubes. It then compares the calculated value with the original number and uses the same function to find Armstrong numbers in a range.

### Sample Input:
153
300,700

### Sample Output
true
370,371 and 407


## 2.Prime Numbers

### Aim:
To check whether the given number is prime number or not and print all prime numbers betweena given range

### Logic:
program takes input and check the number of factors of input using % and == operator .if total no of cator  is 2 then it is prime

### Sample Input
67
14 to 90

### Sample Output
yes it is a prime number
17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 


## 3.Perfect Numebrs

### Aim:
to check whether a given number is perfect number or nor and print all perfect numbers within a given limit

### Logic:
A number is called a Perfect Number if the sum of all its proper divisors  is equal to the number itself.

### Sample Input:
28
1000

### Sample output:
yes 
6 28 496


## 4.Palindrome Check

### Aim:
To check whether a given number is a palindrome using arithmetic operations without converting it into a string, and to check whether a given string is a palindrome.

### Logic:
For the number, the program reverses the digits using % and // operators and compares the reversed number with the original number. For the string, the program reverses the entered string and compares it with the original string.

### Sample input:
1221
naman

### Sample ouput:
yes palindrome
yes palindorme


## 5.Fibonacci series

### Aim:
To print the first n terms of the Fibonacci series using a loop and recursion, and compare the recursive approach by counting the number of function calls.

### Logic:
he loop version generates each term by adding the previous two terms. The recursive version calculates each Fibonacci term by calling itself for the two previous terms, while a counter keeps track of the recursive function calls.

### Sample Inout
10

### Sample output
 Output using loop:
0 1 1 2 3 5 8 13 21 34

Output using recursion:
0 1 1 2 3 5 8 13 21 34


## 6.Pattern Printing

### Aim:
To print a right-angled star triangle, a number pattern, and a centered pyramid pattern using nested loops.

### logic:
The program uses separate functions for each pattern and nested loops to control rows, spaces, numbers, and stars. A main function calls all three pattern functions after validating the number of rows entered by the user.

### Sample input
5

### Sample output
Right-angled triangle of stars:
*
* *
* * *
* * * *
* * * * *

Number pattern:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Centered pyramid:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


## 7. Menu Driven 

### Aim:
To combine the programs from 1 to 6 into a single menu-driven application that allows the user to select and execute different operations until they choose to exit.

### Logic:
The program imports the functions from the previous Python files and displays a menu using a while loop. The user's choice determines which function is executed, and invalid choices are handled without terminating the program.

### Sample Input
1,2,3,4,5,6,7

### SAmple Output
Yes, it is an Armstrong number.
Yes, it is a prime number.
Yes, it is a perfect number. and much more

## 8.Number Guessing Game

### Aim:
To create a number guessing game in which the computer randomly selects a number between 1 and 100 and the user gets a maximum of 7 attempts to guess it.

### Logic:
The program generates a random number using the random module and compares each valid guess with the secret number. It informs the user whether the guess is too high or too low and displays the number of attempts when the correct number is guessed.

### Sample input and output
I have chosen a number
you have 7 chances to guess it
enter you guess45
number is too low
enter you guess 67
number is too low
enter you guess87
number is too high
enter you guess77
number is too low
enter you guess80
CONGRATULATIONS!!!!! you guessed it right
Number of attempts: 5


# ANALYSIS
1.I preferred the for loop for Prime Number, Perfect Number, Fibonacci Series, and Pattern Printing because the number of iterations or range was known. I preferred the while loop for Armstrong Number, Palindrome, and Number Guessing Game where the loop depended on changing values or user input.

2.The recursive version repeats more work as n grows because the same smaller Fibonacci values are calculated multiple times. The loop-based version calculates each term only once, so it is more efficient.

3.We only need to test divisors up to √n. If a number has a factor greater than √n, it must have a corresponding factor smaller than √n, so checking beyond √n is unnecessary.

4.he user can use the Binary Search strategy. They should guess the middle value of the remaining range each time and then eliminate half of the possible numbers based on whether the guess is too high or too low.