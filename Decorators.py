# g = (x*x for x in range(1, 10))
#
# print(list(g))
#
# def gen():
#     for i in range(1, 10):
#         yield i**2

# print(list(gen())
#
# for i in g:
#     print(i, end='\n')
#
# for i in gen():
#     print(i, end='\n')

# v1.0
# def make_pretty(func):
#     def inner():
#         print('Hi')
#         func()
#         print('BYE!')
#     return inner
#
#
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#     g = (x * x for x in range(1, 10))
#     print(list(g))



# v2.0
# def make_pretty(func):
#     print('Hi')
#     func()
#     print('Bye')
#
# def ordinary():
#     print("I am ordinary")
#     g = (x * x for x in range(1, 10))
#     print(list(g))

# make_pretty(ordinary)

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#         return func(a, b)
#     return inner
#
# @smart_divide
# def divide(a, b):
#     return a/b
#
# print(divide(1, 2))
# print(divide(1, 0))

