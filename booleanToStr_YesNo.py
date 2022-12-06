"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""
def bool_to_word(boolean):
    bool_str = str(boolean)
    if bool_str == 'True':
        return 'Yes'
    else:
        return 'No'


# or just
#   return 'Yes' if str(boolean) == 'True' else 'No'