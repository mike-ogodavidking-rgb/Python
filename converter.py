while True:
    while True:
        try:
            distance = float(input("Enter distance in meters: "))
            if distance < 0:
                print("Distance cannot be negative. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("That's not a valid number. Try again.")
    feet = distance * 3.28084
    centimeters = distance * 100
    inches = distance * 39.3701
    choice = input("Choose a unit to convert to (feet, centimeters, inches): ").lower()
    if choice == "feet":
        print(f"{distance} meters is {feet:.2f} feet")
    elif choice == "centimeters":
        print(f"{distance} meters is {centimeters:.2f} centimeters")
    elif choice == "inches":
        print(f"{distance} meters is {inches:.2f} inches")
    else:
        print("Invalid choice. Please enter feet, centimeters, or inches.")

    answer = input("Do you want to convert another distance? (yes/no): ").lower()
    if answer == "no":
        print("Thank you for using the distance converter. Goodbye!")
        break