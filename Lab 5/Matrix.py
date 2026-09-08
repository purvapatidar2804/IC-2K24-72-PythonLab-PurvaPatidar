def matrix_operations():
    matrix = []

    print("Enter the elements of 3x3 matrix:")

    for i in range(3):
        row = []
        for j in range(3):
            value = int(input(f"Enter element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)

    # Display matrix
    print("\nMatrix:")
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=" ")
        print()

    # Sum of all elements
    total = 0
    for i in range(3):
        for j in range(3):
            total += matrix[i][j]

    print("\nSum of all elements:", total)

    # Sum of main diagonal
    diagonal_sum = 0
    for i in range(3):
        diagonal_sum += matrix[i][i]

    print("Sum of main diagonal:", diagonal_sum)

    # Largest and smallest element
    largest = matrix[0][0]
    smallest = matrix[0][0]

    for i in range(3):
        for j in range(3):
            if matrix[i][j] > largest:
                largest = matrix[i][j]

            if matrix[i][j] < smallest:
                smallest = matrix[i][j]

    print("Largest element:", largest)
    print("Smallest element:", smallest)

    # Transpose
    print("\nTranspose:")
    for i in range(3):
        for j in range(3):
            print(matrix[j][i], end=" ")
        print()


matrix_operations()