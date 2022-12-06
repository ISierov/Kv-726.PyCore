"""
The zoo keeper is concerned that perhaps the animals do not have the right tails.
To help her, you must correct the broken function to make sure that the second argument (tail),
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
If the tail is right return true, else return false.
The arguments will always be non empty strings, and normal letters.
DEBUGGING
"""
# def correct_tail(body, tail):
#     sub = body.substr(len(body) - len(tail.length)
#     if sub = tai:
#     return True
#     else:
#     return False

def correct_tail(body, tail):
    body_end = body[-1]
    tail_start = tail[0]
    if body_end == tail_start:
        return True
    else:
        return False
