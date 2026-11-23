# Find the largest item without using max()
def largest_item(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

values = [12, 45, 7, 89, 23]
print("List:", values)
print("Largest item:", largest_item(values))
