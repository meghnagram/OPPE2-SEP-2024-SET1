def count_odd_three_digit_nums(nums):
    
    
    # count = 0
    # for num in nums:
    #     if num is not None and num%2 and len(str(abs(num)))==3:
    #         count += 1
    # return count
    return sum(
       1
       for num in nums
       if num is not None  and num%2 and len(str(abs(num)))==3
    )
    
# #Another Method:
# def count_odd_three_digit_nums(nums):
#     c=0
#     for num in nums:
#         if num==None:
#             continue
#         elif len(str(abs(num)))==3 and num%2==1:
#             c=c+1
#     return c


# Count Odd 3 Digit Numbers (Ignore None)
# Write a function count_odd_three_digit_nums(nums) that takes a list of integers nums and returns the count of numbers that are:

# Odd.
# Three-digit numbers (ignoring the negative sign if present).
# Not None.

# Examples:
# count_odd_three_digit_nums([101, -203, None, 99, 300]) → 2
# Explanation: 101 and -203 are odd three-digit numbers, ignoring None.
# count_odd_three_digit_nums([None, 120, 301, -401, 78]) → 2
# Explanation: 301 and -401 qualify as odd three-digit numbers.
# count_odd_three_digit_nums([10, 305, 507, 99]) → 2
# Explanation: 305 and 507 qualify as odd three-digit numbers.
