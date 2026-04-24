import math


def NULL_not_found(object: any) -> int:
    """Print null-like object information and return status."""
    if type(object) is bool and object is False:
        print(f"Fake: {object} <class 'bool'>")
    elif type(object) is float and math.isnan(object):
        print("Cheese: nan <class 'float'>")
    elif type(object) is int:
        print(f"Zero: {object} <class 'int'>")
    elif type(object) is str and object == "":
        print("Empty:  <class 'str'>")
    elif object is None:
        print("Nothing: None <class 'NoneType'>")
    else:
        print("Type not Found")
        return 1

    return 0
