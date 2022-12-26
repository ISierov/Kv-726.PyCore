import random


def next_palindromic_number(val):
    """
    Search the next palindromic number for the given number
    :param val: some number
    :return: The next palindromic for the given number
    """
    palindromic = int(val)
    while True:
        palindromic += 1
        if palindromic == int(str(palindromic)[::-1]):
            return palindromic


def bonus_time(salary, bonus):
    if bonus:
        return '$' + str(salary * 10)
    else:
        return '$' + str(salary)


def sort_dict(dict1):
    sorted_keys = sorted(dict1, key=dict1.get, reverse=True)
    sorted_values = []
    for k in sorted_keys:
        sorted_values.append(dict1.get(k))
    return list(zip(sorted_keys, sorted_values))


# The best from codewars.com
def sort_dict2(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


def find_average(l):
    if len(l) == 0:
        return 0
    s = 0
    for item in l:
        s += item
    return s / len(l)


# From the codewars.com
def find_average_codewars(array):
    return sum(array) / len(array) if array else 0


def distance(x1, y1, x2, y2):
    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)


def filter_words(st):
    return " ".join(st.split()).capitalize()


def number_to_string(num):
    return str(num)


def reverse(st):
    return " ".join(list(reversed(st.split())))


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {}!".format(name)


def reverse_list(li):
    return list(reversed(li))


def solution(number):
    mult = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            mult += i
    return mult


# From the codewars.com
def solution_codewars(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        return True
    return False
    # return True if fuel_left * mpg >= distance_to_pump else False


def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo"
    return name + " does not play banjo"


def bool_to_word(boolean):
    return "Yes" if boolean else "No"


def count_sheep(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count


# From the codewars.com
def count_sheep_codewars(arrayOfSheeps):
    return arrayOfSheeps.count(True)


def correct_tail(body, tail):
    return body[-1] == tail


def summation(num):
    summa = 0
    for x in range(num + 1):
        summa += x
    return summa


def summation1(num):
    li = []
    for x in range(num + 1):
        li.append(x)
    return sum(li)


# From the codewars.com
def summation_codewars(num):
    return sum(range(num + 1))


def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst


# From the codewars.com
def list_animals_codewars(animals):
    return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))


def double_char(s):
    ns = ""
    for i in s:
        ns = ns + i + i
    return ns


# From the codewars.com
def double_char_codewars(s):
    return ''.join(c * 2 for c in s)


class Ball:
    def __init__(self, b_type='regular'):
        self.type = b_type


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        Human.__init__(self, name)


class Woman(Human):
    def __init__(self, name):
        Human.__init__(self, name)


class Person:
    def __init__(self, name, age):
        self.info = "{}s age is {}".format(name, age)

