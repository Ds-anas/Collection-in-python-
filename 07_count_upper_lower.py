# Count uppercase and lowercase letters
def count_letters(text):
    upper = 0
    lower = 0
    for character in text:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
    return upper, lower

text = input("Enter a string: ")
upper, lower = count_letters(text)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
