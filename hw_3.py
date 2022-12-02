# GZ/Homework #3
print('\nGZ/Homework #3')

# 1. Записати в стрічку філософію Python (читання з файлу "dzen.txt")
print('\n#1. Записати в стрічку філософію Python (читання з файлу "dzen.txt")\n')
goodData = True
try:
    file = open("dzen.txt", "r")
    try:
        data = file.read()
    except Exception as e:
        print(e)
        goodData = False
    finally:
        file.close()
except Exception as ex:
    print(ex)
    goodData = False

if goodData:
    print(data)

    # 1.a. Знайти в заданій стрічці кількість входжень слів (better, never, is)
    print('#1.a. Аналіз тексту філософії Python:\n')
    print('Кількість входжень слів "better":', data.count('better'))
    print('Кількість входжень слів "never":', data.count('never'))
    print('Кількість входжень слів "is":', data.count('is'))

    # 1.b. Вивести весь текст у верхньому регістрі (всі великі літери)
    print('\n#1.b. Текст у верхньому регистрі:\n')
    print(data.upper())

    # 1.c. Замінити всі входження символу “і” на “&”
    print('#1.c. Заміна символи “і” на “&”:\n')
    print(data.replace('i', '&'))

# 2. Задано чотирицифрове натуральне число
print('\n#2. Операції з чотирицифровим числом')
number = input('Введіть чотирицифрове натуральне число: ')
goodNumberFlag = True
for digit in number:
    if not digit.isdigit():
        print('Символ <', digit, '> не є цифрою.')
        goodNumberFlag = False

if goodNumberFlag and (int(number) < 1000 or int(number) > 9999):
    goodNumberFlag = False

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

else:
    print('Число не відповідає вимогам або ж не є числом!')


# 3. Поміняти між собою значення двох змінних, не використовуючи третьої змінної
print('\n#3. Поміняти між собою значення двох змінних, не використовуючи третьої змінної')
a = input('Введіть значення змінної A: ')
b = input('Введіть значення змінної B: ')
a, b = b, a
print('Значення змінних поміняно: A = ', a, ' B = ', b)
