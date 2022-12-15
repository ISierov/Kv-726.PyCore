'''
In this kata you will be given a positive integer, val and you have to create the function
next_pal()(nextPal Javascript) that will output the smallest palindrome number higher than val.
next_pal(11) == 22
next_pal(188) == 191
next_pal(191) == 202
next_pal(2541) == 2552
You will be receiving values higher than 10, all valid.
'''


def next_pal (val):
    next_num = val + 1
    while  str(next_num) != str(next_num)[::-1]:
        next_num += 1
    return next_num

# #ще
# def next_pal(val):
#     next_num = val + 1
#     while True:
#         next_num += 1
#         if str(next_num) == str(next_num)[::-1] :
#             return next_num
