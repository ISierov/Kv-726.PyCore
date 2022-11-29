# Homework #3.1

# 1. Записати в стрічку філософію Пайтона (читання з файлу "dzen.txt")
try:
    file = open("dzen.txt", "r")
    try:
        data = file.read()
    except Exception as e:
        print(e)
    finally:
        file.close()
except Exception as ex:
    print(ex)

# 1.a. Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('Number of occurrences of the word "better":', data.count('better'))
print('Number of occurrences of the word "never":', data.count('never'))
print('Number of occurrences of the word "is":', data.count('is'))

# 1.b. Вивести весь текст у верхньому регістрі (всі великі літери)
print(data.upper())

# 1.c. Замінити всі входження символу “і” на “&”
print(data.replace('i', '&'))

# 2. Задано чотирицифрове натуральне число
number = input('Введіть чотирицифрове натуральне число: ')
goodNumberFlag = True
for digit in number:
    if not digit.isdigit():
        print('Symbol <', digit, '> is not a number.')
        goodNumberFlag = False

if goodNumberFlag and int(number) < 0 and int(number) > 9999:
    goodNumberFlag = False
    print('Число не відповідає вимогам')
    

if goodNumberFlag:
# 2.a. Знайти добуток цифр цього числа
    mult = 1
    for digit in number:
        if digit.isdigit():
            mult *= int(digit)
    print('Добуток чисел', mult)

# 2.b. Записати число в реверсному порядку       
    n = list(number)
    n.reverse()
    print('Число в реверсному порядку ', "".join(n))

# 2.c. Посортувати цифри,що входять в дане число
    n.sort()
    print('Відсортовані цифри числа ', "".join(n))

# 3. Поміняти між собою значення двох змінних, не використовуючи третьої змінної
a = input('Введіть значення змінної A: ')
b = input('Введіть значення змінної B: ')
a, b = b, a
print('Значення змінних поміняно: A = ', a, ' B = ', b)
