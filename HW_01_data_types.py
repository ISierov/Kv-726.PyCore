"""HomeWork"""
# Записати в стрічку філософію Пайтона
the_zen_of_python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('\n')
print(
    f"Word 'better' appears {len(the_zen_of_python.split('better')) - 1} times")
print(
    f"Word 'never' appears {len(the_zen_of_python.split('never')) - 1} times")
print(f"Word 'is' appears {len(the_zen_of_python.split('is')) - 1} times")
print('\n\n')

# Вивести весь текст у верхньому регістрі(всі великі літери)
print(the_zen_of_python.upper())

# Замінити всі входження символу “і” на “&”
the_zen_of_python = the_zen_of_python.replace('i', '&')

'''2. Задано чотирицифрове натуральне число.'''
# Знайти добуток цифр цього числа.
num_1 = 5625
num_product = 1
for num in str(num_1):
    num_product *= int(num)
print(f'Product is {num_product}')

# Записати число в реверсному порядку.
reversed_num = str(num_1)[::-1]
reversed_num = int(reversed_num)
print(f'Reversed {num_1} is {reversed_num}')

# Посортувати цифри, що входять в дане число
temp_list = list(str(num_1))
temp_list.sort()
sorted_nums = ''.join(temp_list)
print(sorted_nums)

# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a = 5
b = 250
print('a =', a)
print('b =', b)
# MAIN CHANGING IS HERE :)
a, b = b, a
print('a =', a)
print('b =', b)
