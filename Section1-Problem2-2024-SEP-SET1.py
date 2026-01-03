def is_dot_com_or_dot_in(domain):
    """
    Checks whether a given domain ends with '.com' or '.in'.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain ends with '.com' or '.in', False otherwise.

    Examples:
        >>> is_dot_com_or_dot_in('example.com')
        True
        >>> is_dot_com_or_dot_in('example.in')
        True
        >>> is_dot_com_or_dot_in('example.org')
        False
        >>> is_dot_com_or_dot_in('mywebsitein')
        False
    """
    
    return domain[-4:] == '.com' or domain[-3:] == '.in'

# #Another Method

# def is_dot_com_or_dot_in(domain):
#     if '.com' in domain or '.in' in domain:
#         return True
#     else:
#         return False

# Check If the given domain is .com or .in
# Write a function is_dot_com_or_dot_in(domain) that takes a string domain and checks whether it ends with .com or .in.
# The function should return True if the domain has the specified suffix; otherwise, it should return False.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples

# is_dot_com_or_dot_in("example.com") -> True
# Explanation: The domain ends with .com.
# is_dot_com_or_dot_in("website.in") -> True
# Explanation: The domain ends with .in.
# is_dot_com_or_dot_in("mydomain.org") -> False
# Explanation: The domain does not end with .com or .in.
# is_dot_com_or_dot_in("invalidcom") -> False
# Explanation: The domain does not end with .com or .in.
    
