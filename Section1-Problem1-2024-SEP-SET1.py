def is_even_two_digit_number(num):
    """
    Determines whether a given number is an even two-digit number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if `num` is an even two-digit number, False otherwise.

    Examples:
        >>> is_even_two_digit_number(42)
        True
        >>> is_even_two_digit_number(99)
        False
        >>> is_even_two_digit_number(-48)
        True
        >>> is_even_two_digit_number(5)
        False
    """
    
    return num % 2 == 0 and 10 <= abs(num) < 100

# #Another Method:
# def is_even_two_digit_number(num):
    
#     if len(str(abs(num)))==2 and num%2==0:
#         return True
#     else:
#         return False

# Check If Even Two-Digit Number
# Write a function is_even_two_digit_number that checks whether a given number is an even two-digit number.

# A number is considered a two-digit number if it has exactly two digits excluding any negative sign.



# For example:

# 24 is an even two-digit number.
# -36 is an even two-digit number.
# 5 is not a two-digit number.
# 101 is not a two-digit number.
# -19 is not an even number.



