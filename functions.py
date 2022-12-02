# def greet(name):
#     """
#     Greeting function
#     :param name: name of someone
#     :return: Nothing
#     """
#     print(f'Hello, {name}. How are you?')
#     return
#
# greet('Ivan')

# greet('Andrii')
# greet('Liubov')

# def my_sum(arg1, arg2):
#     total = arg1 + arg2
#     print("Inside the function : ", total)
#     return total
#     print("After operator the return")
#
#
# suma = my_sum(10, 20)
# print("Outside the function : ", suma)

# def my_print(str):
#     print(str)
#
# my_print("first call function!")
# my_print()
#
# def print_info(name, age):
#     print("Name: ", name)
#     print("Age: ", age)
#
# print_info(age=30, name="Alex")
# print("-" * 10)
# print_info(30, "Alex")

# def print_info(name, age=18):
#     print("Name: ", name)
#     print("Age: ", age)
#
# print_info("Alex")
# print("-" * 10)
# print_info("Ogi", 25)


# def print_inf(arr=[]):
#     arr.append(1)
#     print(arr)
#
# print_inf([123])
# print_inf()
# print_inf([1234])
# print_inf()
# print_inf([12345])
# print_inf()

# def print_smth(name, *args):
#     print(name, ':', sep='')
#     print("1")
#     for i in args:  # if args not empty
#         print(f'{i} element')
#     print('2')
#
#
# print_smth(10)
# print('----------')
# print_smth(1, 2, 3, 5, 57, 89)
#
# for i in []:
#     print('Empty')


# x = 1000

# def do(a):
#     b = 10
#     def do2():
#         nonlocal b
#         b = 1
#         return 0
#
#     global x
#     x = a + b + do2()
#     return x

# def do(a):
#     b = 10
#     def do2():
#         nonlocal b
#         b = 1
#         return 0
#
#     global x
#     do2()
#     x = a + b
#     return x

# do(2)
# print(x)
#
#
# def factor(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factor(n-1)

# def fact(n):
#     suma = 1
#     for i in range(1, n+1):
#         suma = suma * i
#     return suma
#
# # print(factor(6))
# # print(fact(6))
#
# fact2 = lambda x: fact(x) * 2
#
# print((lambda x: fact(x) * 2)(6))  # fact2(6)

# print((lambda a, b, c: a+b+c)(1, 2, 3))
