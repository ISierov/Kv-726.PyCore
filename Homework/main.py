# Glib Zamikula

import hometasks as ht


def headline(s, n=10):
    """
    Print separating line with head text
    :param n:
    :param s: String to put in line
    :return: Nothing
    """
    print('\n' + '-' * n + s + '-' * n)


def isnatural(val):
    """
    Testing if the given data is a natural number
    :param val: number
    :return: True if given number is a natural
    """
    if len(val) == 0:
        return False
    for digit in number:
        if not digit.isdigit():
            return False
    return True


if __name__ == '__main__':

    headline(" 1. Next Palindromic Number ")
    while True:
        number = input('Input the natural number or <0> for exit: ')
        # Verify for exit code
        if number == '0':
            break

        if isnatural(number):
            print('The next palindromic number for {} is {}'.format(number, ht.next_palindromic_number(number)))
        else:
            print("Error: <{}> is a not natural number".format(number))

    headline(" 2. Do I get a bonus? ")
    salary = 234
    print("Salary value is {}, bonus is {} and summary value is {}".format(str(salary), True, ht.bonus_time(234, True)))
    print(
        "Salary value is {}, bonus is {} and summary value is {}".format(str(salary), False, ht.bonus_time(234, False)))

    headline(" 3. Sorting Dictionaries ")
    di = {1: 3, 2: 10, 3: 5, 5: 3}
    print(di)
    print(ht.sort_dict(di))

    headline(" 4. Calculate average ")
    l_num = [4, 23, 6, 4]
    print(l_num)
    # l_num = []
    print("The average of the number: " + str(ht.find_average(l_num)))

    headline(" 5. Find The Distance Between Two Points ")
    a = (1, -4)
    b = (6, 2)
    print(a, b)
    print("Distance between two points: " + str(ht.distance(a[0], a[1], b[0], b[1])))

    headline(" 6. No yelling! ")
    s = "Hi YOU!"
    print("Was <{}> - now is <{}>".format(s, ht.filter_words(s)))
    s = "hAy,   whAt are    yOU   doIng?"
    print("Was <{}> - now is <{}>".format(s, ht.filter_words(s)))

    headline(" 7. Convert a Number to a String ")
    n = 6758
    print("Number {} to string '{}'".format(n, ht.number_to_string(n)))

    headline(" 8. Reversing Words in a Strings ")
    s = " Hi you! It's me. "
    print('String "{}" to reversed string "{}" '.format(s, ht.reverse(s)))

    headline(" 9. Jenny's secret message ")
    names = ['G', 'S', 'Johnny']
    for name in names:
        print('For "{}" greeting is: "{}" '.format(name, ht.greet(name)))

    headline(" 10. Reverse List Order ")
    lst = [1, 3, 5, 9]
    print("Was {} - now is {}".format(lst, ht.reverse_list(lst)))

    headline(" 11. Multiples of 3 or 5 ")
    lst = [1, 3, 5, 9, -5, 34, 87]
    for item in lst:
        print("For number {} solution is: {} ".format(item, ht.solution(item)))

    headline(" 12. Will you make it? ")
    lst = [(50, 25, 2), (51, 25, 2), (49, 25, 2)]
    for item in lst:
        print("For distance/mpg/gallons {} solution is: {} ".format(item, ht.zero_fuel(item[0], item[1], item[2])))

    headline(" 13. Are You Playing Banjo? ")
    names = ['Glib', 'Ray', 'Sergio', 'Johnny', 'ronny']
    for name in names:
        print("{}, are You Playing Banjo? {} ".format(name, ht.are_you_playing_banjo(name)))

    headline(" 14. Convert boolean values to strings 'Yes' or 'No'. ")
    print("True is {}".format(ht.bool_to_word(True)))
    print("False is {}".format(ht.bool_to_word(False)))

    headline(" 15. Counting sheep... ")
    sheep = [True, True, True, False, True, True, True, True, True, False, True, False,
             True, False, False, True, True, True, True, True, False, False, True, True]
    print('We have {} sheep'.format(ht.count_sheep(sheep)))

    headline(" 16. Is this my tail? ")
    animals = [('cow', 'w'), ('donkey', 'y'), ('dog', 'o')]
    for animal in animals:
        print("Is correct pair animal/tail {}? Answer is: {} ".format(animal, ht.correct_tail(animal[0], animal[1])))

    headline(" 17. Grasshopper - Summation ")
    numbers = [3, 8, 36, 15, 2678]
    for item in numbers:
        print("For number {} summation is: {} ".format(item, ht.summation(item)))

    headline(" 18. Fix the loop! ")
    animals = ['dog', 'cat', 'elephant']
    print(animals)
    print(ht.list_animals(animals))

    headline(" 19. Double Char ")
    print(animals)
    for item in animals:
        print("{} >>> {}".format(item, ht.double_char(item)))

