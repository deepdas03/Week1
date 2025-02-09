string = input("Enter a string: ")
upper_count = sum(1 for c in string if c.isupper())
lower_count = sum(1 for c in string if c.islower())

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
