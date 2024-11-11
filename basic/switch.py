#
# Author: Rohtash Lakra
#
def get_day_type(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case "Saturday" | "Sunday":
            return "Weekend"
        case _:
            return "Invalid day"


print(get_day_type("Monday"))
print(get_day_type("Saturday"))
print(get_day_type("Invalid"))
