# Check whether a number is within a given range
def in_range(number, start, end):
    return start <= number <= end

number = int(input("Enter a number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))
if in_range(number, start, end):
    print("The number is in the range.")
else:
    print("The number is not in the range.")
