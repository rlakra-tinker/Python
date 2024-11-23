#
# Author: Rohtash Lakra
#
def full_name(first_name: str, last_name: str, middle_name: str = None) -> str:
    """Returns the full-name based on the provided parameters"""
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


