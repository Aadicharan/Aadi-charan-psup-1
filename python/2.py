char = input("Enter a single character: ")
if len(char) != 1:
    print("Please enter exactly one character.")
else:
    if char.isupper():
        print("The character is uppercase.")
    else:
        print("The character is not uppercase.")