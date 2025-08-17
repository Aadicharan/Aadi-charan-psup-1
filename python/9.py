char = input("Enter a single alphabet: ").lower()

if char in 'aeiou':
    print("It is a vowel.")
elif char.isalpha():
    print("It is a consonant.")
else:
    print("Invalid input.")
