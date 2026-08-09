input = input("Enter Train seat type (sleeper/AC/general/luxuary)").lower()

match input:
    case "sleeper":
        print("You have selected sleeper and only avalaible beds & no AC")
    case "ac":
        print("You have selected AC coach with air conditioning and comfortable seats")
    case "general":
        print("You have selected general coach with no AC and no beds")
    case "luxuary":
        print("You have selected luxuary coach with beds and AC")
    case _:
        print("Invalid seat type Please select correct seat")