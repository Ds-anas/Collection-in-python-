# Return the sum and difference of two numbers
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
total, difference = calculation(x, y)
print("Addition:", total)
print("Subtraction:", difference)
