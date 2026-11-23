# Count local variables declared inside a function
def demo():
    first = 10
    second = 20
    message = "Hello"
    return len(locals())

print("Number of local variables:", demo())
