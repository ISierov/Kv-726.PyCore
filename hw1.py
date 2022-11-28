# Task 1
import string

text = input("<Task 1>\nEnter random wise of Python ZEN: ")

# Task 1.a
newText = text.translate(str.maketrans(' ', ' ', string.punctuation))
txtStr = newText.split(" ")

keys = ['better', 'never', 'is']
values = [0, 0, 0]

for word in txtStr:
    for i in range(3):
        if word == keys[i]:
            values[i] +=1

print("\n<Task 1.a>\nFrequency of words:")
for i in range(3):
    print(f"{keys[i]} = {values[i]}")


# Task 1.b
print(f"\n<Task 1.b>\n{text.upper()}")

# Task 1.c
resText = text.replace("i", "&")
print(f"\n<Task 1.c>\n{resText}")




# Task 2
import random
import math

numRand = random.randint(1000,9999)
print(f"\n\n\n<Task 2>\nRandom generated number: {numRand}")


# Task 2.a
myList = [int(num) for num in str(numRand)]
print(f"\n<Task 2.a>\n{math.prod(myList)}")


# Task 2.b
reversedList = myList
reversedList.reverse()
temp1 = [str(i) for i in reversedList]
temp2 = "".join(temp1)
res = int(temp2)
print(f"\n<Task 2.b>\n{res}")


# Task 2.c
sortedList = myList
sortedList.sort()
temp1 = [str(i) for i in sortedList]
temp2 = "".join(temp1)
res = int(temp2)
print(f"\n<Task 2.c>\n{res}")




# Task 3
import random

a = random.randint(0, 20)
b = random.randint(0, 20)

while a == b:
    a = random.randint(0, 20)
    b = random.randint(0, 20)

print(f"\n\n\n<Task 3>\nRandom generated numbers:\na = {a}\nb = {b}")

a, b = b, a

print(f"\nSwapped numbers:\na = {a}\nb = {b}")
