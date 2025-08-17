char = input("Enter a single character: ")

if char.isalpha():
    print("It is an alphabet.")
elif char.isdigit():
    print("It is a digit.")
else:
    print("It is a special character.")
