# Find the sum of all numbers in a list
def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [10, 20, 30, 40]
print("List:", numbers)
print("Sum:", list_sum(numbers))
