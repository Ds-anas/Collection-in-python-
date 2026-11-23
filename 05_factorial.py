# Find factorial of a non-negative integer
def factorial(number):
    if number < 0:
        return None
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result

n = int(input("Enter a non-negative integer: "))
answer = factorial(n)
if answer is None:
    print("Please enter a non-negative integer.")
else:
    print("Factorial:", answer)
