# Check whether a number is perfect
def is_perfect(number):
    if number <= 1:
        return False
    total = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            total += divisor
    return total == number

n = int(input("Enter a positive number: "))
if is_perfect(n):
    print(n, "is a perfect number.")
else:
    print(n, "is not a perfect number.")
