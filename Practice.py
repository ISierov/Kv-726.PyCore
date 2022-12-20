# Створити клас багатокутників. З цього класу наслідується клас прямокутників, для класу прямокутників
# додати метод пошуку площі
#
# class Polygon:
#     def __init__(self, num_of_sides):
#         self.sides = num_of_sides
#
#
# class Recatngles(Polygon):
#     def __init__(self, a=0, b=0):
#         super().__init__(num_of_sides=4)
#         self.__set_a(a)
#         self.__set_b(b)
#
#     def get_a(self):
#         return self.__a
#
#     def __set_a(self, a=0):
#         if a < 0:
#             self.__a = 0
#         else:
#             self.__a = a
#
#     def get_b(self):
#         return self.__b
#
#     def __set_b(self, b=0):
#         if b < 0:
#             self.__b = 0
#         else:
#             self.__b = b
#
#     def area(self):
#         return self.get_a()*self.get_b()
#
# if __name__ == '__main__':
#     Rect1 = Recatngles()
#     Rect2 = Recatngles(2, 4)
#
#     print(Rect2.area())
#     print(Rect1.area())


# while True:
#     try:
#         data = int(input())
#         if data % 2 == 0:
#             print('It\'s even')
#             break
#         else:
#             print('It\'s odd')
#             break
#     except ValueError as err:
#         print('Not valid data: ', err)
#
#
#
# from random import randint
#
# who = randint(0, 100) % 2
# if who == 0:
#     print('Nikita')
# elif who == 1:
#     print('Maria')
