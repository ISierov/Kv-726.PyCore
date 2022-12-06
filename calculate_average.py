"""
Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
"""

def find_average(numbers):
    s = sum(numbers)
    l = len(numbers)
    av = s/l
    return av