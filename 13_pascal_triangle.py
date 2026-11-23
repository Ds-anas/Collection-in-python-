# Print the first n rows of Pascal's triangle
def pascal_triangle(rows):
    for row in range(rows):
        number = 1
        print(" " * (rows - row), end="")
        for column in range(row + 1):
            print(number, end=" ")
            number = number * (row - column) // (column + 1)
        print()

n = int(input("Enter number of rows: "))
if n > 0:
    pascal_triangle(n)
else:
    print("Enter a positive number of rows.")
