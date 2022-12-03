# Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.
# If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat must receive only his stated salary.
# Return the total figure the individual will receive as a string prefixed with "$"
# STRINGSLOGIC


def bonus_time(salary, bonus):
    if bonus is True:
        salary *= 10
    else:
        salary == salary
    return f'${salary}'