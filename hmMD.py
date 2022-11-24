# TASK 111111111111111111111111111111111111111111111111111111111111111111111111111111111111
a = ('Beautiful is better than ugly.')
b = ('Explicit is better than implicit.')
c = ('Simple is better than complex.')
d = ('Complex is better than complicated.')
e = ('Flat is better than nested.')
f = ('Sparse is better than dense.')
g = ('Readability counts.')
h = ('Special cases arent special enough to break the rules.')
i = ('Although practicality beats purity.')
j = ('Errors should never pass silently.')
k = ('Unless explicitly silenced.')
l = ('In the face of ambiguity, refuse the temptation to guess.')
m = ('There should be one-- and preferably only one --obvious way to do it.')
o = ('Although that way may not be obvious at first unless youre Dutch.')
p = ('Now is better than never.')
q = ('Although never is often better than *right* now.')
r = ('If the implementation is hard to explain, its a bad idea.')
s = ('Namespaces are one honking great idea -- lets do more of those!')
zen = a+b+c+d+e+f+g+h+i+j+k+l+m+o+p+q+r+s
print (str(zen))
print(zen.count('better'))
print(zen.count('never'))
print(zen.count('is'))
print(zen.upper())
change = zen
old_letter = 'i'
new_letter = '&'
change = zen.replace(old_letter,new_letter)
print(change)
# TASK22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
n1 = int(input('Enter your number:'))
n2 = 0
prod = 1
while n1 > 0:
    digit = n1 % 10
    n1 //= 10
    prod *= digit
    n2 *= 10
    n2 += digit


print(prod)
print(n2)



hades=input('Enter your number:').split()
for i in range(len(hades)):
    hades[i] = int(hades[i])
hades.sort()
print(*hades)
# TASK33333333333333333333333333333333333333333333333333333
a = input('a =')
b = input ('b =')
a,b = b,a

print ('a =',a)
print ('b =',b)