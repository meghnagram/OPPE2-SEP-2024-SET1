# Write your code here

# Read the number of names
n = int(input())
names = []

# Process each name
for _ in range(n):
    name = input()
    parts = name.split()
    # Create the abbreviated name
    short_name = f'{". ".join(map(lambda x: x[0], parts[:-1]))}. {parts[-1]}'
    names.append(short_name)

# Sort and print the results
for name in sorted(names):
    print(name)

# #Another Method:
# # Write your code here

# a=int(input())
# k=[]

# while(a!=0):
    
#     a -=1
#     b = input()
#     l=b.split(' ')
#     j=l[-1]
#     s=''
#     for i in l:
#         if j==i:
#             s=s+j 
#         else: 
#             s=s+i[0]+'. '
#     k.append(s) 
#     s=''
        
# k.sort()
# for i in k:
#     print(i)


# Abbreviate Initials And Sort
# Write a program that takes a list of full names and outputs their initials (except the last name) followed by the full last name. The output should be sorted alphabetically.

# An initial is the first letter of each part of a name.

# Assume that the names are given in the correct case.

# Hint: Use sorted function or list.sort to sort the list

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# First line contains the number of names, n.
# Next n lines contain one full name per line.
# Output Format

# Output the processed names in sorted order, one per line.
# Example

# Input:

# 3
# John Doe
# Alice Johnson
# Bob Alan Rickman
# Output:

# A. Johnson
# B. A. Rickman
# J. Doe


