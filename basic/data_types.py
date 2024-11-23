#
# Author: Rohtash Lakra
#
def full_name(first_name: str, last_name: str, middle_name: str = None) -> str:
    """Returns the name"""
    if first_name and middle_name and last_name:
        return "{} {} {}".format(first_name.title(), middle_name.title(), last_name.title())
    elif first_name and last_name:
        return "{} {}".format(first_name.title(), last_name.title())
    # elif first_name and middle_name:
    #     return "{} {}".format(first_name.title(), middle_name.title())
    # elif middle_name and last_name:
    #     return "{} {}".format(middle_name.title(), middle_name.title())
    elif first_name:
        return first_name.title()
    elif last_name:
        return last_name.title()

    return None


print()
fullName = full_name("first", "last", "middle")
print("fullName={}".format(fullName))
assert fullName == "First Middle Last"
firstAndLastName = full_name("first", "last")
print("firstAndLastName={}".format(firstAndLastName))
assert firstAndLastName == "First Last"
firstNameOnly = full_name("first", None)
print("firstNameOnly={}".format(firstNameOnly))
assert firstNameOnly == "First"
lastNameOnly = full_name(None, "last")
print("lastNameOnly={}".format(lastNameOnly))
assert lastNameOnly == "Last"
noName = full_name(None, None)
print("noName={}".format(noName))
assert noName == None
print()
