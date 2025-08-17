choice = int(input("Choose fuel type (1: Petrol, 2: Diesel, 3: Electric): "))

match choice:
    case 1: print("You chose Petrol.")
    case 2: print("You chose Diesel.")
    case 3: print("You chose Electric.")
    case _: print("Invalid choice.")
