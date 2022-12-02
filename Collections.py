
arr = [1, 2, 4, 5, 10]
# print(id(arr))
# new = arr.copy()
# arr.append(5)
# arr.clear()
# arr.count(1)
# new.extend([5])
# n = arr.index(4)
# arr.insert(3, [5])
# arr.pop()
# arr.pop(1)
# arr.remove(2)

# arr.reverse()
# arr.sort()
# new_sort = arr.copy().sort()  # new_sort = sorted(arr)
# new_rev = reversed(arr)
# print(id(arr))
# print(id(new_sort))
# print(id(new_rev))

# str = list('String')
# print(str)
# m = max(arr)
# m = min(arr)
# m = sum(arr)


# print(m)
# print(n)
# print(new)
#
# mylist = [True, True, True]
# x = all(mylist)
# print(x)
# ####################
# mylist = [0, 1, 1]
# x = all(mylist)
# print(x)
# ####################
# mydict = {4: "Apple", 2: "Orange"}
# x = all(mydict)
# print(x)

# mylist = [False, True, False]
# x = any(mylist)
# print(x)
# ####################
# mytuple = (0, [], False)
# x = any(mytuple)
# print(x)
# ####################
# mydict = {0 : "Apple", 1 : "Orange"}
# x = any(mydict)
# print(x)

# x = ['apple', 'banana', 'cherry']
# y = enumerate(x, 100)
# print(list(y))

# new_arr = [i**2 for i in arr if i % 2 == 0]
# print(arr)
# print(new_arr)

# a = [1, 2, 3]
# a1, a2, a3 = a
#
# print(a1, a2, a3)

# a = (1, 5, 4)
# b = reversed(a)
# print(tuple(b))


# s1 = {1, 2, 5}
# s2 = {2, 5, 7}
# s3 = s1.difference(s2)
# s1.difference_update(s2)
# s1.discard(9)
# s2.remove(9)
# s1.intersection_update(s2)
# s3 = {7, 8, 9}
# s3 = s1.union(s2)
# print(s3)
# print(s1.isdisjoint(s3))
# print(s1)
# print(s3)

# s_diff = s1 - s1.intersection(s2)
# s_diff = s1.difference(s2)


# s1 = {(), 1, ''}
# s3 = {1, 2}
# print(s1.issubset(s3))
# print(s3.issubset(s1))  # s1.issuperset(s3)
# print(s1.issuperset(s3))
# n = s1.pop()
# print(s1)
# print(n)

# d = {1: [1234, 145], 2: 0, 3: 0, 5: 'name'}
#
# print(id(d[2]), id(d[3]))

# d = {'name': 'Vasyl', 'surname': 'Bilan', 'id': '1', 'task': 'run application'}
# for key in d:
#     print("student {} = {}".format(key, d[key]))
# for key, val in d.items():
#     print("{} = {} .".format(key, val))
# for key in d.keys():
#     print("student {} = {}".format(key, d[key]))
# for val in d.values():
#     print("student {} = {}".format("?", val))

# odd_squares = {x: x * x for x in range(11) if x % 2 == 1}
# print(odd_squares)
#
# odd = (2 ** x for x in range(10))
# print(tuple(odd))
