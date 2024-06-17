day = input("Enter the day of the week: ")

match day:
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend.")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is a weekday.")
    case _:
        print("That's not a valid day of the week.")