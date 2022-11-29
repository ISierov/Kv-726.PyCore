#  2.1 -- 4цифрове -> добуток
user_number = input("enter four-digit natural number: \n")
number = int(user_number)
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10
multiplication = a * b * c * d
print(a, b, c, d, multiplication)
# print((number // 1000) * (number // 100) % 10) * ((number // 10) % 10) * (number % 10))


#  2.2. --4цифрове -> реверс
print(user_number[::-1])


#  2.3 -- 4цифрове -> посортувати
list_number = list(user_number)
list_number.sort()
print(list_number)
