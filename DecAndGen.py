# doubled_odds = [n * 2 for n in range(10) if n % 2 == 1]
# print(doubled_odds)

# vec1 = [3, 10, 2]
# vec2 = [-20, 5, 1]
# print(zip(vec1, vec2))
# print(list(zip(vec1, vec2)))
# dot_mul = [u*v for u, v in zip(vec1, vec2)]
# print(dot_mul)
# dot_prod = sum(dot_mul)
# print(dot_prod)

# s = 'abc'
# a = [1, 2, 3, 4]
#
# print(dict(zip(s, a)))
#
# print(dict(zip(a, s)))

#
# s = 'abcd'
# t = (10, 20, 30)
# g = [(s[i], t[i]) for i in range(len(s)-1)]
# for item in g:
#     print(item)

# winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
# fake_lottery_numbers = map(lambda n: 2*n, winning_lottery_numbers)
# print(list(fake_lottery_numbers))
#
# from functools import reduce
#
# print('l', reduce(lambda x, y: x+y, [47, 11, 42, 13]))
#
# def a_add_b(a, b):
#     print("a:{} b:{}".format(a, b))
#     return a+b
#
# print('f', reduce(a_add_b, [47, 11, 42, 13]))

'''

list, tuple

num, str -> кількусть символів в його записі
tuple, list -> кількість елементів що вміщують
за допомогою кастомного ітератора

'>>> [1234, 'sfdgf', 14676.543, (1345, 67)]

4, 5, 9, 2

'''

array = [1234, 'sfdgf', 14676.543, (1345, 67)]

class MyClass:
    def __init__(self, array):
        self.arr = array

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(array):
            raise StopIteration
        if type(self.arr[self.i]) in (int, float):
            l = len(str(self.arr[self.i]))
        elif type(self.arr[self.i]) in (tuple, str, list):
            l = len(self.arr[self.i])
        else:
            raise TypeError('Dont know type')
        self.i += 1
        return l


myclass = MyClass(array)
try:
    for val in myclass:
        print(val)
except TypeError as e:
    print(e)
except StopIteration:
    print('End')
