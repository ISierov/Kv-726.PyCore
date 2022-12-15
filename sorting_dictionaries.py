"""
Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?
Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).
The list must be sorted by the value and be sorted largest to smallest.
Examples
sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]
"""
def sort_dict(d):
    is_sorted = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return is_sorted

# or is_sorted = sorted(d.items(), key=lambda item: -item[1])
# or is_sorted = sorted(d.items(), key=lambda item: item[1])[::-1]

# #or
# def sort_dict(d):
#     is_sorted = sorted(d.items())
#     is_sorted.sort(key=lambda item: item[1], reverse=True)
#     return is_sorted
