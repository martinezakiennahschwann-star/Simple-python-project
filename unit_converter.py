print("=== SIMPLE UNIT CONVERTER ===")
print("1. Length")
print("2. Weight")
print("3. Time")

choice = input("Choose a category (1/2/3): ")

# LENGTH CONVERTER
if choice == "1":
    print("\nLength Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")

    length_choice = input("Choose (1/2): ")
    value = float(input("Enter the value: "))

    if length_choice == "1":
        print("Result:", value / 1000, "kilometers")
    elif length_choice == "2":
        print("Result:", value * 1000, "meters")
    else:
        print("Invalid choice")

# WEIGHT CONVERTER
elif choice == "2":
    print("\nWeight Converter")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Grams")

    weight_choice = input("Choose (1/2): ")
    value = float(input("Enter the value: "))

    if weight_choice == "1":
        print("Result:", value / 1000, "kilograms")
    elif weight_choice == "2":
        print("Result:", value * 1000, "grams")
    else:
        print("Invalid choice")

# TIME CONVERTER
elif choice == "3":
    print("\nTime Converter")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")

    time_choice = input("Choose (1/2): ")
    value = float(input("Enter the value: "))

    if time_choice == "1":
        print("Result:", value / 60, "minutes")
    elif time_choice == "2":
        print("Result:", value * 60, "seconds")
    else:
        print("Invalid choice")

else:
    print("Invalid category selected")