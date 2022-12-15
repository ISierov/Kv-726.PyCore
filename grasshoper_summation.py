"""
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
For example:
summation(2) -> 3
1 + 2
summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
FUNDAMENTALSMATHEMATICS
"""

def summation(num):
    sum = (num * (num + 1)) //2
    return sum

# # or
# def summation(num):
#     sum = 0
#     x = range(num+1)
#     for i in x:
#         sum += i
#     return sum

