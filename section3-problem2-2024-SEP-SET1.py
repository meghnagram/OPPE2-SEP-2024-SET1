
with open(filename) as f:
    vowel_count = 0
    for line in f:
        for char in line:
            if char in 'aeiou':
                if vowel_count % 2 == 0:
                    print("ub", end="")
                else:
                    print("dub", end="")
                vowel_count += 1
            print(char, end="")

# #Another Method:

# with open(filename,'r') as file:
#     def ub(s):
#         return('ub'+s)
#     def dub(s):
#         return('dub'+s)
#     c=1
#     for line in file:
#         for j in line:
#             if j in 'aeiou':
#                 if c%2==1:
#                     print(ub(j),end='')
#                     c=c+1
#                 else:
#                     print(dub(j),end='')

# Ubbi Dubbi - Add "ub" and "dub" Alternately Before Vowels in the Text
# Given a text file containing lowercase letters, modify the text such that:

# Before each vowel, add the string "ub" if it is the first or an odd-numbered vowel encountered.
# Add "dub" before the vowel if it is the second or an even-numbered vowel encountered.
# Preserve the text's original formatting, including spaces and newlines.
# Assume the input text is all lowercase and may have multiple lines.

# Examples

# Input

# hello world
# pyhton is good
# Output

# hubelldubo wuborld
# pythdubon ubis gduboubod


  
