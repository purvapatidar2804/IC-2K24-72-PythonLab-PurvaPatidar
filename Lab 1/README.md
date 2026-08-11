# Lab 1 - Python Programs

## 1. Variable and Identifier Practice

### Aim
To declare variables of different data types and display their values along with their data types using `type()`.

### Logic
1. Declare variables for name, age, height, and student status.
2. Store values of different data types in these variables.
3. Use `print()` to display each variable.
4. Use `type()` to display the data type of each variable.

### Sample Input
No user input is required.

### Sample Output
Name: Purva Type: <class 'str'>
Age: 20 Type: <class 'int'>
Height: 5.4 Type: <class 'float'>
Student: True Type: <class 'bool'>

## 2. Greeting Program

### Aim
To take the user's name, age, and city as input and display them in a single sentence using an f-string.

### Logic
1. Take the user's name as input.
2. Take the user's age as input.
3. Take the user's city as input.
4. Use an f-string to combine all three values into one sentence.
5. Display the greeting.

### Sample Input
Enter your name: Purva Patidar
Enter your age: 20
Enter your city: kuwan

### Sample Output
Hello Purva Patidar, you are 20 years old and you live in kuwan.

## 3. Arithmetic Operations

### Aim
To take two numbers as input and perform basic arithmetic operations such as addition, subtraction, multiplication, division, and remainder.

### Logic
1. Take two numbers as input from the user.
2. Convert the inputs into floating-point numbers.
3. Perform addition, subtraction, multiplication, division, and remainder operations.
4. Display each result with a clear label.

### Sample Input
Enter first number: 10
Enter second number: 5

### Sample Output
Sum: 15.0
Difference: 5.0
Product: 50.0
Quotient: 2.0
Remainder: 0.0

## 4. Celsius to Fahrenheit

### Aim
To convert a temperature from Celsius to Fahrenheit using the given conversion formula.

### Logic
1. Take the temperature in Celsius as input.
2. Convert the input into a floating-point number.
3. Apply the Celsius to Fahrenheit conversion formula.
4. Display the temperature in Fahrenheit.

### Formula
F = (C × 9/5) + 32

### Sample Input
Enter temperature in Celsius: 25

### Sample Output
Temperature in Fahrenheit: 77.0

## 5. String Manipulation

### Aim
To perform different string manipulation operations on a full name using Python string methods.

### Logic
1. Take a full name as input from the user.
2. Convert the name into uppercase using `upper()`.
3. Convert the name into lowercase using `lower()`.
4. Reverse the name using slicing.
5. Find the length of the name using `len()`.
6. Use `title()` and `strip()` string methods for additional string manipulation.
7. Display all the results.

### Sample Input
Enter your full name: Purva Patidar

### Sample Output
Uppercase: PURVA PATIDAR
Lowercase: purva patidar
Reversed: raditaP avruP
Length: 13
Title Case: Purva Patidar
Stripped Name: Purva Patidar


## 6. Escape Sequence Practice

### Aim
To print a simple receipt using escape sequences such as \t and \n.

### Logic
1. Print the heading of the receipt.
2. Use `\n` to create a new line.
3. Use `\t` to create tab spaces and align the item names and prices.
4. Display the items and their prices.
5. Display the total amount.

### Sample Input
No user input is required.

### Sample Output
RECEIPT

Item        Price
------------------------
Pen         20
Notebook    50
Pencil      10
------------------------
Total       80

## 7. Menu Driven Calculator

### Aim
To build a menu-driven calculator that performs basic arithmetic operations and continues until the user chooses to exit.

### Logic
1. Display a menu containing addition, subtraction, multiplication, division, and exit options.
2. Take the user's choice as input.
3. If the user selects an arithmetic operation, take two numbers as input.
4. Perform the selected operation and display the result.
5. Continue displaying the menu until the user selects the exit option.
6. Handle division by zero using a condition.

### Sample Input
Enter your choice: 1
Enter first number: 10
Enter second number: 3

Enter your choice: 5

### Sample Output
Result: 13.0
Calculator exited.