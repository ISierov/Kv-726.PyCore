# ex 1
new_string = "Namespaces are one honking great idea -- let's do more of those!"
counter = 0
for i in new_string.split():
    if i in ["better", "new", "is"]:
        counter += 1
print(counter)
print(new_string.upper())
print(new_string.replace("i", "&"))

# ex 2
number = input()
mult = 1
for i in number:
    mult *= int(i)
print(mult)  # multiplication
reversed_number = ''
i = -1
for _ in range(4):
    reversed_number += number[i]
    i -= 1
print(reversed_number)  # reversed number
list_number = []
number = int(number)
while number > 0:  # make a list of the digits of iur number
    n = number % 10
    list_number.append(n)
    number //= 10
new_list = []  # make a list of sorted digits
for i in range(4):
    new_list.append(max(list_number))
    list_number.remove(max(list_number))
print(int(''.join(map(str, new_list))))

# ex 3

a = int(input("a = "))
b = int(input("b ="))
a = a + b
b = a - b
a = a - b
print(f"a = {a} \nb = {b}")
