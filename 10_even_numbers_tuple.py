# Print even numbers from a tuple
def print_even_numbers(values):
    for value in values:
        if value % 2 == 0:
            print(value, end=" ")

numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print("Even numbers:")
print_even_numbers(numbers)
print()
