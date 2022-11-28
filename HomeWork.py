# # ------------ 1. Записати в стрічку філософію Пайтона
# python = '''
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# '''

# ------------ a. Знайти в заданій стрічці кількість входжень слів (better, never, is)
# a = python.find('better')
# a1 = python.find('never')
# a2 = python.find('is')
# print(a, a1, a2, sep=' ////// ')

# ------------ b. Вивести весь текст у верхньому регістрі (всі великі літери)
# a = python.upper()
# print(a)

# ------------ c. Замінити всі входження символу “і” на “&”
# a = python.replace('i', '&')
# print(a)


