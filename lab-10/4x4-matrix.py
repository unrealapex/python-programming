def sumColumn(matrix, column):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][column]
    print(f"Sum of the elements for column {column} is {sum}")

sumColumn([[1.5, 2, 3, 4], [5.5, 6, 7, 8], [9.5, 1, 3, 1]], 1)
