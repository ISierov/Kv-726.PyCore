"""
create a function that takes in a list and returns a list with the reverse order.
Examples (Input -> Output)
* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]
"""
def reverse_list(l):
    reverse_l = l[::-1]
    return reverse_l