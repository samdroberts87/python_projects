def is_even(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    return number % 2 == 0
