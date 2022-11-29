# 3 -- поміняти між собою значення 2 змінних, не викор 3
x = int(input("x = "))
y = int(input("y = "))

x = x + y
y = x - y
x = x - y

print("x =",x, "y =",y)

# abo
x = input("x = ")
y = input("y = ")

x, y = y, x
print("x =",x, "y =",y)