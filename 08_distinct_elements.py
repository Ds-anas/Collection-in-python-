# Return distinct elements from a list
def distinct_elements(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

values = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", values)
print("Distinct elements:", distinct_elements(values))
