# class Human:
#     def who(self):
#         return 'human'
#
# class Parent:
#     def who(self):
#         return 'parent'
#
# class Child(Parent):
#     def who(self):
#         return 'child'
#
#
# c = Child()
# c.val = 100
# print(c.who())
#
# c.__class__ = Parent
# print(c.who())
# print(c.val)
#
# c.__class__ = Human
# print(c.who())
# print(c.val)


class Par1 (object):
    def method_1(self):
        return '(Par1 method_1)'

    def method_2(self):
        return '(Par1 method_2)'


class Par2 (object):
    def method_2(self):
        return '(Par2 method_2)'

    def method_3(self):
        return '(Par2 method_3)'


class Child(Par1, Par2):
    pass

x = Child()
print(x.method_1(), x.method_2(), x.method_3())

